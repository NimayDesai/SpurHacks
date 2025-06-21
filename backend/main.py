from flask import Flask, request, jsonify
from flask_cors import CORS

# Initialize Flask app
app = Flask(__name__)
CORS(app)  # Enable CORS for frontend communication

# Basic configuration
app.config['SECRET_KEY'] = 'your-secret-key-here'

# Sample data (replace with database later)
users = []

# Routes
@app.route('/')
def home():
    return jsonify({"message": "Flask API is running!"})

@app.route('/api/health')
def health_check():
    return jsonify({"status": "healthy", "message": "API is working"})

@app.route('/api/login', methods=['POST'])
def login():
    data = request.get_json()
    
    if not data or 'email' not in data or 'password' not in data:
        return jsonify({"error": "Email and password required"}), 400
    
    email = data['email']
    password = data['password']
    
    # Basic validation (replace with real authentication)
    if email and password:
        return jsonify({
            "message": "Login successful",
            "user": {"email": email}
        }), 200
    else:
        return jsonify({"error": "Invalid credentials"}), 401

@app.route('/api/register', methods=['POST'])
def register():
    data = request.get_json()
    
    if not data or 'email' not in data or 'password' not in data:
        return jsonify({"error": "Email and password required"}), 400
    
    email = data['email']
    password = data['password']
    
    # Check if user already exists
    if any(user['email'] == email for user in users):
        return jsonify({"error": "User already exists"}), 409
    
    # Add user (in real app, hash password and save to database)
    new_user = {"email": email, "password": password}
    users.append(new_user)
    
    return jsonify({
        "message": "User registered successfully",
        "user": {"email": email}
    }), 201

# Error handlers
@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Endpoint not found"}), 404

@app.errorhandler(500)
def internal_error(error):
    return jsonify({"error": "Internal server error"}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=4000)