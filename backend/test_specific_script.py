#!/usr/bin/env python3
"""Test creating a Tavus conversation with a specific custom script to verify it works."""

import os
import sys
import logging
from dotenv import load_dotenv
from services.tavus_agent import TavusAgent

# Load environment variables
load_dotenv()

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def test_specific_custom_script():
    """Test creating a conversation with a specific custom script."""
    # Load API key
    api_key = os.getenv('TAVUS_API_KEY', '')
    if not api_key:
        print("ERROR: No TAVUS_API_KEY found in environment")
        return
    
    replica_id = os.getenv('TAVUS_REPLICA_ID', 'r1a4e22fa0d9')
    
    print(f"=== Testing Specific Custom Script ===")
    
    # Create agent
    agent = TavusAgent(api_key)
    
    # Clean up any existing conversations first
    print("\n=== Cleaning Up Existing Conversations ===")
    ended_count = agent.cleanup_active_conversations()
    print(f"Ended {ended_count} existing conversations")
    
    # Test with a very specific, unique custom script
    test_script = "Hello there! This is a test script from June 21st, 2025. I should say exactly this greeting and nothing else at the start."
    test_persona = "You are a test AI. Say the opening script exactly, then respond normally."
    test_style = "friendly"
    
    print(f"\n=== Creating Conversation with Test Script ===")
    print(f"Custom script: '{test_script}'")
    print(f"Persona: '{test_persona}'")
    print(f"Style: '{test_style}'")
    
    conversation_response = agent.create_conversation(
        replica_id=replica_id,
        persona_instructions=test_persona,
        custom_script=test_script,
        conversation_style=test_style
    )
    
    if conversation_response:
        print(f"\n✅ Test conversation created successfully!")
        print(f"Conversation ID: {conversation_response.get('conversation_id')}")
        print(f"Conversation URL: {conversation_response.get('conversation_url')}")
        
        print(f"\n🎯 EXPECTED RESULT:")
        print(f"   When you join this conversation, the AI should say:")
        print(f"   '{test_script}'")
        print(f"\n📋 TEST URL: {conversation_response.get('conversation_url')}")
        
        return conversation_response
    else:
        print("❌ Failed to create test conversation")
        return None

if __name__ == "__main__":
    test_specific_custom_script()
