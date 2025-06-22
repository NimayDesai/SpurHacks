"""Main application file for the backend service."""

import os
from datetime import timedelta
from flask import Flask, jsonify
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from flask_socketio import SocketIO
from dotenv import load_dotenv
from models.account import db, User
from routes.auth import auth_bp, token_blocklist
from routes.animation import animation_bp
from routes.tavus import tavus_bp
from routes.ai_config import ai_config_bp
from routes.ai_agent import ai_agent_bp
from routes.webrtc import init_webrtc_routes

# Load environment variables
load_dotenv()
from routes.gemini import gemini_bp


def create_app():
    """Create and configure the Flask application."""
    app = Flask(__name__)
    
    # Configure the app
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['JWT_SECRET_KEY'] = os.environ.get('JWT_SECRET_KEY', 'super-secret-key-for-development')
    app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(hours=1)
    app.config['JWT_TOKEN_LOCATION'] = ['headers']
    app.config['JWT_HEADER_NAME'] = 'Authorization'
    app.config['JWT_HEADER_TYPE'] = 'Bearer'
    app.config['JWT_ERROR_MESSAGE_KEY'] = 'error'
    # Make sure JSON responses can be properly returned from JWT-protected routes
    app.config['PROPAGATE_EXCEPTIONS'] = True
    
    # Initialize extensions
    db.init_app(app)
    bcrypt = Bcrypt(app)
    jwt = JWTManager(app)
    CORS(app, resources={r"/*": {"origins": "*"}}, supports_credentials=True)
    
    # Initialize SocketIO with better WebSocket configuration
    socketio = SocketIO(
        app, 
        cors_allowed_origins="*", 
        logger=False, 
        engineio_logger=False,
        async_mode='threading',
        transports=['websocket', 'polling'],
        ping_timeout=60,
        ping_interval=25
    )
    
    # Initialize WebRTC routes
    init_webrtc_routes(socketio)
    
    # Register blueprints
    app.register_blueprint(auth_bp)
    app.register_blueprint(animation_bp)
    app.register_blueprint(tavus_bp)
    app.register_blueprint(ai_config_bp)
    app.register_blueprint(ai_agent_bp)
    app.register_blueprint(gemini_bp)
    
    @jwt.token_in_blocklist_loader
    def check_if_token_is_revoked(jwt_header, jwt_payload):
        """Check if a token is in the blocklist."""
        jti = jwt_payload["jti"]
        return jti in token_blocklist
        
    @jwt.invalid_token_loader
    def invalid_token_callback(error_string):
        """Handle invalid token errors."""
        return jsonify({
            'error': 'Invalid token',
            'message': error_string
        }), 401
    
    @jwt.unauthorized_loader
    def missing_token_callback(error_string):
        """Handle missing token errors."""
        return jsonify({
            'error': 'Authorization required',
            'message': error_string
        }), 401
        
    @jwt.expired_token_loader
    def expired_token_callback(jwt_header, jwt_payload):
        """Handle expired token errors."""
        return jsonify({
            'error': 'Token expired',
            'message': 'The token has expired'
        }), 401
    
    @app.route('/')
    def index():
        """Default route for health check."""
        return {'message': 'SpurHacks API is running'}, 200
    
    # Create tables
    with app.app_context():
        db.create_all()
        
    return app, socketio


def main():
    """Run the application."""
    app, socketio = create_app()
    # Disable reloader to prevent restarts when manim files are created
    socketio.run(
        app, 
        debug=True, 
        host='0.0.0.0', 
        port=int(os.environ.get('PORT', 5002)),
        use_reloader=False
    )


if __name__ == "__main__":
    main()
