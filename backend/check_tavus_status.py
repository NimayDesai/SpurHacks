#!/usr/bin/env python3
"""Check what Tavus conversations are active and try to clean them up."""

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

def check_tavus_status():
    """Check the current status of Tavus conversations and account."""
    # Load API key
    api_key = os.getenv('TAVUS_API_KEY', '')
    if not api_key:
        print("ERROR: No TAVUS_API_KEY found in environment")
        return
    
    replica_id = os.getenv('TAVUS_REPLICA_ID', 'r1a4e22fa0d9')
    
    print(f"=== Tavus Account Status Check ===")
    
    # Create agent
    agent = TavusAgent(api_key)
    
    # Check active conversations
    print("\n=== Checking Active Conversations ===")
    conversations = agent.get_active_conversations()
    if conversations:
        print(f"Active conversations response: {conversations}")
        if 'data' in conversations:
            active_convs = conversations['data']
            print(f"Number of active conversations: {len(active_convs)}")
            for i, conv in enumerate(active_convs):
                print(f"  {i+1}. ID: {conv.get('conversation_id', 'Unknown')}")
                print(f"     Status: {conv.get('status', 'Unknown')}")
                print(f"     Created: {conv.get('created_at', 'Unknown')}")
                print(f"     URL: {conv.get('conversation_url', 'Unknown')}")
        else:
            print("No 'data' field in response")
    else:
        print("Failed to get conversations or no conversations found")
    
    # Check replica status
    print(f"\n=== Checking Replica Status ===")
    replica_info = agent.test_replica(replica_id)
    if replica_info:
        print(f"Replica info: {replica_info}")
    else:
        print("Failed to get replica info")
    
    # Try to get all replicas
    print(f"\n=== Checking All Replicas ===")
    all_replicas = agent.get_replicas()
    if all_replicas:
        print(f"All replicas: {all_replicas}")
    else:
        print("Failed to get all replicas")

if __name__ == "__main__":
    check_tavus_status()
