import google.generativeai as genai
import os
from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity

# Create blueprint
gemini_bp = Blueprint('gemini', __name__, url_prefix='/api/gemini')

# Configure Gemini API
GEMINI_API_KEY = os.environ.get('GEMINI_API_KEY')
if not GEMINI_API_KEY:
    raise ValueError("GEMINI_API_KEY environment variable is required")

genai.configure(api_key=GEMINI_API_KEY)

# Initialize the model
model = genai.GenerativeModel('gemini-2.5-flash')

@gemini_bp.route('/generate', methods=['POST'])
def generate_response():
    """Generate a response using Gemini API."""
    try:
        data = request.get_json()

        if not data:
            return jsonify({"error": "No data provided"}), 400

        prompt = data.get('prompt')
        instructions = data.get('instructions',
            """
               You will be given a topic.

Your task is to write a high-quality educational narration script in the style of a 3Blue1Brown video, based on that topic.

Instructions:
1. The script should be maximum 200 words in length.
2. Write it as continuous narration — the exact words that would be spoken in a video.
3. Do not include speaker labels, scene directions, formatting, emojis, or visual references of any kind.
4. The narration should flow naturally, guiding the viewer from intuition to insight.
5. Focus on clarity and conceptual understanding. You may use analogies, rhetorical questions, or simple build-up, but no lists or definitions without context.
6. Do not explain what will be shown visually — only the narration that would accompany those visuals.
7. The script should contain some time stamps to indicate pacing, but do not include any specific visual instructions.

The result should feel like the voiceover from a 3Blue1Brown video: elegant, thoughtful, and tightly focused on the concept.
"
    """)

        if not prompt:
            return jsonify({"error": "Prompt is required"}), 400

        # Combine instructions and prompt
        full_prompt = f"{instructions}\n\n{prompt}" if instructions else prompt

        # Generate response
        response = model.generate_content(full_prompt)

        return jsonify({
            "success": True,
            "response": response.text,
            "prompt": prompt,
            "instructions": instructions
        }), 200

    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500


@gemini_bp.route('/generate-manim', methods=['POST'])
def generate_manim_code():
    """Generate Manim code using Gemini API to visualize a script."""
    try:
        data = request.get_json()

        if not data:
            return jsonify({"error": "No data provided"}), 400

        script = data.get('script')
        
        if not script:
            return jsonify({"error": "Script is required"}), 400

        # These instructions are specifically for Manim code generation
        instructions = """You will be given a script.

Your task is to generate Manim (Python) code that visually represents the entire content of the script with absolute fidelity — no omissions, rewording, summarizing, or assumptions.

Strict Instructions:
1. Do not change any part of the script — not even a single word.
2. Every sentence must be represented exactly as written, either through verbatim text on screen or visual explanation, as described below.
3. If the script contains spoken or narrative content, display it using Text() or Tex() exactly as it appears.
4. If a concept, object, shape, graph, math topic, or anything visual is mentioned, you must generate a meaningful visual for it using Manim — not just show the words.
5. The output should not be a slideshow of sentences — combine accurate visuals with matching narration wherever applicable.
6. Do not infer or add any content beyond what is written. No interpretation, no expansion, no simplification.
7. You may use animations and transitions only if they help represent the script more clearly and are strictly aligned with the content.
8. The Manim code must be clean, logically structured, and well-commented to explain which parts of the code correspond to which parts of the script.
9. Ensure the code is executable in a standard Manim environment without additional dependencies or modifications.
10. The generated code should not use any external libraries or custom functions beyond standard Manim features.
11. The generated code should not use any external images, videos, or assets — everything must be created using Manim's built-in capabilities.
12. The generated code should not include any interactive elements or user inputs — it should be a straightforward animation script.
13. The text displayed should be clear, readable, and appropriately sized for viewing in a video format.
14. The script will provide time stamps for pacing, make sure to respect these in the generated code by slowing down or increasing speed of animations.
15. MAKE SURE THE CODE IS ERROR PROOF. IF NOT REGENERATE IT UNTIL IT IS.

Your Goal:
Transform the script into a faithful Manim animation — combining exact narration and visuals for every concept described. The visuals should enhance the script, not modify or reinterpret it."""

        # Combine instructions and script
        full_prompt = f"{instructions}\n\nScript:\n{script}"

        # Generate Manim code
        response = model.generate_content(full_prompt)

        return jsonify({
            "success": True,
            "manim_code": response.text,
            "script": script
        }), 200

    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500