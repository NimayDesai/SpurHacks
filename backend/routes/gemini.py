import google.generativeai as genai
import os
import re
import subprocess
import time
import hashlib
import glob
from flask import Blueprint, request, jsonify, send_file
from flask_jwt_extended import jwt_required, get_jwt_identity
from anthropic import Anthropic
from dotenv import load_dotenv

load_dotenv()

# Create blueprint
gemini_bp = Blueprint('gemini', __name__, url_prefix='/api/gemini')

# Configure Gemini API
GEMINI_API_KEY = os.environ.get('GEMINI_API_KEY')
if not GEMINI_API_KEY:
    raise ValueError("GEMINI_API_KEY environment variable is required")

# Configure Anthropic API for Claude
CLAUDE_API_KEY = os.environ.get('ANTHROPIC_API_KEY')
if not CLAUDE_API_KEY:
    raise ValueError("ANTHROPIC_API_KEY environment variable is required")

genai.configure(api_key=GEMINI_API_KEY)
anthropic_client = Anthropic(api_key=CLAUDE_API_KEY)

# Initialize the model
model = genai.GenerativeModel('gemini-1.5-flash')

def extract_code_from_claude_response(response_text):
    """Extract Python code from Claude's response, which might contain markdown code blocks."""
    # Look for Python code blocks in markdown format (```python ... ```)
    code_blocks = re.findall(r'```python\n(.*?)\n```', response_text, re.DOTALL)
    
    if code_blocks:
        # Return the first complete Python code block
        return code_blocks[0]
    
    # If no code blocks found but there are triple backticks, try to extract anything between them
    code_blocks = re.findall(r'```\n(.*?)\n```', response_text, re.DOTALL)
    if code_blocks:
        return code_blocks[0]
    
    # If no code blocks found, try to find any code that looks like Python
    if 'from manim import' in response_text or 'import manim' in response_text:
        lines = response_text.split('\n')
        start_idx = None
        for i, line in enumerate(lines):
            if 'from manim import' in line or 'import manim' in line:
                start_idx = i
                break
        
        if start_idx is not None:
            # Return from first import to the end
            return '\n'.join(lines[start_idx:])
    
    # If everything else fails, return the whole response
    return response_text

