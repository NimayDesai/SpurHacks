#!/usr/bin/env python3

"""
Test script to create an actual Tavus conversation and see if credits/account issues are resolved.
"""

import sys
import os

# Add the backend directory to the Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from services.tavus_agent import TavusAgent
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def test_create_conversation():
    """Test creating an actual Tavus conversation"""
    print("=== Testing Actual Conversation Creation ===")
    
    api_key = os.getenv('TAVUS_API_KEY')
    if not api_key:
        print("❌ ERROR: TAVUS_API_KEY not found in environment")
        return None
        
    tavus = TavusAgent(api_key)
    
    # Test data matching what our frontend would send
    persona_instructions = "You are a friendly AI assistant for testing."
    custom_script = "Hello! I'm testing the new script system. This should be my exact opening line."
    conversation_style = "conversational"
    
    try:
        print(f"Attempting to create conversation with:")
        print(f"  persona_instructions: {persona_instructions}")
        print(f"  custom_script: {custom_script}")
        print(f"  conversation_style: {conversation_style}")
        print()
        
        conversation_id = tavus.create_conversation(
            persona_instructions=persona_instructions,
            custom_script=custom_script,
            conversation_style=conversation_style
        )
        
        print(f"✅ SUCCESS: Created conversation with ID: {conversation_id}")
        return conversation_id
        
    except Exception as e:
        print(f"❌ ERROR: Failed to create conversation: {e}")
        return None

if __name__ == "__main__":
    conversation_id = test_create_conversation()
    
    if conversation_id:
        print(f"\n🎉 Test passed! Conversation created: {conversation_id}")
        print("The credits/account issue appears to be resolved!")
    else:
        print(f"\n💥 Test failed! Conversation could not be created.")
        print("The credits/account issue may still be active.")
