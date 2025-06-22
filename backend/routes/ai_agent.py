"""Simple HTTP-based AI agent routes to avoid WebSocket issues."""

import logging
import os
import time
from flask import Blueprint, request, jsonify
from services.tavus_agent import TavusAgent

logger = logging.getLogger(__name__)

ai_agent_bp = Blueprint('ai_agent', __name__, url_prefix='/api/ai-agent')

@ai_agent_bp.route('/create', methods=['POST'])
def create_ai_agent():
    """Create an AI agent with custom script via HTTP API."""
    try:
        data = request.get_json()
        
        if not data:
            return jsonify({"error": "No data provided"}), 400
            
        custom_script = data.get('custom_script', '')
        room_id = data.get('room_id', 'default-room')
        
        logger.info(f"Creating Tavus AI agent for room {room_id}")
        
        # AI Configuration
        persona_instructions = "You are an AI tutor who has learned an educational script. Use the script as your knowledge base to help students understand the topic. Be helpful, patient, and engaging. If students ask about unrelated topics, kindly guide them back to the subject matter."
        conversation_style = "polite, insightful, focused, and helpful"
        
        logger.info(f"Using custom_script: '{custom_script[:100]}...'")
        
        # Initialize Tavus agent
        tavus_agent = TavusAgent(os.getenv('TAVUS_API_KEY', ''))
        
        if not tavus_agent.api_key:
            logger.error("No Tavus API key found")
            return jsonify({"error": "Tavus API key not configured"}), 500
        
        # Use your specific replica ID
        replica_id = os.getenv('TAVUS_REPLICA_ID', 'r1a4e22fa0d9')
        logger.info(f"Using replica: {replica_id}")
        
        # Test the replica first
        replica_test = tavus_agent.test_replica(replica_id)
        if not replica_test:
            logger.error(f"Replica {replica_id} is not available")
            return jsonify({"error": f"Replica {replica_id} is not ready"}), 400
        
        logger.info(f"Replica test successful: {replica_test.get('name', 'Unknown')}")
        
        # Clean up any active conversations first
        logger.info("Cleaning up active conversations...")
        ended_count = tavus_agent.cleanup_active_conversations()
        if ended_count > 0:
            logger.info(f"Ended {ended_count} active conversations")
            time.sleep(2)  # Wait for cleanup
        
        # Create a conversation with the script
        conversation_response = tavus_agent.create_conversation(
            replica_id=replica_id,
            persona_instructions=persona_instructions,
            custom_script=custom_script,
            conversation_style=conversation_style
        )
        
        if not conversation_response:
            logger.error("Failed to create Tavus conversation")
            return jsonify({"error": "Failed to create AI conversation"}), 500
        
        # Get conversation details
        conversation_id = conversation_response.get('conversation_id')
        conversation_url = tavus_agent.get_conversation_url(conversation_id)
        
        if not conversation_url:
            return jsonify({"error": "Failed to get conversation URL"}), 500
        
        logger.info(f"Conversation created successfully: {conversation_id}")
        
        # Return agent data
        agent_data = {
            'agent_id': f'tavus_agent_{room_id}',
            'conversation_id': conversation_id,
            'conversation_url': conversation_url,
            'replica_id': replica_id,
            'agent_name': replica_test.get('name', 'AI Assistant'),
            'status': 'active',
            'type': 'tavus_conversation',
            'persona_instructions': persona_instructions,
            'custom_script': custom_script,
            'conversation_style': conversation_style
        }
        
        return jsonify({
            "success": True,
            "agent_data": agent_data
        }), 200
        
    except Exception as e:
        logger.error(f"Error creating AI agent: {e}")
        return jsonify({"error": str(e)}), 500
