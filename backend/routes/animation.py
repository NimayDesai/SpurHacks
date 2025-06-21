"""Animation routes for the application."""

import os
import uuid
import subprocess
from flask import Blueprint, request, jsonify, send_file
from flask_jwt_extended import jwt_required

# Create a blueprint for animation routes
animation_bp = Blueprint('animation', __name__, url_prefix='/api/animation')

@animation_bp.route('/render', methods=['POST'])
@jwt_required()
def render_animation():
    """Render a Manim animation based on the specified type."""
    data = request.get_json()
    
    if not data or 'animation_type' not in data:
        return jsonify({'error': 'Animation type is required'}), 400
    
    animation_type = data['animation_type']
    
    # Map animation type to scene class
    animation_map = {
        'circle': 'CreateCircle',
        'square_to_circle': 'SquareToCircle',
        'text': 'WriteText',
        'math': 'MathExample'
    }
    
    if animation_type not in animation_map:
        return jsonify({'error': 'Invalid animation type'}), 400
    
    scene_class = animation_map[animation_type]
    output_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'static', 'animations')
    os.makedirs(output_dir, exist_ok=True)
    
    unique_id = str(uuid.uuid4())
    
    try:
        # Run manim command to generate animation
        # Note: This assumes 'manim' is installed and available in PATH
        # In production, you might need to use the full path to the manim executable
        result = subprocess.run(
            ['manim', '-ql', os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'manim_examples.py'), 
             scene_class, f'--output_file={unique_id}', f'--media_dir={output_dir}'],
            check=True,
            capture_output=True,
            text=True
        )
        
        # Find the generated file
        for file in os.listdir(output_dir):
            if file.endswith('.mp4') and unique_id in file:
                return jsonify({
                    'animation_url': f'/api/animation/file/{file}',
                    'message': 'Animation rendered successfully'
                }), 200
        
        return jsonify({
            'error': 'Failed to locate generated animation',
            'logs': result.stdout
        }), 500
        
    except subprocess.CalledProcessError as e:
        return jsonify({
            'error': 'Animation rendering failed',
            'message': str(e),
            'stdout': e.stdout,
            'stderr': e.stderr
        }), 500
    except Exception as e:
        return jsonify({
            'error': 'Server error while rendering animation',
            'message': str(e)
        }), 500

@animation_bp.route('/file/<path:filename>')
def serve_animation(filename):
    """Serve a generated animation file."""
    animations_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'static', 'animations')
    return send_file(os.path.join(animations_dir, filename))
