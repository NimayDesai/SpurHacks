#!/bin/bash
# filepath: /Users/nimaydesai/Documents/Coding/SpurHacks/backend/auto_curl.sh

API_URL="http://localhost:5001/api/gemini/generate-manim"
OUTPUT_FILE="manim_code.py"

print_usage() {
    echo "Usage: $0 [options] [script text]"
    echo "  -f FILE    Read script from FILE instead of command line arguments"
    echo "  -o FILE    Save output to FILE (default: manim_code.py)"
    echo "  -h         Show this help message"
    echo ""
    echo "If no script is provided via arguments or -f option, the script will read from stdin."
}

# Process options
while getopts "f:o:h" opt; do
    case $opt in
        f) INPUT_FILE="$OPTARG";;
        o) OUTPUT_FILE="$OPTARG";;
        h) print_usage; exit 0;;
        \?) echo "Invalid option: -$OPTARG" >&2; print_usage; exit 1;;
    esac
done

# Remove processed options
shift $((OPTIND-1))

# Get the script content
if [ -n "$INPUT_FILE" ]; then
    # Read from file
    if [ ! -f "$INPUT_FILE" ]; then
        echo "Error: Input file '$INPUT_FILE' not found." >&2
        exit 1
    fi
    SCRIPT_CONTENT=$(cat "$INPUT_FILE")
elif [ $# -gt 0 ]; then
    # Read from command line arguments
    SCRIPT_CONTENT="$*"
else
    # Read from stdin
    echo "Enter your script (Ctrl+D when finished):"
    SCRIPT_CONTENT=$(cat)
fi

if [ -z "$SCRIPT_CONTENT" ]; then
    echo "Error: No script content provided." >&2
    print_usage
    exit 1
fi

# Use Python to properly encode JSON (more reliable than sed)
JSON_DATA=$(python3 -c "import json; print(json.dumps({'script': r'''$SCRIPT_CONTENT'''}))") 

# Send curl request
echo "Sending request to $API_URL..."
RESPONSE=$(curl -s -X POST "$API_URL" \
  -H "Content-Type: application/json" \
  -d "$JSON_DATA")

# Check if curl command succeeded
if [ $? -ne 0 ]; then
    echo "Error: Failed to connect to the API." >&2
    exit 1
fi

# Check if response contains an error
if echo "$RESPONSE" | grep -q '"error"'; then
    echo "Error: API returned an error." >&2
    echo "API Response: $RESPONSE" >&2
    exit 1
fi

# Extract the Manim code from the response using Python
MANIM_CODE=$(python3 -c "
import json, sys
try:
    response = json.loads('''$RESPONSE''')
    if 'manim_code' in response:
        print(response['manim_code'])
    elif 'error' in response:
        print(f'Error: {response[\"error\"]}', file=sys.stderr)
        exit(1)
    else:
        print('Error: Unexpected response format', file=sys.stderr)
        print(f'Response: {response}', file=sys.stderr)
        exit(1)
except json.JSONDecodeError as e:
    print(f'Error parsing JSON response: {e}', file=sys.stderr)
    print(f'Response: {'''$RESPONSE'''}', file=sys.stderr)
    exit(1)
")

if [ $? -ne 0 ]; then
    echo "Failed to extract Manim code from response."
    exit 1
fi

if [ -z "$MANIM_CODE" ]; then
    echo "Error: No Manim code returned." >&2
    echo "API Response: $RESPONSE" >&2
    exit 1
fi

# Save to file
echo "$MANIM_CODE" > "$OUTPUT_FILE"
echo "Manim code saved to $OUTPUT_FILE"

# Print summary
echo ""
echo "Success! Generated $(wc -l < "$OUTPUT_FILE") lines of Manim code."
echo "To run the animation, use: manim -pql $OUTPUT_FILE"