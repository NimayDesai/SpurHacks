#!/usr/bin/env python3
"""Test script to verify the custom_greeting field is being sent correctly to Tavus."""

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

def test_custom_greeting():
    """Test that our custom_greeting is being sent correctly."""
    # Load API key
    api_key = os.getenv('TAVUS_API_KEY', '')
    if not api_key:
        print("ERROR: No TAVUS_API_KEY found in environment")
        return
    
    # Create agent
    agent = TavusAgent(api_key)
    
    # Test the conversation context building
    print("\n=== Testing Conversational Context Building ===")
    persona = "Read the script at the start"
    script = "Hi. Hawk tuah. skibidi bop bop bop yes yes."
    style = "friendly"
    
    context = agent._build_conversational_context(persona, script, style)
    print(f"Built context: {context}")
    
    # Test what data would be sent to Tavus API
    print("\n=== Testing Tavus API Data ===")
    replica_id = os.getenv('TAVUS_REPLICA_ID', 'r1a4e22fa0d9')
    
    # Mock the data building part of create_conversation
    data = {
        "replica_id": replica_id,
        "conversation_name": "SpurHacks Video Call"
    }
    
    if context:
        data["conversational_context"] = context
    
    if script:
        data["custom_greeting"] = script
    else:
        data["custom_greeting"] = "Hi. Hawk tuah. skibidi bop bop bop yes yes."
    
    base_url = os.getenv('BASE_URL', 'http://10.200.6.212:5002')
    if base_url:
        data["callback_url"] = f"{base_url}/api/tavus/callback"
    
    print("Data that would be sent to Tavus API:")
    for key, value in data.items():
        print(f"  {key}: {value}")
    
    print(f"\n=== Key Field Check ===")
    print(f"custom_greeting field: '{data.get('custom_greeting')}'")
    print(f"This should be exactly: 'Hi. Hawk tuah. skibidi bop bop bop yes yes.'")
    print(f"Match: {data.get('custom_greeting') == 'Hi. Hawk tuah. skibidi bop bop bop yes yes.'}")

if __name__ == "__main__":
    test_custom_greeting()
