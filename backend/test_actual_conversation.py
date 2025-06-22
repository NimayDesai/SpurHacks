#!/usr/bin/env python3
"""Test script to actually create a Tavus conversation and verify the custom_greeting is sent."""

import os
import sys
import logging
import json
from dotenv import load_dotenv
from services.tavus_agent import TavusAgent

# Load environment variables
load_dotenv()

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def test_actual_conversation_creation():
    """Test creating an actual conversation with the custom greeting."""
    # Load API key
    api_key = os.getenv('TAVUS_API_KEY', '')
    if not api_key:
        print("ERROR: No TAVUS_API_KEY found in environment")
        return
    
    replica_id = os.getenv('TAVUS_REPLICA_ID', 'r1a4e22fa0d9')
    
    print(f"=== Testing Actual Conversation Creation ===")
    print(f"Using replica_id: {replica_id}")
    print(f"API key: {api_key[:10]}...")
    
    # Create agent
    agent = TavusAgent(api_key)
    
    # Test replica first
    print("\n=== Testing Replica Availability ===")
    replica_test = agent.test_replica(replica_id)
    if replica_test:
        print(f"Replica test successful: {replica_test.get('name', 'Unknown')}")
    else:
        print("Replica test failed")
        return
    
    # Clean up any existing conversations
    print("\n=== Cleaning Up Existing Conversations ===")
    ended_count = agent.cleanup_active_conversations()
    print(f"Ended {ended_count} existing conversations")
    
    # Now create a new conversation with our custom greeting
    print("\n=== Creating New Conversation ===")
    print("This should use the custom_greeting field correctly...")
    
    conversation_response = agent.create_conversation(
        replica_id=replica_id,
        persona_instructions="Read the script at the start",
        custom_script="Hi. Hawk tuah. skibidi bop bop bop yes yes.",
        conversation_style="friendly"
    )
    
    if conversation_response:
        print(f"✅ Conversation created successfully!")
        print(f"Conversation ID: {conversation_response.get('conversation_id')}")
        print(f"Conversation URL: {conversation_response.get('conversation_url')}")
        print(f"Status: {conversation_response.get('status')}")
        
        # Get the conversation URL for testing
        conversation_id = conversation_response.get('conversation_id')
        conversation_url = agent.get_conversation_url(conversation_id)
        print(f"Direct conversation URL: {conversation_url}")
        
        print(f"\n🎯 TEST RESULT: If this worked correctly, when you join the conversation at the URL above,")
        print(f"   the AI should say: 'Hi. Hawk tuah. skibidi bop bop bop yes yes.' as the opening greeting.")
        
        return conversation_response
    else:
        print("❌ Failed to create conversation")
        return None

if __name__ == "__main__":
    test_actual_conversation_creation()
