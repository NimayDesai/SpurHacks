"""Tavus AI Agent Service for video calls."""

import os
import requests
import logging
from typing import Optional, Dict, Any

logger = logging.getLogger(__name__)

class TavusAgent:
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.base_url = "https://tavusapi.com"
        self.headers = {
            "x-api-key": api_key,  # Tavus uses x-api-key header
            "Content-Type": "application/json"
        }
    
    def create_conversation(self, replica_id: str = "r1a4e22fa0d9", persona_instructions: str = "Read the script at the start", custom_script: str = "Hi. Hawk tuah. skibidi bop bop bop yes yes.", conversation_style: str = "friendly") -> Optional[Dict[str, Any]]:
        """Create a conversational video with your specific replica and custom instructions."""
        try:
            # Build comprehensive conversational context
            conversational_context = self._build_conversational_context(persona_instructions, custom_script, conversation_style)
            
            # Use the conversation endpoint for real-time interaction
            data = {
                "replica_id": replica_id,
                "conversation_name": "SpurHacks Video Call"
            }
            
            # Use the proper Tavus API fields
            if conversational_context:
                data["conversational_context"] = conversational_context
                logger.info(f"Using conversational context: {conversational_context}")
            
            # This is the key field - custom_greeting is what the AI says when someone joins
            if custom_script:
                data["custom_greeting"] = custom_script
                logger.info(f"Using custom_greeting (opening script): {custom_script}")
            else:
                data["custom_greeting"] = "Hi. Hawk tuah. skibidi bop bop bop yes yes."
                logger.info("Using default custom_greeting: Hi. Hawk tuah. skibidi bop bop bop yes yes.")
            
            # Add callback URL if available
            base_url = os.getenv('BASE_URL', 'http://10.200.6.212:5002')
            if base_url:
                data["callback_url"] = f"{base_url}/api/tavus/callback"
            
            logger.info(f"Creating conversation with data: {data}")
            
            response = requests.post(
                f"{self.base_url}/v2/conversations",
                headers=self.headers,
                json=data,
                timeout=30
            )
            
            logger.info(f"Tavus conversation creation response: {response.status_code} - {response.text}")
            
            if response.status_code in [200, 201]:
                return response.json()
            else:
                logger.error(f"Tavus conversation API error: {response.status_code} - {response.text}")
                return None
            
        except requests.exceptions.RequestException as e:
            logger.error(f"Error creating Tavus conversation: {e}")
            return None
    
    def _build_conversational_context(self, persona_instructions: str, custom_script: str, conversation_style: str) -> str:
        """Build a comprehensive conversational context for the AI."""
        context_parts = []
        
        # Add persona instructions first - this is the core identity
        if persona_instructions:
            context_parts.append(f"PERSONA: {persona_instructions}")
        
        # Add conversation style
        if conversation_style and conversation_style != "friendly":
            context_parts.append(f"STYLE: Be {conversation_style} in your responses.")
        
        # Note: The opening greeting is now handled by custom_greeting field
        # This context is for ongoing conversation behavior
        if custom_script:
            context_parts.append(f"CONVERSATION_GUIDANCE: After your initial greeting, continue the conversation naturally based on the user's responses.")
        
        if context_parts:
            full_context = " | ".join(context_parts)
            logger.info(f"Built conversational context: {full_context}")
            return full_context
        
        return ""
    
    def get_conversation_url(self, conversation_id: str) -> Optional[str]:
        """Get the conversation URL for iframe embedding."""
        try:
            # Get conversation details
            response = requests.get(
                f"{self.base_url}/v2/conversations/{conversation_id}",
                headers=self.headers,
                timeout=30
            )
            
            logger.info(f"Tavus conversation details response: {response.status_code}")
            
            if response.status_code == 200:
                data = response.json()
                # Return the conversation URL for iframe embedding
                return data.get('conversation_url') or f"https://tavus.io/conversations/{conversation_id}"
            else:
                logger.error(f"Tavus conversation details API error: {response.status_code} - {response.text}")
                return None
            
        except requests.exceptions.RequestException as e:
            logger.error(f"Error getting conversation URL: {e}")
            return None
    
    def test_replica(self, replica_id: str = "r1a4e22fa0d9") -> Optional[Dict[str, Any]]:
        """Test if the specific replica is available and working."""
        try:
            response = requests.get(
                f"{self.base_url}/v2/replicas/{replica_id}",
                headers=self.headers,
                timeout=30
            )
            
            logger.info(f"Tavus replica test response: {response.status_code} - {response.text}")
            
            if response.status_code == 200:
                return response.json()
            else:
                logger.error(f"Tavus replica test error: {response.status_code} - {response.text}")
                return None
            
        except requests.exceptions.RequestException as e:
            logger.error(f"Error testing replica: {e}")
            return None
    
    def get_replicas(self) -> Optional[Dict[str, Any]]:
        """Get available replicas."""
        try:
            response = requests.get(
                f"{self.base_url}/v2/replicas",
                headers=self.headers,
                timeout=30
            )
            
            logger.info(f"Tavus replicas response: {response.status_code} - {response.text}")
            
            if response.status_code == 200:
                return response.json()
            else:
                logger.error(f"Tavus replicas API error: {response.status_code} - {response.text}")
                return None
            
        except requests.exceptions.RequestException as e:
            logger.error(f"Error getting replicas: {e}")
            return None
    def send_message(self, conversation_id: str, message: str) -> Optional[Dict[str, Any]]:
        """Note: Tavus doesn't support direct message injection. This is for compatibility."""
        logger.info(f"Note: Message '{message}' would be sent to conversation {conversation_id}, but Tavus handles conversation through their interface.")
        
        # Return a mock success response for compatibility
        return {
            "success": True,
            "message": "Message noted (Tavus handles conversation through video interface)",
            "conversation_id": conversation_id,
            "note": "Real conversation happens in the Tavus video interface"
        }
    
    def get_active_conversations(self) -> Optional[Dict[str, Any]]:
        """Get all active conversations."""
        try:
            response = requests.get(
                f"{self.base_url}/v2/conversations",
                headers=self.headers,
                timeout=30
            )
            
            logger.info(f"Tavus conversations response: {response.status_code}")
            
            if response.status_code == 200:
                return response.json()
            else:
                logger.error(f"Tavus conversations API error: {response.status_code} - {response.text}")
                return None
            
        except requests.exceptions.RequestException as e:
            logger.error(f"Error getting conversations: {e}")
            return None
    
    def end_conversation(self, conversation_id: str) -> bool:
        """End an active conversation."""
        try:
            response = requests.delete(
                f"{self.base_url}/v2/conversations/{conversation_id}",
                headers=self.headers,
                timeout=30
            )
            
            logger.info(f"Tavus end conversation response: {response.status_code} - {response.text}")
            
            if response.status_code in [200, 204]:
                return True
            else:
                logger.error(f"Tavus end conversation API error: {response.status_code} - {response.text}")
                return False
            
        except requests.exceptions.RequestException as e:
            logger.error(f"Error ending conversation: {e}")
            return False
    
    def cleanup_active_conversations(self) -> int:
        """End all active conversations to free up slots."""
        try:
            conversations_data = self.get_active_conversations()
            if not conversations_data:
                return 0
            
            conversations = conversations_data.get('data', [])
            ended_count = 0
            
            for conv in conversations:
                if isinstance(conv, dict):
                    status = conv.get('status', '')
                    conv_id = conv.get('conversation_id', '')
                    
                    if status in ['active', 'processing', 'connecting', 'in_progress'] and conv_id:
                        logger.info(f"Ending conversation {conv_id} with status {status}")
                        if self.end_conversation(conv_id):
                            ended_count += 1
                        
            return ended_count
            
        except Exception as e:
            logger.error(f"Error cleaning up conversations: {e}")
            return 0

    def get_video_status(self, video_id: str) -> Optional[Dict[str, Any]]:
        """Get the status of a video."""
        try:
            response = requests.get(
                f"{self.base_url}/v2/videos/{video_id}",
                headers=self.headers,
                timeout=30
            )
            
            logger.info(f"Tavus video status response: {response.status_code} - {response.text}")
            
            if response.status_code == 200:
                return response.json()
            else:
                logger.error(f"Tavus video status API error: {response.status_code} - {response.text}")
                return None
            
        except requests.exceptions.RequestException as e:
            logger.error(f"Error getting video status: {e}")
            return None