@gemini_bp.route('/video/<path:video_path>')
def serve_video(video_path):
    """Serve generated Manim video files."""
    try:
        # Get the full path to the video file
        manim_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'manim_gens')
        full_video_path = os.path.join(manim_dir, video_path)
        
        # Check if file exists
        if not os.path.exists(full_video_path):
            return jsonify({"error": "Video file not found"}), 404
        
        # Serve the video file
        return send_file(full_video_path, mimetype='video/mp4')
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500

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
1. The script should be maximum 60-80 words in length (30-40 seconds).
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
    """Generate Manim code using Claude 4 Sonnet API to visualize a script."""
    try:
        data = request.get_json()

        if not data:
            return jsonify({"error": "No data provided"}), 400

        script = data.get('script')
        
        if not script:
            return jsonify({"error": "Script is required"}), 400

        # These instructions are specifically for Manim code generation
        instructions = """
You'll receive a complete script. Your job is to generate fully functional Manim (Python) code that mirrors every line of that script—verbatim—using on-screen text and visuals. Follow these rules exactly:

1. **Exact text only.** Every word of the script that appears on screen must match character for character. No paraphrasing or editing.
2. **Visualize only what's described.** Whenever the script mentions a shape, graph, mathematical object, or concept, show a matching Manim primitive (e.g., `Circle()`, `Line()`, `NumberPlane()`); if it doesn't, simply display the script text with `Text()` or `Tex()`.
3. **No added assumptions.** If something is ambiguous or unspecified, skip inventing visuals—just render the original text.
4. **Well-structured, runnable code.** Provide a single Python file with all imports (`from manim import *`), a Scene subclass, and clear comments tying each code block to its script lines. It must run without errors in a standard ManimCE setup.
5. **Timing and layout.** Honor any timestamps with `wait()`, keep text legible for a 16:9 video, and space objects to avoid overlap.
6. **No extras.** Do not include commentary, reasoning, or any content not explicitly in the script.
7. Make sure that all text and graphics are completely visible in the video area.
8. Add visuals wherever possible to illustrate the concepts in the script, but do not add any extra content that is not in the script. Make sure these visuals are appropriately positioned and sized for clarity.
9. **Precise timing control:** When timestamps appear in the script (like "[0:08]"), implement precise scene transitions. At each timestamp:
   a. Clear previous elements with appropriate FadeOut animations
   b. Introduce new content with suitable animations (Write, FadeIn, etc.)
   c. Use wait() calls to maintain exact timing between timestamps
   d. Ensure smooth transitions between sections while strictly adhering to the timestamp progression
   e. For mathematical concepts introduced at specific timestamps, time their appearance to match exactly when mentioned
10. The video should be finished when the final timestamp is reached, with all elements cleared.
Your output should be a complete, clean, executable Manim script that faithfully and exactly represents the input, with just enough visuals to illustrate what the script names.

****** IMPORTANT *******
# instead of
curve = plane.get_graph(curve_func, t_range=[-4.5, 4.5], color=YELLOW, stroke_width=4)

# do this:
curve = plane.plot(
    curve_func,
    x_range=[-4.5, 4.5],
    color=YELLOW,
    stroke_width=4
)

IMPORTANT: Provide ONLY the complete Python code with no explanations, comments outside the code, or markdown formatting. Just the raw Python code that can be directly saved to a file and executed.
"""

        # Combine instructions and script for Claude
        full_prompt = f"{instructions}\n\nScript:\n{script}"

        # Generate Manim code using Claude 4 Sonnet
        response = anthropic_client.messages.create(
            model="claude-sonnet-4-20250514",
            max_tokens=4000,
            system="You are an expert in creating Manim animations from scripts. Provide only clean, executable Python code with no surrounding explanations or markdown.",
            messages=[
                {"role": "user", "content": full_prompt}
            ]
        )
        
        # Extract the text from Claude's response
        response_text = response.content[0].text
        
        # Extract code from Claude's response
        manim_code = extract_code_from_claude_response(response_text)
        
        # Create manim_gens directory if it doesn't exist
        manim_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'manim_gens')
        if not os.path.exists(manim_dir):
            os.makedirs(manim_dir)
        
        # Create a unique filename using timestamp and a short hash of the script
        import hashlib
        import time
        
        timestamp = time.strftime("%Y%m%d_%H%M%S")
        script_hash = hashlib.md5(script.encode()).hexdigest()[:8]
        filename = f"manim_script_{timestamp}_{script_hash}.py"
        filepath = os.path.join(manim_dir, filename)
        
        # Write code to file
        with open(filepath, 'w') as f:
            f.write(manim_code)
        
        # Get the scene class name from the code
        scene_class = None
        for line in manim_code.split('\n'):
            if line.startswith('class ') and '(Scene)' in line:
                scene_class = line.split('class ')[1].split('(')[0].strip()
                break
        
        run_command = f"manim -pql {filepath}" + (f" {scene_class}" if scene_class else "")

        return jsonify({
            "success": True,
            "manim_code": manim_code,
            "file_path": filepath,
            "scene_class": scene_class,
            "run_command": run_command
        }), 200

    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500


