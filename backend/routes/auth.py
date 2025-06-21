"""Authentication routes for the application."""

from flask import Blueprint, request, jsonify
from flask_bcrypt import Bcrypt
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity, get_jwt
from models.account import User, db

# Create a blueprint for authentication routes
auth_bp = Blueprint('auth', __name__, url_prefix='/api/auth')
bcrypt = Bcrypt()

# JWT token blacklist (in-memory for simplicity - use Redis in production)
token_blocklist = set()

@auth_bp.route('/signup', methods=['POST'])
def signup():
    """Register a new user."""
    data = request.get_json()
    
    # Validate input
    if not data or not data.get('username') or not data.get('email') or not data.get('password'):
        return jsonify({'error': 'Missing required fields'}), 400
    
    # Check if user already exists
    if User.query.filter_by(username=data['username']).first():
        return jsonify({'error': 'Username already exists'}), 409
    
    if User.query.filter_by(email=data['email']).first():
        return jsonify({'error': 'Email already exists'}), 409
    
    # Create new user
    hashed_password = bcrypt.generate_password_hash(data['password']).decode('utf-8')
    new_user = User(
        username=data['username'],
        email=data['email'],
        password=hashed_password
    )
    
    # Save user to database
    db.session.add(new_user)
    db.session.commit()
    
    return jsonify({
        'message': 'User created successfully',
        'user': new_user.to_dict()
    }), 201


@auth_bp.route('/login', methods=['POST'])
def login():
    """Authenticate a user and return a JWT token."""
    try:
        print("Login attempt received")
        data = request.get_json()
        
        # Validate input
        if not data:
            print("No JSON data received")
            return jsonify({'error': 'Missing request data'}), 400
            
        if not data.get('username') or not data.get('password'):
            print(f"Missing credentials: username={bool(data.get('username'))}, password={bool(data.get('password'))}")
            return jsonify({'error': 'Missing username or password'}), 400
        
        # Find user by username
        username = data['username']
        print(f"Looking up user: {username}")
        user = User.query.filter_by(username=username).first()
        
        # Check if user exists and password is correct
        if not user:
            print(f"User not found: {username}")
            return jsonify({'error': 'Invalid username or password'}), 401
            
        if not bcrypt.check_password_hash(user.password, data['password']):
            print(f"Invalid password for user: {username}")
            return jsonify({'error': 'Invalid username or password'}), 401
        
        # Create access token
        print(f"Creating token for user ID: {user.id}")
        access_token = create_access_token(identity=user.id)
        
        print(f"Login successful for user: {username}")
        return jsonify({
            'message': 'Login successful',
            'user': user.to_dict(),
            'access_token': access_token
        }), 200
    except Exception as e:
        print(f"Login error: {str(e)}")
        return jsonify({'error': f'An error occurred during login: {str(e)}'}), 500


@auth_bp.route('/logout', methods=['POST'])
@jwt_required()
def logout():
    """Log out a user by blacklisting their JWT token."""
    jti = get_jwt()['jti']
    token_blocklist.add(jti)
    
    return jsonify({'message': 'Logout successful'}), 200


@auth_bp.route('/me', methods=['GET'])
@jwt_required()
def get_current_user():
    """Get the current authenticated user's information."""
    try:
        # Get the JWT identity
        user_id = get_jwt_identity()
        print(f"JWT identity (user_id): {user_id}")
        
        # Get the user from the database
        user = User.query.get(user_id)
        
        if not user:
            print(f"User with ID {user_id} not found in database")
            return jsonify({'error': 'User not found'}), 404
        
        print(f"User found: {user.username}")
        return jsonify({'user': user.to_dict()}), 200
    except Exception as e:
        print(f"Error in get_current_user: {str(e)}")
        return jsonify({'error': 'An error occurred while retrieving user information'}), 500
