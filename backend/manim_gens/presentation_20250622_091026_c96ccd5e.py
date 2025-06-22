# Manim configuration for LaTeX
import os
import sys

# Add MiKTeX to PATH (adjust path as needed for your system)
if sys.platform.startswith('win'):
    os.environ['PATH'] += r';C:\Program Files\MiKTeX\miktex\bin\x64'
elif sys.platform.startswith('darwin'):  # macOS
    os.environ['PATH'] += ':/usr/local/bin:/opt/homebrew/bin'
    
from manim import *

# Configure LaTeX template
config.tex_template = TexTemplate()
config.tex_template.add_to_preamble(r"\usepackage{amsmath}")
config.tex_template.add_to_preamble(r"\usepackage{amssymb}")
config.tex_template.add_to_preamble(r"\usepackage{mathtools}")
config.tex_template.add_to_preamble(r"\usepackage{physics}")

from manim import *

class LinearAlgebraTransformations(Scene):
    def construct(self):
        # [0:00-0:05] Linear algebra, at its core, is about transformations.
        title = Text("Linear algebra, at its core, is about transformations.", font_size=48)
        self.play(Write(title))
        self.wait(5)
        
        # [0:05] Fade out title and show transformation examples
        self.play(FadeOut(title))
        
        # [0:05-0:15] Imagine stretching, rotating, or shearing a space. These actions, seemingly disparate, are all described by matrices.
        transformation_text = Text("Imagine stretching, rotating, or shearing a space.", font_size=40)
        transformation_text.to_edge(UP)
        self.play(Write(transformation_text))
        
        # Create a simple grid to show transformations
        grid = NumberPlane(
            x_range=[-3, 3, 1],
            y_range=[-2, 2, 1],
            background_line_style={"stroke_color": BLUE, "stroke_width": 1}
        )
        grid.scale(0.8)
        self.play(Create(grid))
        
        # Show original vector
        original_vector = Arrow(ORIGIN, [2, 1, 0], color=RED, buff=0)
        self.play(Create(original_vector))
        
        self.wait(2)
        
        # Show stretching transformation
        stretch_text = Text("Stretching", font_size=32, color=YELLOW)
        stretch_text.to_edge(DOWN, buff=1)
        self.play(Write(stretch_text))
        
        stretched_vector = Arrow(ORIGIN, [3, 1.5, 0], color=GREEN, buff=0)
        self.play(Transform(original_vector, stretched_vector))
        self.wait(1)
        
        # Show rotation transformation
        self.play(FadeOut(stretch_text))
        rotation_text = Text("Rotating", font_size=32, color=YELLOW)
        rotation_text.to_edge(DOWN, buff=1)
        self.play(Write(rotation_text))
        
        rotated_vector = Arrow(ORIGIN, [-1, 2, 0], color=PURPLE, buff=0)
        self.play(Transform(original_vector, rotated_vector))
        self.wait(1)
        
        # Show shearing transformation
        self.play(FadeOut(rotation_text))
        shear_text = Text("Shearing", font_size=32, color=YELLOW)
        shear_text.to_edge(DOWN, buff=1)
        self.play(Write(shear_text))
        
        sheared_vector = Arrow(ORIGIN, [1, 2, 0], color=ORANGE, buff=0)
        self.play(Transform(original_vector, sheared_vector))
        self.wait(2)
        
        matrices_text = Text("These actions, seemingly disparate, are all described by matrices.", font_size=36)
        matrices_text.to_edge(DOWN)
        self.play(FadeOut(shear_text), Write(matrices_text))
        self.wait(5)
        
        # [0:15-0:20] Clear and show matrix acting on vector
        self.play(FadeOut(transformation_text), FadeOut(matrices_text), FadeOut(grid), FadeOut(original_vector))
        
        matrix_action_text = Text("A matrix acts on a vector, transforming it to a new position.", font_size=44)
        self.play(Write(matrix_action_text))
        self.wait(5)
        
        # [0:20-0:28] Show the recipe analogy
        self.play(FadeOut(matrix_action_text))
        
        recipe_text = Text("Think of it as a recipe:", font_size=42)
        recipe_text.to_edge(UP)
        self.play(Write(recipe_text))
        
        matrix_part = Text("the matrix defines the operation,", font_size=36, color=BLUE)
        matrix_part.move_to([0, 1, 0])
        
        vector_part = Text("the vector is the ingredient,", font_size=36, color=RED)
        vector_part.move_to([0, 0, 0])
        
        result_part = Text("and the result is the transformed vector.", font_size=36, color=GREEN)
        result_part.move_to([0, -1, 0])
        
        self.play(Write(matrix_part))
        self.wait(1)
        self.play(Write(vector_part))
        self.wait(1)
        self.play(Write(result_part))
        self.wait(3)
        
        # [0:28-0:35] Final message about applications
        self.play(
            FadeOut(recipe_text),
            FadeOut(matrix_part),
            FadeOut(vector_part),
            FadeOut(result_part)
        )
        
        applications_text = Text(
            "This simple idea underlies countless applications,\nfrom computer graphics to machine learning.",
            font_size=40
        )
        self.play(Write(applications_text))
        self.wait(7)
        
        # Clear everything at the end
        self.play(FadeOut(applications_text))
