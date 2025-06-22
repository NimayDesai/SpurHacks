#!/usr/bin/env python3
"""Test script for quiz generation endpoint."""

import requests
import json

# Configuration
API_BASE_URL = "http://localhost:5002/api"
QUIZ_ENDPOINT = f"{API_BASE_URL}/gemini/generate-quiz"

# Sample educational script for testing
SAMPLE_SCRIPT = """
Photosynthesis is the process by which plants convert light energy into chemical energy.
This process occurs in the chloroplasts of plant cells, specifically in structures called thylakoids.

The overall equation for photosynthesis is:
6CO2 + 6H2O + light energy → C6H12O6 + 6O2

Photosynthesis consists of two main stages:

1. Light-dependent reactions (Photo stage): These occur in the thylakoids and involve the capture of light energy by chlorophyll. Water molecules are split, releasing oxygen as a byproduct, and energy is stored in molecules called ATP and NADPH.

2. Light-independent reactions (Calvin Cycle): These occur in the stroma of chloroplasts. Carbon dioxide is fixed into organic molecules using the energy from ATP and NADPH produced in the light-dependent reactions.

The significance of photosynthesis cannot be overstated - it produces the oxygen we breathe and forms the base of most food chains on Earth. Without photosynthesis, life as we know it would not exist.
"""

def test_quiz_generation():
    """Test the quiz generation endpoint."""
    print("Testing Quiz Generation Endpoint")
    print("=" * 50)

    # Prepare request data
    request_data = {
        "script": SAMPLE_SCRIPT,
        "num_questions": 3  # Request 3 questions for testing
    }

    try:
        print("Sending request to:", QUIZ_ENDPOINT)
        print("Request data length:", len(SAMPLE_SCRIPT), "characters")

        # Make the request
        response = requests.post(
            QUIZ_ENDPOINT,
            json=request_data,
            headers={"Content-Type": "application/json"},
            timeout=30
        )

        print(f"Response status code: {response.status_code}")

        if response.status_code == 200:
            data = response.json()

            if data.get("success"):
                print("✅ Quiz generated successfully!")

                quiz_data = data.get("quiz", {})
                questions = quiz_data.get("questions", [])

                print(f"Number of questions generated: {len(questions)}")
                print("\n" + "=" * 50)

                # Display each question
                for i, question in enumerate(questions, 1):
                    print(f"\nQuestion {i}:")
                    print(f"ID: {question.get('id')}")
                    print(f"Question: {question.get('question')}")
                    print("Options:")

                    options = question.get('options', {})
                    for option_key, option_text in options.items():
                        marker = "✓" if option_key == question.get('correct_answer') else " "
                        print(f"  {option_key}. {option_text} {marker}")

                    print(f"Correct Answer: {question.get('correct_answer')}")
                    print(f"Explanation: {question.get('explanation')}")
                    print("-" * 30)

            else:
                print("❌ Quiz generation failed:")
                print("Error:", data.get("error"))
                if "raw_response" in data:
                    print("Raw response:", data["raw_response"][:500])

        else:
            print(f"❌ Request failed with status code: {response.status_code}")
            print("Response:", response.text[:500])

    except requests.exceptions.ConnectionError:
        print("❌ Could not connect to the server. Make sure the backend is running on port 5002.")
    except requests.exceptions.Timeout:
        print("❌ Request timed out. The quiz generation might be taking too long.")
    except Exception as e:
        print(f"❌ Unexpected error: {str(e)}")

def test_invalid_requests():
    """Test error handling with invalid requests."""
    print("\n" + "=" * 50)
    print("Testing Error Handling")
    print("=" * 50)

    # Test 1: Empty script
    print("\nTest 1: Empty script")
    try:
        response = requests.post(
            QUIZ_ENDPOINT,
            json={"script": "", "num_questions": 3},
            headers={"Content-Type": "application/json"},
            timeout=10
        )
        print(f"Status: {response.status_code}")
        if response.status_code != 200:
            print("✅ Correctly rejected empty script")
        else:
            print("❌ Should have rejected empty script")
    except Exception as e:
        print(f"Error: {e}")

    # Test 2: Missing script
    print("\nTest 2: Missing script")
    try:
        response = requests.post(
            QUIZ_ENDPOINT,
            json={"num_questions": 3},
            headers={"Content-Type": "application/json"},
            timeout=10
        )
        print(f"Status: {response.status_code}")
        if response.status_code != 200:
            print("✅ Correctly rejected missing script")
        else:
            print("❌ Should have rejected missing script")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    test_quiz_generation()
    test_invalid_requests()
    print("\n" + "=" * 50)
    print("Testing complete!")
