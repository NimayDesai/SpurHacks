#!/usr/bin/env python3

"""
Test script changes - create multiple conversations with different scripts
to verify that each AI agent uses its specific script.
"""

import sys
import os
import time

# Add the backend directory to the Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from services.tavus_agent import TavusAgent
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def test_script_changes():
    """Test creating conversations with different scripts"""
    print("=== Testing Script Changes ===")
    
    api_key = os.getenv('TAVUS_API_KEY')
    if not api_key:
        print("❌ ERROR: TAVUS_API_KEY not found in environment")
        return
        
    tavus = TavusAgent(api_key)
    
    # Clean up existing conversations first
    print("\n=== Cleaning Up Existing Conversations ===")
    try:
        conversations = tavus.list_conversations()
        for conv in conversations.get('data', []):
            if conv['status'] == 'active':
                print(f"Ending conversation {conv['conversation_id']}")
                tavus.end_conversation(conv['conversation_id'])
        print("Cleanup complete\n")
    except Exception as e:
        print(f"Cleanup error: {e}\n")
    
    # Test different scripts
    test_scripts = [
        {
            "script": "Script #1: Welcome to our sales demo! I'm here to show you our product.",
            "persona": "You are a sales representative. Use the exact opening script.",
            "style": "professional"
        },
        {
            "script": "Script #2: Hi there! I'm your personal tutor. Let's start learning together!",
            "persona": "You are an educational tutor. Say the opening exactly as given.",
            "style": "friendly"
        },
        {
            "script": "Script #3: Greetings! I am a technical support specialist ready to help.",
            "persona": "You are tech support. Use the exact greeting provided.",
            "style": "helpful"
        }
    ]
    
    conversations = []
    
    for i, test in enumerate(test_scripts, 1):
        print(f"=== Creating Conversation {i} ===")
        print(f"Script: '{test['script']}'")
        print(f"Persona: '{test['persona']}'")
        print(f"Style: '{test['style']}'")
        
        try:
            conversation_data = tavus.create_conversation(
                persona_instructions=test['persona'],
                custom_script=test['script'],
                conversation_style=test['style']
            )
            
            conversation_id = conversation_data['conversation_id']
            conversation_url = conversation_data['conversation_url']
            
            conversations.append({
                'id': conversation_id,
                'url': conversation_url,
                'script': test['script'],
                'number': i
            })
            
            print(f"✅ Created: {conversation_id}")
            print(f"URL: {conversation_url}")
            print()
            
            # Small delay between creations
            time.sleep(1)
            
        except Exception as e:
            print(f"❌ Failed to create conversation {i}: {e}")
            print()
    
    # Summary
    print("=== TEST SUMMARY ===")
    print(f"Created {len(conversations)} conversations with different scripts:")
    print()
    
    for conv in conversations:
        print(f"🎯 Conversation {conv['number']}:")
        print(f"   ID: {conv['id']}")
        print(f"   URL: {conv['url']}")
        print(f"   Expected Opening: '{conv['script']}'")
        print()
    
    print("📋 TESTING INSTRUCTIONS:")
    print("1. Join each conversation URL in a separate browser tab")
    print("2. Listen to each AI's opening greeting")
    print("3. Verify each AI says its specific script exactly")
    print("4. This confirms that script changes work properly!")
    
    return conversations

if __name__ == "__main__":
    conversations = test_script_changes()
    
    if conversations:
        print(f"\n🎉 Successfully created {len(conversations)} test conversations!")
        print("Each should use its specific script when you join.")
    else:
        print(f"\n💥 Failed to create test conversations.")
