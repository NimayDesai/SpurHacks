#!/usr/bin/env python3

"""
End active conversations and create a new one with a specific script to test script changes.
"""

import sys
import os

# Add the backend directory to the Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from services.tavus_agent import TavusAgent
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def end_and_test():
    """End active conversations and create a new one"""
    print("=== Ending Active Conversations and Testing New Script ===")
    
    api_key = os.getenv('TAVUS_API_KEY')
    if not api_key:
        print("❌ ERROR: TAVUS_API_KEY not found in environment")
        return
        
    tavus = TavusAgent(api_key)
    
    # End the active conversation
    active_conversation_id = "c87ebf8ab61d24f9"
    print(f"Ending active conversation: {active_conversation_id}")
    
    try:
        tavus.end_conversation(active_conversation_id)
        print(f"✅ Ended conversation: {active_conversation_id}")
    except Exception as e:
        print(f"⚠️ Could not end conversation: {e}")
    
    print()
    
    # Create a new conversation with a specific script
    test_script = "FINAL TEST: Hello! This is the NEW script from our latest test. If you hear this exact message, the script changes are working perfectly!"
    test_persona = "You are a test assistant. Say the opening script exactly, then respond normally."
    test_style = "friendly"
    
    print(f"Creating new conversation with script:")
    print(f"'{test_script}'")
    print()
    
    try:
        conversation_data = tavus.create_conversation(
            persona_instructions=test_persona,
            custom_script=test_script,
            conversation_style=test_style
        )
        
        print(f"✅ SUCCESS! New conversation created:")
        print(f"   ID: {conversation_data['conversation_id']}")
        print(f"   URL: {conversation_data['conversation_url']}")
        print()
        print(f"🎯 EXPECTED GREETING:")
        print(f"   '{test_script}'")
        print()
        print(f"📋 TEST URL: {conversation_data['conversation_url']}")
        print()
        print("🔍 TO TEST:")
        print("1. Join the conversation URL above")
        print("2. Listen to the AI's opening greeting")
        print("3. Verify it says the EXACT script above")
        print("4. This confirms script changes work!")
        
        return conversation_data
        
    except Exception as e:
        print(f"❌ Failed to create new conversation: {e}")
        return None

if __name__ == "__main__":
    result = end_and_test()
    
    if result:
        print(f"\n🎉 Test ready! The AI should use the new script immediately.")
    else:
        print(f"\n💥 Test setup failed.")
