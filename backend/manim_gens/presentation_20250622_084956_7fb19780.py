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

class LimitExplanation(Scene):
    def construct(self):
        # [0:00] - [0:05]
        title = Text("What does it mean for a function to have a limit?", font_size=36)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(5)
        
        # [0:05] - [0:15]
        self.play(FadeOut(title))
        
        # Create a graph for walking visualization
        plane = NumberPlane(
            x_range=[-3, 3, 1],
            y_range=[-2, 3, 1],
            x_length=8,
            y_length=5,
            background_line_style={"stroke_opacity": 0.3}
        )
        
        # Define a function with a removable discontinuity
        def func(x):
            return (x**2 - 1) / (x - 1) if x != 1 else None
        
        # Plot the function except at x = 1
        curve = plane.plot(
            lambda x: x + 1,
            x_range=[-2.5, 0.99],
            color=BLUE,
            stroke_width=4
        )
        curve2 = plane.plot(
            lambda x: x + 1,
            x_range=[1.01, 2.5],
            color=BLUE,
            stroke_width=4
        )
        
        # Add a hole at x = 1
        hole = Circle(radius=0.08, color=WHITE, fill_opacity=1).move_to(plane.c2p(1, 2))
        hole_outline = Circle(radius=0.08, color=BLUE, fill_opacity=0, stroke_width=2).move_to(plane.c2p(1, 2))
        
        # Add a walking dot
        dot = Dot(color=RED, radius=0.1).move_to(plane.c2p(-2, -1))
        
        text1 = Text("Imagine walking along a graph.", font_size=28)
        text2 = Text("A limit describes where you're headed, not necessarily where you are.", font_size=28)
        text1.to_edge(UP)
        text2.next_to(text1, DOWN, buff=0.3)
        
        self.play(Create(plane), Create(curve), Create(curve2), Create(hole), Create(hole_outline))
        self.play(Write(text1))
        self.play(Create(dot))
        self.play(MoveAlongPath(dot, Line(plane.c2p(-2, -1), plane.c2p(0.5, 1.5))))
        self.play(Write(text2))
        self.wait(3)
        
        # [0:15] - [0:25]
        self.play(FadeOut(text1), FadeOut(text2), FadeOut(dot))
        
        text3 = Text("Even if the function's undefined at a point,", font_size=28)
        text4 = Text("the limit tells us the value it *approaches* as we get arbitrarily close.", font_size=28)
        text3.to_edge(UP)
        text4.next_to(text3, DOWN, buff=0.3)
        
        # Highlight the hole
        highlight = Circle(radius=0.3, color=YELLOW, fill_opacity=0, stroke_width=3).move_to(plane.c2p(1, 2))
        
        # Add approaching dots
        dot_left = Dot(color=GREEN, radius=0.08).move_to(plane.c2p(0.5, 1.5))
        dot_right = Dot(color=GREEN, radius=0.08).move_to(plane.c2p(1.5, 2.5))
        
        self.play(Write(text3))
        self.play(Create(highlight), Flash(hole))
        self.play(Write(text4))
        self.play(Create(dot_left), Create(dot_right))
        self.play(
            dot_left.animate.move_to(plane.c2p(0.9, 1.9)),
            dot_right.animate.move_to(plane.c2p(1.1, 2.1))
        )
        self.wait(2)
        
        # [0:25] - [0:35]
        self.play(FadeOut(text3), FadeOut(text4), FadeOut(highlight), FadeOut(dot_left), FadeOut(dot_right))
        
        text5 = Text("Think of it like aiming for a target –", font_size=28)
        text6 = Text("you might not hit it perfectly, but your approach matters.", font_size=28)
        text5.to_edge(UP)
        text6.next_to(text5, DOWN, buff=0.3)
        
        # Create target visualization
        target = Circle(radius=0.15, color=RED, fill_opacity=0.5).move_to(plane.c2p(1, 2))
        target_center = Dot(color=RED, radius=0.05).move_to(plane.c2p(1, 2))
        
        # Arrows approaching the target
        arrow1 = Arrow(plane.c2p(0.3, 1.3), plane.c2p(0.9, 1.9), color=ORANGE, buff=0.1)
        arrow2 = Arrow(plane.c2p(1.7, 2.7), plane.c2p(1.1, 2.1), color=ORANGE, buff=0.1)
        
        self.play(Write(text5))
        self.play(Create(target), Create(target_center))
        self.play(Write(text6))
        self.play(Create(arrow1), Create(arrow2))
        self.wait(2)
        
        # [0:35] - End
        self.play(FadeOut(text5), FadeOut(text6), FadeOut(target), FadeOut(target_center), FadeOut(arrow1), FadeOut(arrow2))
        
        text7 = Text("Limits are the foundation for calculus;", font_size=28)
        text8 = Text("they help us understand instantaneous change and", font_size=28)
        text9 = Text("the behavior of functions at crucial points.", font_size=28)
        text7.to_edge(UP)
        text8.next_to(text7, DOWN, buff=0.3)
        text9.next_to(text8, DOWN, buff=0.3)
        
        self.play(Write(text7))
        self.play(Write(text8))
        self.play(Write(text9))
        self.wait(3)
        
        # Final cleanup
        self.play(FadeOut(plane), FadeOut(curve), FadeOut(curve2), FadeOut(hole), FadeOut(hole_outline))
        self.play(FadeOut(text7), FadeOut(text8), FadeOut(text9))
