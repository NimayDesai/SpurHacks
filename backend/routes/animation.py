"""Animation routes for the application."""

import os
import uuid
import subprocess
from flask import Blueprint, request, jsonify, send_file
from flask_jwt_extended import jwt_required

# Create a blueprint for animation routes
animation_bp = Blueprint('animation', __name__, url_prefix='/api/animation')

@animation_bp.route('/render', methods=['POST'])
@jwt_required(optional=True)  # Make JWT optional for testing
def render_animation():
    """Render a Manim animation based on the specified type."""
    print("Animation render request received")
    
    # Check if we have a valid JWT token
    from flask_jwt_extended import get_jwt_identity
    current_user = get_jwt_identity()
    
    # Get authorization header to check what might be wrong
    auth_header = request.headers.get('Authorization')
    print(f"Authorization header: {auth_header}")
    print(f"JWT identity: {current_user}")
    
    if current_user is None:
        # Allow the request to proceed for testing, but log it
        print("WARNING: No valid JWT token provided, proceeding anyway for testing")
    
    try:
        data = request.get_json()
        print(f"Request data: {data}")
        
        if not data or 'animation_type' not in data:
            print("Missing animation_type in request")
            return jsonify({'error': 'Animation type is required'}), 400
    except Exception as e:
        print(f"Error parsing request data: {e}")
        return jsonify({'error': 'Invalid JSON data'}), 400
    animation_type = data['animation_type']
    
    # Map animation type to scene class
    animation_map = {
        'circle': 'CreateCircle',
        'square_to_circle': 'SquareToCircle',
        'text': 'WriteText',
        'math': 'MathExample',
        'custom_text': 'CustomTextAnimation',
        'custom_math': 'CustomMathAnimation'
    }
    
    if animation_type not in animation_map:
        return jsonify({'error': 'Invalid animation type'}), 400
    
    scene_class = animation_map[animation_type]
    
    # Get custom text or formula if provided
    custom_text = data.get('custom_text', '')
    custom_formula = data.get('custom_formula', '')
    
    print(f"Animation type: {animation_type}, Scene: {scene_class}")
    print(f"Custom text: {custom_text}")
    print(f"Custom formula: {custom_formula}")
    
    output_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'static', 'animations')
    os.makedirs(output_dir, exist_ok=True)
    
    unique_id = str(uuid.uuid4())
    
    try:
        # Create a unique output filename
        unique_filename = f"{animation_type}_{unique_id}.mp4"
        
        # Run manim command to generate animation
        manim_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'manim_examples.py')
        
        print(f"Running manim command for {scene_class}")
        print(f"Manim file path: {manim_file_path}")
        print(f"Output directory: {output_dir}")
        
        # Prepare environment variables for custom content
        env = os.environ.copy()
        if custom_text:
            env['MANIM_CUSTOM_TEXT'] = custom_text
        if custom_formula:
            env['MANIM_CUSTOM_FORMULA'] = custom_formula
        
        # Use manim community version syntax
        result = subprocess.run([
            'manim', 
            '-ql',  # Low quality for faster rendering
            '--output_file', unique_filename,  # Specify output filename
            '--media_dir', output_dir,  # Specify output directory
            manim_file_path,
            scene_class
        ], check=True, capture_output=True, text=True, timeout=60, env=env)
        
        print(f"Manim command completed successfully")
        print(f"Stdout: {result.stdout}")
        
        # The file should be created in output_dir/videos/manim_examples/480p15/
        video_subdir = os.path.join(output_dir, 'videos', 'manim_examples', '480p15')
        expected_file_path = os.path.join(video_subdir, unique_filename)
        
        print(f"Looking for file at: {expected_file_path}")
        
        if os.path.exists(expected_file_path):
            # Move file to the main animations directory
            final_file_path = os.path.join(output_dir, unique_filename)
            os.makedirs(os.path.dirname(final_file_path), exist_ok=True)
            
            import shutil
            shutil.move(expected_file_path, final_file_path)
            print(f"Moved file to: {final_file_path}")
            
            # Use animation_bp.url_prefix to ensure consistency with blueprint registration
            url_prefix = animation_bp.url_prefix or '/api/animation'
            
            # Remove any trailing slash from url_prefix
            if url_prefix.endswith('/'):
                url_prefix = url_prefix[:-1]
                
            # Construct the animation URL without duplicating the /api part
            if url_prefix.startswith('/api'):
                animation_url = f"{url_prefix}/file/{unique_filename}"
            else:
                animation_url = f"/api{url_prefix}/file/{unique_filename}"
            
            print(f"Animation URL: {animation_url}")
            
            return jsonify({
                'animation_url': animation_url,
                'message': 'Animation rendered successfully',
                'filename': unique_filename
            }), 200
        else:
            print(f"Expected file not found at: {expected_file_path}")
            # List what files were actually created
            if os.path.exists(video_subdir):
                files_created = os.listdir(video_subdir)
                print(f"Files in video directory: {files_created}")
                
                # Try to find any MP4 file
                for file in files_created:
                    if file.endswith('.mp4'):
                        source_path = os.path.join(video_subdir, file)
                        final_file_path = os.path.join(output_dir, f"{animation_type}_{unique_id}.mp4")
                        
                        import shutil
                        shutil.move(source_path, final_file_path)
                        print(f"Found and moved file: {file} to {final_file_path}")
                        
                        # Use animation_bp.url_prefix to ensure consistency
                        url_prefix = animation_bp.url_prefix or '/api/animation'
                        if url_prefix.endswith('/'):
                            url_prefix = url_prefix[:-1]
                            
                        if url_prefix.startswith('/api'):
                            animation_url = f"{url_prefix}/file/{animation_type}_{unique_id}.mp4"
                        else:
                            animation_url = f"/api{url_prefix}/file/{animation_type}_{unique_id}.mp4"
                        
                        return jsonify({
                            'animation_url': animation_url,
                            'message': 'Animation rendered successfully',
                            'filename': f"{animation_type}_{unique_id}.mp4"
                        }), 200
            
            return jsonify({
                'error': 'Failed to locate generated animation file',
                'expected_path': expected_file_path,
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
    file_path = os.path.join(animations_dir, filename)
    
    print(f"Attempting to serve file: {file_path}")
    if not os.path.exists(file_path):
        print(f"ERROR: File not found: {file_path}")
        # If the requested file is the mock debug animation and it doesn't exist, create it
        if filename == 'mock_debug_animation.mp4':
            try:
                print(f"Creating mock MP4 file at {file_path}")
                # Try to copy a blank video file from a template if it exists
                blank_template = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'static', 'blank.mp4')
                if os.path.exists(blank_template):
                    import shutil
                    shutil.copy(blank_template, file_path)
                    print(f"Copied blank video template to {file_path}")
                else:
                    # Create an empty file as fallback
                    with open(file_path, 'wb') as f:
                        f.write(b'')
                    print(f"Created empty file at {file_path}")
            except Exception as e:
                print(f"Error creating mock file: {str(e)}")
                return jsonify({'error': f'File not found and could not create mock: {str(e)}'}), 404
        else:
            return jsonify({'error': f'File not found: {filename}'}), 404
    
    return send_file(file_path)

@animation_bp.route('/debug', methods=['GET'])
def debug_animation_route():
    """Debug endpoint to test animation routes."""
    import sys
    import platform
    
    static_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'static', 'animations')
    os.makedirs(static_dir, exist_ok=True)
    
    # Try to detect if manim is available
    manim_available = False
    try:
        import importlib.util
        manim_spec = importlib.util.find_spec('manim')
        manim_available = manim_spec is not None
    except:
        pass
    
    # Create a test file to verify file access
    test_file_path = os.path.join(static_dir, 'test_file.txt')
    file_write_success = False
    try:
        with open(test_file_path, 'w') as f:
            f.write('Test file for animation route debugging')
        file_write_success = True
    except Exception as e:
        file_write_error = str(e)
    
    # List installed packages
    try:
        import pkg_resources
        installed_packages = [f"{d.project_name}=={d.version}" for d in pkg_resources.working_set]
    except:
        installed_packages = ["Unable to list installed packages"]
    
    return jsonify({
        'status': 'Animation debug endpoint is working',
        'python_version': sys.version,
        'platform': platform.platform(),
        'static_dir': static_dir,
        'static_dir_exists': os.path.exists(static_dir),
        'blueprint_url_prefix': animation_bp.url_prefix,
        'test_file_write_success': file_write_success,
        'test_file_path': test_file_path,
        'manim_available': manim_available,
        'installed_packages': installed_packages
    }), 200

