# Implementing Manim in SpurHacks Project

## What is Manim?

Manim is a powerful animation engine designed for creating explanatory math videos, created by Grant Sanderson (3Blue1Brown). It allows you to create high-quality animations programmatically with Python.

## Installation Guide

### Prerequisites

- Python 3.8+
- FFmpeg
- LaTeX (for rendering mathematical expressions)

### Step 1: Install System Dependencies

**On macOS:**

```bash
# Install Homebrew if not already installed
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Install FFmpeg
brew install ffmpeg

# Install LaTeX
brew install --cask mactex
```

### Step 2: Set up a Python virtual environment

```bash
cd /Users/ilyaasismailsimmou/spurhacks/SpurHacks
python -m venv manim-env
source manim-env/bin/activate
```

### Step 3: Install Manim

```bash
pip install manim
```

For the community version (which is often easier to use):

```bash
pip install manim-community
```

## Creating Your First Animation

Create a new Python file `animations/first_animation.py`:

```python
from manim import *

class CircleToSquare(Scene):
    def construct(self):
        # Create shapes
        circle = Circle()
        circle.set_fill(BLUE, opacity=0.5)
        square = Square()
        square.set_fill(RED, opacity=0.5)

        # Display circle
        self.play(Create(circle))

        # Transform circle to square
        self.play(Transform(circle, square))

        # Wait for a second and fade out
        self.wait(1)
        self.play(FadeOut(circle))


class DisplayMathFormula(Scene):
    def construct(self):
        # Display a mathematical formula
        formula = MathTex(r"e^{i\pi} + 1 = 0")

        # Add the formula to scene
        self.play(Write(formula))

        # Wait for 2 seconds
        self.wait(2)
```

## Running Animations

From your terminal, run:

```bash
# For low quality (faster rendering)
manim -ql animations/first_animation.py CircleToSquare

# For medium quality
manim -qm animations/first_animation.py CircleToSquare

# For high quality
manim -qh animations/first_animation.py CircleToSquare

# To render all scenes in a file
manim -ql animations/first_animation.py
```

## Integrating with Flask

### Step 1: Create an API endpoint for rendering animations

Add the following to your Flask application:

```python
import os
import uuid
import subprocess
from flask import send_file, jsonify, request

@app.route('/api/render-animation', methods=['POST'])
@jwt_required()
def render_animation():
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
    output_dir = 'static/animations'
    os.makedirs(output_dir, exist_ok=True)

    unique_id = str(uuid.uuid4())
    output_file = f"{output_dir}/{unique_id}"

    try:
        # Run manim command to generate animation
        result = subprocess.run(
            ['manim', '-ql', 'manim_examples.py', scene_class,
             f'--output_file={unique_id}', f'--media_dir={output_dir}'],
            check=True,
            capture_output=True,
            text=True
        )

        # Find the generated file
        for file in os.listdir(output_dir):
            if file.endswith('.mp4') and unique_id in file:
                return jsonify({
                    'animation_url': f'/static/animations/{file}',
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
```

### Step 2: Serve the generated animations

Update your Flask app to serve the static files:

```python
@app.route('/static/animations/<path:filename>')
def serve_animation(filename):
    return send_file(f'static/animations/{filename}')
```

## Frontend Integration

Create a component to display the animations:

```tsx
// src/components/animation-player.tsx
"use client";

import { useState } from "react";
import { useAuth } from "@/lib/auth-context";
import { Button } from "@/components/ui/button";
import { Card } from "@/components/ui/card";

interface AnimationPlayerProps {
  className?: string;
}

export default function AnimationPlayer({ className }: AnimationPlayerProps) {
  const { token } = useAuth();
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const [animationUrl, setAnimationUrl] = useState<string | null>(null);

  const animations = [
    { id: "circle", name: "Create Circle" },
    { id: "square_to_circle", name: "Square to Circle" },
    { id: "text", name: "Write Text" },
    { id: "math", name: "Math Formula" },
  ];

  const renderAnimation = async (animationType: string) => {
    if (!token) {
      setError("You must be logged in to render animations");
      return;
    }

    setLoading(true);
    setError(null);

    try {
      const response = await fetch("/api/render-animation", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          Authorization: `Bearer ${token}`,
        },
        body: JSON.stringify({ animation_type: animationType }),
      });

      const data = await response.json();

      if (response.ok) {
        setAnimationUrl(data.animation_url);
      } else {
        setError(data.error || "Failed to render animation");
      }
    } catch (err) {
      setError("An error occurred while rendering the animation");
      console.error(err);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className={`space-y-4 ${className}`}>
      <h2 className="text-2xl font-bold mb-4">Math Animations</h2>

      <div className="grid grid-cols-2 gap-2 mb-4">
        {animations.map((anim) => (
          <Button
            key={anim.id}
            onClick={() => renderAnimation(anim.id)}
            disabled={loading}
            variant="outline"
            className="h-16"
          >
            {anim.name}
          </Button>
        ))}
      </div>

      {loading && (
        <div className="text-center py-4">
          <div className="inline-block animate-spin h-6 w-6 border-2 border-current border-t-transparent rounded-full"></div>
          <p className="mt-2">Rendering animation...</p>
        </div>
      )}

      {error && (
        <div className="bg-red-50 border border-red-200 text-red-700 px-4 py-3 rounded">
          {error}
        </div>
      )}

      {animationUrl && !loading && (
        <Card className="p-2">
          <video
            src={animationUrl}
            controls
            autoPlay
            className="w-full rounded"
          />
        </Card>
      )}
    </div>
  );
}
```

## Customizing Animations

To create custom animations, you can:

1. Add new scene classes to `manim_examples.py`
2. Update the `animation_map` in the Flask API endpoint
3. Add the new animation option to the `animations` array in the frontend component

## Advanced Usage

### Custom Parameters

Modify the API endpoint to accept parameters for customizing animations:

```python
@app.route('/api/render-animation', methods=['POST'])
@jwt_required()
def render_animation():
    data = request.get_json()

    animation_type = data.get('animation_type')
    text_content = data.get('text_content', 'SpurHacks Demo')
    formula = data.get('formula', r'e^{i\pi} + 1 = 0')

    # Generate a temporary Python script with the customizations
    script_content = f'''
from manim import *

class CustomAnimation(Scene):
    def construct(self):
        {"text = Text(f'{text_content}', font_size=72)" if animation_type == 'text' else ""}
        {"formula = MathTex(r'{formula}', font_size=96)" if animation_type == 'math' else ""}
        # Rest of the animation code...
    '''

    # Save the script and render it...
```

## Resources

- [Manim Community Documentation](https://docs.manim.community/)
- [Manim on GitHub](https://github.com/ManimCommunity/manim/)
- [3Blue1Brown YouTube Channel](https://www.youtube.com/c/3blue1brown) for examples