@gemini_bp.route('/generate-presentation', methods=['POST'])
def generate_presentation():
    """Generate a complete presentation: script, Manim video, and Tavus AI data."""
    try:
        print("=== generate_presentation endpoint called ===")
        print(f"Request method: {request.method}")
        print(f"Request headers: {dict(request.headers)}")
        print(f"Request content type: {request.content_type}")
        
        data = request.get_json()
        print(f"Request data: {data}")

        if not data:
            print("ERROR: No data provided")
            return jsonify({"error": "No data provided"}), 400

        prompt = data.get('prompt')
        print(f"Extracted prompt: '{prompt}'")
        if not prompt:
            print("ERROR: Prompt is required")
            return jsonify({"error": "Prompt is required"}), 400

        print(f"Starting processing for prompt: '{prompt}'")
    except Exception as e:
        print(f"EARLY ERROR in generate_presentation: {str(e)}")
        print(f"Error type: {type(e)}")
        import traceback
        traceback.print_exc()
        return jsonify({
            "success": False,
            "error": f"Early processing error: {str(e)}"
        }), 500
        
    try:

        # Step 1: Generate educational script using Gemini
        script_instructions = """
You will be given a topic.

Your task is to write a high-quality educational narration script in the style of a 3Blue1Brown video, based on that topic.

Instructions:
1. The script should be maximum 60-80 words in length (30-40 seconds).
2. Write it as continuous narration — the exact words that would be spoken in a video.
3. Do not include speaker labels, scene directions, formatting, emojis, or visual references of any kind.
4. The narration should flow naturally, guiding the viewer from intuition to insight.
5. Focus on clarity and conceptual understanding. You may use analogies, rhetorical questions, or simple build-up, but no lists or definitions without context.
6. Do not explain what will be shown visually — only the narration that would accompany those visuals.
7. The script should contain some time stamps to indicate pacing, but do not include any specific visual instructions.

The result should feel like the voiceover from a 3Blue1Brown video: elegant, thoughtful, and tightly focused on the concept.
"""
        
        script_prompt = f"{script_instructions}\n\n{prompt}"
        script_response = model.generate_content(script_prompt)
        generated_script = script_response.text

        # Step 2: Generate Manim code using Claude
        manim_instructions = """
IMPORTANT: Do NOT use MathTex or any LaTeX-based objects; use only Text() for all on-screen content to avoid LaTeX compilation issues.
You'll receive a complete script. Your job is to generate fully functional Manim (Python) code that mirrors every line of that script—verbatim—using on-screen text and visuals. Follow these rules exactly:

1. **Exact text only.** Every word of the script that appears on screen must match character for character. No paraphrasing or editing.
2. **Visualize only what's described.** Whenever the script mentions a shape, graph, mathematical object, or concept, show a matching Manim primitive (e.g., `Circle()`, `Line()`, `NumberPlane()`); if it doesn't, simply display the script text with `Text()` or `Tex()`.
3. **No added assumptions.** If something is ambiguous or unspecified, skip inventing visuals—just render the original text.
4. **Well-structured, runnable code.** Provide a single Python file with all imports (`from manim import *`), a Scene subclass, and clear comments tying each code block to its script lines. It must run without errors in a standard ManimCE setup.
5. **Timing and layout.** Honor any timestamps with `wait()`, keep text legible for a 16:9 video, and space objects to avoid overlap.
6. **No extras.** Do not include commentary, reasoning, or any content not explicitly in the script.
7. Make sure that all text and graphics are completely visible in the video area.
8. Add visuals wherever possible to illustrate the concepts in the script, but do not add any extra content that is not in the script. Make sure these visuals are appropriately positioned and sized for clarity.
9. **Precise timing control:** When timestamps appear in the script (like "[0:08]"), implement precise scene transitions. At each timestamp:
   a. Clear previous elements with appropriate FadeOut animations
   b. Introduce new content with suitable animations (Write, FadeIn, etc.)
   c. Use wait() calls to maintain exact timing between timestamps
   d. Ensure smooth transitions between sections while strictly adhering to the timestamp progression
   e. For mathematical concepts introduced at specific timestamps, time their appearance to match exactly when mentioned
10. The video should be finished when the final timestamp is reached, with all elements cleared.
11. **Use only valid Manim colors:** Use only these colors: WHITE, BLACK, RED, GREEN, BLUE, YELLOW, PURPLE, PINK, ORANGE, GRAY, LIGHT_GRAY, DARK_GRAY, BLUE_A, BLUE_B, BLUE_C, BLUE_D, BLUE_E, GREEN_A, GREEN_B, GREEN_C, GREEN_D, GREEN_E, RED_A, RED_B, RED_C, RED_D, RED_E, YELLOW_A, YELLOW_B, YELLOW_C, YELLOW_D, YELLOW_E, PURPLE_A, PURPLE_B, PURPLE_C, PURPLE_D, PURPLE_E, PINK, LIGHT_PINK, DARK_BROWN, LIGHT_BROWN, GOLD. Do not use undefined colors like BROWN.

Your output should be a complete, clean, executable Manim script that faithfully and exactly represents the input, with just enough visuals to illustrate what the script names.

****** IMPORTANT *******
# instead of
curve = plane.get_graph(curve_func, t_range=[-4.5, 4.5], color=YELLOW, stroke_width=4)

# do this:
curve = plane.plot(
    curve_func,
    x_range=[-4.5, 4.5],
    color=YELLOW,
    stroke_width=4
)

IMPORTANT: Provide ONLY the complete Python code with no explanations, comments outside the code, or markdown formatting. Just the raw Python code that can be directly saved to a file and executed.
"""

        manim_prompt = f"{manim_instructions}\n\nScript:\n{generated_script}"
        
        # Generate Manim code using Claude
        claude_response = anthropic_client.messages.create(
            model="claude-sonnet-4-20250514",
            max_tokens=4000,
            system="You are an expert in creating Manim animations from scripts. Provide only clean, executable Python code with no surrounding explanations or markdown.",
            messages=[
                {"role": "user", "content": manim_prompt}
            ]
        )
        
        # Extract the text from Claude's response
        response_text = claude_response.content[0].text
        
        # Extract code from Claude's response
        manim_code = extract_code_from_claude_response(response_text)
        
        # Step 3: Create and save the Manim file
        import hashlib
        import time
        import subprocess
        import glob
        
        # Create manim_gens directory if it doesn't exist
        manim_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'manim_gens')
        if not os.path.exists(manim_dir):
            os.makedirs(manim_dir)
        
        # Create a unique filename
        timestamp = time.strftime("%Y%m%d_%H%M%S")
        script_hash = hashlib.md5(generated_script.encode()).hexdigest()[:8]
        filename = f"presentation_{timestamp}_{script_hash}.py"
        filepath = os.path.join(manim_dir, filename)
        
        # Write code to file with LaTeX configuration
        manim_code_with_config = f"""# Manim configuration for LaTeX
import os
import sys

# Add MiKTeX to PATH (adjust path as needed for your system)
if sys.platform.startswith('win'):
    os.environ['PATH'] += r';C:\\Program Files\\MiKTeX\\miktex\\bin\\x64'
elif sys.platform.startswith('darwin'):  # macOS
    os.environ['PATH'] += ':/usr/local/bin:/opt/homebrew/bin'
    
from manim import *

# Configure LaTeX template
config.tex_template = TexTemplate()
config.tex_template.add_to_preamble(r"\\usepackage{{amsmath}}")
config.tex_template.add_to_preamble(r"\\usepackage{{amssymb}}")
config.tex_template.add_to_preamble(r"\\usepackage{{mathtools}}")
config.tex_template.add_to_preamble(r"\\usepackage{{physics}}")

{manim_code}
"""
        
        with open(filepath, 'w') as f:
            f.write(manim_code_with_config)
        
        # Get the scene class name from the code
        scene_class = None
        for line in manim_code.split('\n'):
            if line.startswith('class ') and '(Scene)' in line:
                scene_class = line.split('class ')[1].split('(')[0].strip()
                break
        
        if not scene_class:
            return jsonify({
                "success": False,
                "error": "Could not find scene class in generated Manim code"
            }), 400
        
        # Step 4: Run Manim to generate the video
        try:
            # Run manim command to generate video
            manim_command = f"manim -pql {filepath} {scene_class}"
            result = subprocess.run(
                manim_command,
                shell=True,
                cwd=manim_dir,
                capture_output=True,
                text=True,
                timeout=120  # 2 minute timeout
            )
            
            if result.returncode != 0:
                return jsonify({
                    "success": False,
                    "error": f"Manim execution failed: {result.stderr}",
                    "stdout": result.stdout
                }), 400
            
            # Find the generated video file
            video_pattern = os.path.join(manim_dir, "media", "videos", os.path.splitext(filename)[0], "480p15", "*.mp4")
            video_files = glob.glob(video_pattern)
            
            if not video_files:
                return jsonify({
                    "success": False,
                    "error": "Video file not found after Manim execution"
                }), 400
            
            video_path = video_files[0]
            # Get relative path for serving
            video_filename = os.path.basename(video_path)
            video_relative_path = f"media/videos/{os.path.splitext(filename)[0]}/480p15/{video_filename}"

            # Double video speed via ffmpeg post-processing
            fast_basename = os.path.splitext(video_filename)[0] + "_fast.mp4"
            fast_path = os.path.join(os.path.dirname(video_path), fast_basename)
            subprocess.run([
                "ffmpeg", "-y", "-i", video_path,
                "-filter:v", "setpts=0.5*PTS",
                "-filter:a", "atempo=2.3",
                fast_path
            ], check=True)
            # Update to use sped-up video
            video_filename = fast_basename
            video_relative_path = f"media/videos/{os.path.splitext(filename)[0]}/480p15/{video_filename}"
            
        except subprocess.TimeoutExpired:
            return jsonify({
                "success": False,
                "error": "Manim execution timed out"
            }), 400
        except Exception as e:
            return jsonify({
                "success": False,
                "error": f"Error running Manim: {str(e)}"
            }), 400

        # Step 5: Return everything needed for the presentation
        return jsonify({
            "success": True,
            "script": generated_script,
            "manim_code": manim_code,
            "video_path": video_relative_path,
            "video_url": f"/api/gemini/video/{video_relative_path}",
            "file_path": filepath,
            "scene_class": scene_class,
            "prompt": prompt
        }), 200

    except Exception as e:
        print(f"Error in generate_presentation: {str(e)}")
        print(f"Error type: {type(e)}")
        import traceback
        traceback.print_exc()
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500