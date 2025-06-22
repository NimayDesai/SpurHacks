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

class LimitConcept(Scene):
    def construct(self):
        # Initial question
        title = Text("What does it mean for something to approach a limit?", font_size=36)
        title.to_edge(UP, buff=0.5)
        self.play(Write(title))
        self.wait(5)
        
        # [0:05] - Wall walking analogy
        self.play(FadeOut(title))
        
        analogy_text = Text("Imagine walking towards a wall – you get closer and closer,\nbut never quite touch it.", 
                           font_size=32, text_align="center")
        analogy_text.move_to(UP * 2)
        
        # Visual representation of walking towards wall
        wall = Rectangle(height=3, width=0.2, color=GRAY).to_edge(RIGHT, buff=1)
        person = Circle(radius=0.2, color=BLUE).move_to(LEFT * 4)
        
        self.play(Write(analogy_text))
        self.play(Create(wall), Create(person))
        
        # Show person walking towards wall
        self.play(person.animate.move_to(LEFT * 2), run_time=2)
        self.play(person.animate.move_to(LEFT * 1), run_time=1.5)
        self.play(person.animate.move_to(LEFT * 0.5), run_time=1)
        self.play(person.animate.move_to(LEFT * 0.3), run_time=0.8)
        
        self.wait(1)
        
        # [0:15] - Function limit explanation
        self.play(FadeOut(analogy_text), FadeOut(wall), FadeOut(person))
        
        function_text = Text("A function approaching a limit is similar.", font_size=36)
        function_text.move_to(UP * 2.5)
        
        limit_text = Text("As the input gets arbitrarily close to a specific value,\nthe output gets arbitrarily close to the limit.", 
                         font_size=32, text_align="center")
        limit_text.move_to(UP * 0.5)
        
        # Create coordinate plane
        plane = NumberPlane(
            x_range=[-3, 3, 1],
            y_range=[-2, 4, 1],
            x_length=8,
            y_length=5,
            background_line_style={"stroke_opacity": 0.3}
        ).scale(0.7).move_to(DOWN * 1.5)
        
        # Create a function that approaches a limit
        def func(x):
            return 2 + (x - 1)**2 / 4
        
        curve = plane.plot(
            func,
            x_range=[-2.5, 2.5],
            color=YELLOW,
            stroke_width=3
        )
        
        # Show approach to x = 1, limit = 2
        limit_line = DashedLine(
            plane.c2p(-3, 2), 
            plane.c2p(3, 2),
            color=RED,
            stroke_width=2
        )
        
        vertical_line = DashedLine(
            plane.c2p(1, -2),
            plane.c2p(1, 4),
            color=GREEN,
            stroke_width=2
        )
        
        self.play(Write(function_text))
        self.wait(2)
        self.play(Write(limit_text))
        self.play(Create(plane), Create(curve))
        self.play(Create(limit_line), Create(vertical_line))
        
        # Show points approaching the limit
        approaching_points = []
        x_values = [0.5, 0.8, 0.9, 0.95, 0.99]
        
        for x_val in x_values:
            point = Dot(plane.c2p(x_val, func(x_val)), color=BLUE, radius=0.05)
            approaching_points.append(point)
            self.play(Create(point), run_time=0.5)
        
        self.wait(2)
        
        # [0:25] - Not about reaching the value
        self.play(
            FadeOut(function_text), 
            FadeOut(limit_text),
            FadeOut(plane),
            FadeOut(curve),
            FadeOut(limit_line),
            FadeOut(vertical_line),
            *[FadeOut(point) for point in approaching_points]
        )
        
        reaching_text = Text("It's not about actually *reaching* the value,\nbut about getting infinitely close.", 
                            font_size=36, text_align="center")
        reaching_text.move_to(ORIGIN)
        
        self.play(Write(reaching_text))
        self.wait(3)
        
        # [0:35] - Cornerstone of calculus
        self.play(FadeOut(reaching_text))
        
        cornerstone_text = Text("This seemingly simple idea is a cornerstone of calculus,\nunlocking a deep understanding of change and continuity.", 
                               font_size=32, text_align="center")
        cornerstone_text.move_to(ORIGIN)
        
        self.play(Write(cornerstone_text))
        self.wait(3)
        
        self.play(FadeOut(cornerstone_text))