@animation_bp.route('/render-debug', methods=['POST'])
def render_animation_debug():
    """Debug version of the render animation endpoint without JWT requirement."""
    print("DEBUG Animation render request received (no JWT required)")
    
    # Get authorization header to check what might be wrong
    auth_header = request.headers.get('Authorization')
    print(f"Authorization header: {auth_header}")
    
    try:
        data = request.get_json()
        print(f"Request data: {data}")
        
        if not data or 'animation_type' not in data:
            print("Missing animation_type in request")
            return jsonify({'error': 'Animation type is required'}), 400
        
        animation_type = data['animation_type']
        print(f"Animation type: {animation_type}")
        
        # Map animation type to scene class
        animation_map = {
            'circle': 'CreateCircle',
            'square_to_circle': 'SquareToCircle',
            'text': 'WriteText',
            'math': 'MathExample',
            'custom_text': 'CustomTextAnimation',
            'custom_math': 'CustomMathAnimation'
        }
        
        if animation_type not in animation_map:
            print(f"Invalid animation type: {animation_type}")
            return jsonify({'error': 'Invalid animation type'}), 400
        
        # Create a mock MP4 file if it doesn't exist
        static_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'static', 'animations')
        mock_file_path = os.path.join(static_dir, 'mock_debug_animation.mp4')
        
        # Check if mock file exists, if not create an empty file
        if not os.path.exists(mock_file_path):
            try:
                print(f"Creating mock MP4 file at {mock_file_path}")
                # Try to copy a blank video file from a template if it exists
                blank_template = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'static', 'blank.mp4')
                if os.path.exists(blank_template):
                    import shutil
                    shutil.copy(blank_template, mock_file_path)
                    print(f"Copied blank video template to {mock_file_path}")
                else:
                    # Create an empty file as fallback
                    with open(mock_file_path, 'wb') as f:
                        f.write(b'')
                    print(f"Created empty file at {mock_file_path}")
            except Exception as e:
                print(f"Error creating mock file: {str(e)}")
        
        # Return a mock response for testing
        # Use animation_bp.url_prefix to ensure consistency with blueprint registration
        url_prefix = animation_bp.url_prefix or '/api/animation'
        
        # Remove any trailing slash from url_prefix
        if url_prefix.endswith('/'):
            url_prefix = url_prefix[:-1]
            
        # Construct the animation URL without duplicating the /api part
        if url_prefix.startswith('/api'):
            # If already starts with /api, use the exact path
            animation_url = f"{url_prefix}/file/mock_debug_animation.mp4"
        else:
            # Otherwise prepend it
            animation_url = f"/api{url_prefix}/file/mock_debug_animation.mp4"
        
        print(f"Debug animation URL: {animation_url}")
        
        return jsonify({
            'animation_url': animation_url,
            'message': 'Debug animation endpoint working',
            'auth_header_present': auth_header is not None
        }), 200
            
    except Exception as e:
        print(f"General error in debug animation route: {str(e)}")
        return jsonify({
            'error': 'Server error in debug endpoint',
            'message': str(e)
        }), 500
