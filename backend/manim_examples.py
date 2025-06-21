"""
This file contains examples of Manim animations that can be used in the SpurHacks project.
"""

import os
import sys
from manim import *

class CreateCircle(Scene):
    def construct(self):
        circle = Circle()  # create a circle
        circle.set_fill(PINK, opacity=0.5)  # set the color and opacity
        self.play(Create(circle))  # show the circle on screen
        self.wait(1)
        
class SquareToCircle(Scene):
    def construct(self):
        circle = Circle()  # create a circle
        circle.set_fill(PINK, opacity=0.5)  # set color and opacity

        square = Square()  # create a square
        square.rotate(PI / 4)  # rotate it slightly
        square.set_fill(BLUE, opacity=0.5)  # set color and opacity

        self.play(Create(square))  # animate the creation of the square
        self.wait(1)
        self.play(Transform(square, circle))  # transform the square into a circle
        self.wait(1)
        self.play(FadeOut(square))  # fade out the square/circle
        
class WriteText(Scene):
    def construct(self):
        # Check if custom text is provided via environment variable
        custom_text = os.environ.get('MANIM_CUSTOM_TEXT', 'SpurHacks Demo')
        text = Text(custom_text, font_size=72)
        self.play(Write(text))
        self.wait(2)
        
class MathExample(Scene):
    def construct(self):
        # Check if custom formula is provided via environment variable
        custom_formula = os.environ.get('MANIM_CUSTOM_FORMULA', r"e^{i\pi} + 1 = 0")
        
        # Write a math equation
        formula = MathTex(custom_formula, font_size=96)
        self.play(Write(formula))
        self.wait(2)
        
        # Transform to another equation if it's the default
        if custom_formula == r"e^{i\pi} + 1 = 0":
            new_formula = MathTex(r"e^{i\pi} = -1", font_size=96)
            self.play(TransformMatchingTex(formula, new_formula))
            self.wait(2)

class CustomTextAnimation(Scene):
    def construct(self):
        # Get custom text from environment variable
        custom_text = os.environ.get('MANIM_CUSTOM_TEXT', 'Custom Text Animation')
        
        # Create animated text
        text = Text(custom_text, font_size=48)
        text.set_color_by_gradient(BLUE, GREEN)
        
        # Animate the text appearing
        self.play(Write(text))
        self.wait(1)
        
        # Scale and rotate the text
        self.play(text.animate.scale(1.5).rotate(PI/6))
        self.wait(1)
        
        # Change color
        self.play(text.animate.set_color(RED))
        self.wait(1)
        
        # Fade out
        self.play(FadeOut(text))

class CustomMathAnimation(Scene):
    def construct(self):
        # Get custom formula from environment variable
        custom_formula = os.environ.get('MANIM_CUSTOM_FORMULA', r"f(x) = x^2")
        
        # Create the formula
        formula = MathTex(custom_formula, font_size=72)
        formula.set_color(YELLOW)
        
        # Animate the formula
        self.play(Write(formula))
        self.wait(1)
        
        # Move it around
        self.play(formula.animate.to_edge(UP))
        self.wait(1)
        
        # Add some explanation text
        explanation = Text("A mathematical expression", font_size=36)
        explanation.next_to(formula, DOWN, buff=1)
        self.play(Write(explanation))
        self.wait(2)
        
        # Fade everything out
        self.play(FadeOut(formula), FadeOut(explanation))
