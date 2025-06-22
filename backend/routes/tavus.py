"""Tavus AI agent API routes."""

import os
import logging
from flask import Blueprint, request, jsonify
from services.tavus_agent import TavusAgent

logger = logging.getLogger(__name__)

tavus_bp = Blueprint('tavus', __name__, url_prefix='/api/tavus')

# Initialize Tavus agent
tavus_agent = TavusAgent(os.getenv('TAVUS_API_KEY', ''))

# Store active conversations (in production, use Redis or database)
active_conversations = {}

@tavus_bp.route('/test', methods=['GET'])
def test_tavus_connection():
    """Test Tavus API connection."""
    try:
        if not tavus_agent.api_key:
            return jsonify({
                'error': 'Tavus API key not configured',
                'api_key_present': False
            }), 500
        
        # Try to get replicas to test the connection
        replicas = tavus_agent.get_replicas()
        
        return jsonify({
            'success': True,
            'api_key_present': bool(tavus_agent.api_key),
            'api_key_length': len(tavus_agent.api_key) if tavus_agent.api_key else 0,
            'replicas_response': replicas is not None,
            'status': 'Tavus API connection test completed'
        })
        
    except Exception as e:
        logger.error(f"Error testing Tavus connection: {e}")
        return jsonify({'error': f'Test failed: {str(e)}'}), 500

@tavus_bp.route('/create-agent', methods=['POST'])
def create_ai_agent():
    """Create an AI agent for a room."""
    try:
        data = request.get_json()
        room_id = data.get('room_id')
        
        if not room_id:
            return jsonify({'error': 'Room ID is required'}), 400
        
        if not tavus_agent.api_key:
            return jsonify({'error': 'Tavus API key not configured'}), 500
        
        logger.info(f"Creating AI agent for room: {room_id}")
        
        # First, try to get existing replicas
        replicas = tavus_agent.get_replicas()
        
        if replicas and replicas.get('data'):
            # Use the first available replica
            replica_id = replicas['data'][0]['replica_id']
            logger.info(f"Using existing replica: {replica_id}")
        else:
            # Create a new replica
            replica = tavus_agent.create_replica("SpurHacks AI Assistant")
            if not replica:
                return jsonify({'error': 'Failed to create AI replica'}), 500
            replica_id = replica.get('replica_id')
        
        # Create a video conversation
        video_response = tavus_agent.create_video_conversation(replica_id, room_id)
        if not video_response:
            return jsonify({'error': 'Failed to create AI video conversation'}), 500
        
        # Store conversation info
        active_conversations[room_id] = {
            'video_id': video_response.get('video_id'),
            'replica_id': replica_id,
            'status': 'active',
            'video_url': video_response.get('download_url') or video_response.get('hosted_url')
        }
        
        return jsonify({
            'success': True,
            'video_id': video_response.get('video_id'),
            'agent_video_url': video_response.get('download_url') or video_response.get('hosted_url'),
            'status': 'AI agent created successfully'
        })
        
    except Exception as e:
        logger.error(f"Error creating AI agent: {e}")
        return jsonify({'error': f'Internal server error: {str(e)}'}), 500

@tavus_bp.route('/send-message', methods=['POST'])
def send_message_to_agent():
    """Send a message to the AI agent."""
    try:
        data = request.get_json()
        room_id = data.get('room_id')
        message = data.get('message')
        
        if not room_id or not message:
            return jsonify({'error': 'Room ID and message are required'}), 400
        
        conversation_info = active_conversations.get(room_id)
        if not conversation_info:
            return jsonify({'error': 'No active AI agent in this room'}), 404
        
        # Send message to Tavus (simplified - just log for now)
        response = tavus_agent.send_message(conversation_info['video_id'], message)
        if not response:
            return jsonify({'error': 'Failed to send message to AI agent'}), 500
        
        return jsonify({
            'success': True,
            'response': response,
            'ai_response': f"AI received your message: '{message}'. I'm processing your request!",
            'status': 'Message sent to AI agent'
        })
        
    except Exception as e:
        logger.error(f"Error sending message to AI agent: {e}")
        return jsonify({'error': 'Internal server error'}), 500

@tavus_bp.route('/end-agent', methods=['POST'])
def end_ai_agent():
    """End the AI agent session."""
    try:
        data = request.get_json()
        room_id = data.get('room_id')
        
        if not room_id:
            return jsonify({'error': 'Room ID is required'}), 400
        
        conversation_info = active_conversations.get(room_id)
        if not conversation_info:
            return jsonify({'error': 'No active AI agent in this room'}), 404
        
        # End conversation
        success = tavus_agent.end_conversation(conversation_info['conversation_id'])
        if success:
            del active_conversations[room_id]
            return jsonify({
                'success': True,
                'status': 'AI agent ended successfully'
            })
        else:
            return jsonify({'error': 'Failed to end AI agent'}), 500
        
    except Exception as e:
        logger.error(f"Error ending AI agent: {e}")
        return jsonify({'error': 'Internal server error'}), 500

@tavus_bp.route('/callback', methods=['POST'])
def tavus_callback():
    """Handle callbacks from Tavus."""
    try:
        data = request.get_json()
        logger.info(f"Tavus callback: {data}")
        
        # Handle different callback types
        event_type = data.get('event_type')
        conversation_id = data.get('conversation_id')
        
        if event_type == 'conversation_ended':
            # Find and remove the conversation from active list
            for room_id, conv_info in list(active_conversations.items()):
                if conv_info['conversation_id'] == conversation_id:
                    del active_conversations[room_id]
                    break
        
        return jsonify({'status': 'callback received'}), 200
        
    except Exception as e:
        logger.error(f"Error handling Tavus callback: {e}")
        return jsonify({'error': 'Internal server error'}), 500

@tavus_bp.route('/status/<room_id>', methods=['GET'])
def get_agent_status(room_id):
    """Get the status of the AI agent in a room."""
    try:
        conversation_info = active_conversations.get(room_id)
        if not conversation_info:
            return jsonify({'active': False})
        
        # Get current status from Tavus
        status = tavus_agent.get_conversation_status(conversation_info['conversation_id'])
        
        return jsonify({
            'active': True,
            'conversation_id': conversation_info['conversation_id'],
            'tavus_status': status
        })
        
    except Exception as e:
        logger.error(f"Error getting agent status: {e}")
        return jsonify({'error': 'Internal server error'}), 500
