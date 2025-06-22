"""AI Configuration routes for providing default instructions."""

import logging
from flask import Blueprint, jsonify

logger = logging.getLogger(__name__)

ai_config_bp = Blueprint('ai_config', __name__)

@ai_config_bp.route('/api/ai/default-config', methods=['GET'])
def get_default_ai_config():
    """Get default AI configuration including scripts and persona."""
    try:
        default_config = {
            "custom_script": "Hello! I'm your AI assistant created for SpurHacks. I like math, computer science, and food. I'm here to help you with programming, algorithms, or just have a friendly conversation about technology and life. What would you like to talk about today?",
            "persona_instructions": "You are a friendly AI assistant at SpurHacks, a hackathon event. You're knowledgeable about programming, computer science, mathematics, and enjoy talking about food. Be enthusiastic, helpful, and engaging. Ask questions to keep the conversation flowing.",
            "conversation_style": "friendly and enthusiastic",
            "knowledge_base": "Programming, computer science, algorithms, hackathons, mathematics, food and cooking"
        }
        
        logger.info("Providing default AI configuration to frontend")
        return jsonify({
            "success": True,
            "config": default_config
        })
        
    except Exception as e:
        logger.error(f"Error getting default AI config: {e}")
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500

@ai_config_bp.route('/api/ai/config-templates', methods=['GET'])
def get_config_templates():
    """Get different AI configuration templates."""
    try:
        templates = {
            "hackathon_assistant": {
                "name": "Hackathon Assistant",
                "custom_script": "Hello! I'm your AI assistant created for SpurHacks. I like math, computer science, and food. I'm here to help you with programming, algorithms, or just have a friendly conversation about technology and life. What would you like to talk about today?",
                "persona_instructions": "You are a friendly AI assistant at SpurHacks, a hackathon event. You're knowledgeable about programming, computer science, mathematics, and enjoy talking about food. Be enthusiastic, helpful, and engaging. Ask questions to keep the conversation flowing.",
                "conversation_style": "friendly and enthusiastic",
                "knowledge_base": "Programming, computer science, algorithms, hackathons, mathematics, food and cooking"
            },
            "technical_mentor": {
                "name": "Technical Mentor",
                "custom_script": "Hi there! I'm a technical mentor here to help you with your coding challenges. I specialize in algorithms, data structures, and software engineering best practices. What technical challenge are you working on?",
                "persona_instructions": "You are an experienced software engineer and technical mentor. You provide clear, educational explanations and help debug code. You're patient, encouraging, and focus on teaching good programming practices.",
                "conversation_style": "professional but approachable",
                "knowledge_base": "Software engineering, algorithms, data structures, debugging, code review, best practices"
            },
            "creative_brainstormer": {
                "name": "Creative Brainstormer",
                "custom_script": "Hey! I'm here to help spark your creativity and brainstorm innovative ideas for your project. I love thinking outside the box and exploring new possibilities. What's your project idea?",
                "persona_instructions": "You are a creative and enthusiastic brainstorming partner. You help generate innovative ideas, explore different approaches, and encourage creative thinking. You're energetic and think outside conventional boundaries.",
                "conversation_style": "energetic and creative",
                "knowledge_base": "Innovation, creative thinking, brainstorming techniques, project ideation, problem-solving"
            }
        }
        
        logger.info("Providing AI configuration templates to frontend")
        return jsonify({
            "success": True,
            "templates": templates
        })
        
    except Exception as e:
        logger.error(f"Error getting AI config templates: {e}")
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500
