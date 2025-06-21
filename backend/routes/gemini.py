import google.generativeai as genai
import os
from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity

# Create blueprint
gemini_bp = Blueprint('gemini', __name__, url_prefix='/api/gemini')

# Configure Gemini API
GEMINI_API_KEY = os.environ.get('GEMINI_API_KEY')
if not GEMINI_API_KEY:
    raise ValueError("GEMINI_API_KEY environment variable is required")

genai.configure(api_key=GEMINI_API_KEY)

# Initialize the model
model = genai.GenerativeModel('gemini-pro')

@gemini_bp.route('/generate', methods=['POST'])
@jwt_required()  # Remove this if you don't want authentication
def generate_response():
    """Generate a response using Gemini API."""
    try:
        data = request.get_json()
        
        if not data:
            return jsonify({"error": "No data provided"}), 400
        
        prompt = data.get('prompt')
        instructions = data.get(
            """
               You will be given a topic.

Your task is to write a high-quality educational narration script in the style of a 3Blue1Brown video, based on that topic.

Instructions:
1. The script should be approximately 200 words in length.
2. Write it as continuous narration — the exact words that would be spoken in a video.
3. Do not include speaker labels, scene directions, formatting, emojis, or visual references of any kind.
4. The narration should flow naturally, guiding the viewer from intuition to insight.
5. Focus on clarity and conceptual understanding. You may use analogies, rhetorical questions, or simple build-up, but no lists or definitions without context.
6. Do not explain what will be shown visually — only the narration that would accompany those visuals.

The result should feel like the voiceover from a 3Blue1Brown video: elegant, thoughtful, and tightly focused on the concept.             
    """)
        
        if not prompt:
            return jsonify({"error": "Prompt is required"}), 400
        
        # Combine instructions and prompt
        full_prompt = f"{instructions}\n\n{prompt}" if instructions else prompt
        
        # Generate response
        response = model.generate_content(full_prompt)
        
        return jsonify({
            "success": True,
            "response": response.text,
            "prompt": prompt,
            "instructions": instructions
        }), 200
        
    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500

@gemini_bp.route('/chat', methods=['POST'])
@jwt_required()  # Remove this if you don't want authentication
def chat():
    """Have a conversation with Gemini."""
    try:
        data = request.get_json()
        
        if not data:
            return jsonify({"error": "No data provided"}), 400
        
        messages = data.get('messages', [])
        system_instruction = data.get('system_instruction', '')
        
        if not messages:
            return jsonify({"error": "Messages are required"}), 400
        
        # Start a chat session
        chat_session = model.start_chat(history=[])
        
        # Add system instruction if provided
        if system_instruction:
            chat_session.send_message(f"System: {system_instruction}")
        
        # Send the latest message
        latest_message = messages[-1] if messages else ""
        response = chat_session.send_message(latest_message)
        
        return jsonify({
            "success": True,
            "response": response.text,
            "message_count": len(messages)
        }), 200
        
    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500

@gemini_bp.route('/health', methods=['GET'])
def health_check():
    """Check if Gemini API is configured correctly."""
    try:
        # Test with a simple prompt
        test_response = model.generate_content("Say 'API is working'")
        
        return jsonify({
            "success": True,
            "status": "healthy",
            "test_response": test_response.text
        }), 200
        
    except Exception as e:
        return jsonify({
            "success": False,
            "status": "unhealthy",
            "error": str(e)
        }), 500