"""
This file contains examples of Manim animations that can be used in the SpurHacks project.
"""

from manim import *

class CreateCircle(Scene):
    def construct(self):
        circle = Circle()  # create a circle
        circle.set_fill(PINK, opacity=0.5)  # set the color and opacity
        self.play(Create(circle))  # show the circle on screen
        
class SquareToCircle(Scene):
    def construct(self):
        circle = Circle()  # create a circle
        circle.set_fill(PINK, opacity=0.5)  # set color and opacity

        square = Square()  # create a square
        square.rotate(PI / 4)  # rotate it slightly
        square.set_fill(BLUE, opacity=0.5)  # set color and opacity

        self.play(Create(square))  # animate the creation of the square
        self.play(Transform(square, circle))  # transform the square into a circle
        self.play(FadeOut(square))  # fade out the square/circle
        
class WriteText(Scene):
    def construct(self):
        text = Text("SpurHacks Demo", font_size=72)
        self.play(Write(text))
        self.wait(2)
        
class MathExample(Scene):
    def construct(self):
        # Write a math equation
        formula = MathTex(r"e^{i\pi} + 1 = 0", font_size=96)
        self.play(Write(formula))
        self.wait(2)
        
        # Transform to another equation
        new_formula = MathTex(r"e^{i\pi} = -1", font_size=96)
        self.play(TransformMatchingTex(formula, new_formula))
        self.wait(2)
