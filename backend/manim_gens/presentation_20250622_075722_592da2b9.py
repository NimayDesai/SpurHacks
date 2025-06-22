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

class NumberLineArithmetic(Scene):
    def construct(self):
        # [0:00-0:03] Imagine a number line
        title = Text("Imagine a number line.", font_size=48)
        self.play(Write(title))
        self.wait(0.5)
        
        # Create number line
        number_line = NumberLine(
            x_range=[-8, 8, 1],
            length=12,
            include_numbers=True,
            numbers_to_include=range(-8, 9),
            font_size=24
        )
        
        self.play(FadeOut(title))
        self.play(Create(number_line))
        self.wait(1)
        
        # [0:03-0:09] Addition? It's a journey to the right. Moving forward along the line, accumulating distance.
        addition_text = Text("Addition?  It's a journey to the right.", font_size=36)
        addition_text.to_edge(UP)
        self.play(Write(addition_text))
        
        # Show addition movement
        dot = Dot(number_line.n2p(0), color=BLUE, radius=0.1)
        self.play(FadeIn(dot))
        
        # Move right for addition (e.g., 2 + 3)
        arrow1 = Arrow(number_line.n2p(0), number_line.n2p(2), color=GREEN, stroke_width=4)
        plus_two = Text("+2", font_size=24, color=GREEN).next_to(arrow1, UP)
        self.play(Create(arrow1), Write(plus_two))
        self.play(dot.animate.move_to(number_line.n2p(2)))
        
        arrow2 = Arrow(number_line.n2p(2), number_line.n2p(5), color=GREEN, stroke_width=4)
        plus_three = Text("+3", font_size=24, color=GREEN).next_to(arrow2, UP)
        self.play(Create(arrow2), Write(plus_three))
        self.play(dot.animate.move_to(number_line.n2p(5)))
        
        forward_text = Text("Moving forward along the line, accumulating distance.", font_size=32)
        forward_text.next_to(addition_text, DOWN)
        self.play(Write(forward_text))
        self.wait(1)
        
        # [0:09-0:15] Subtraction? The opposite. A journey to the left. Losing ground, retracing steps.
        self.play(FadeOut(addition_text), FadeOut(forward_text))
        self.play(FadeOut(arrow1), FadeOut(arrow2), FadeOut(plus_two), FadeOut(plus_three))
        
        subtraction_text = Text("Subtraction?  The opposite.", font_size=36)
        subtraction_text.to_edge(UP)
        self.play(Write(subtraction_text))
        
        # Reset dot position
        self.play(dot.animate.move_to(number_line.n2p(5)))
        
        # Show subtraction movement
        arrow3 = Arrow(number_line.n2p(5), number_line.n2p(2), color=RED, stroke_width=4)
        minus_three = Text("-3", font_size=24, color=RED).next_to(arrow3, UP)
        self.play(Create(arrow3), Write(minus_three))
        self.play(dot.animate.move_to(number_line.n2p(2)))
        
        left_text = Text("A journey to the left.", font_size=32)
        left_text.next_to(subtraction_text, DOWN)
        self.play(Write(left_text))
        
        arrow4 = Arrow(number_line.n2p(2), number_line.n2p(0), color=RED, stroke_width=4)
        minus_two = Text("-2", font_size=24, color=RED).next_to(arrow4, UP)
        self.play(Create(arrow4), Write(minus_two))
        self.play(dot.animate.move_to(number_line.n2p(0)))
        
        losing_text = Text("Losing ground, retracing steps.", font_size=32)
        losing_text.next_to(left_text, DOWN)
        self.play(Write(losing_text))
        self.wait(1)
        
        # [0:15-0:18] See how they're mirror images?
        self.play(FadeOut(subtraction_text), FadeOut(left_text), FadeOut(losing_text))
        
        mirror_text = Text("See how they're mirror images?", font_size=36)
        mirror_text.to_edge(UP)
        self.play(Write(mirror_text))
        
        # Show both arrows together to demonstrate mirror effect
        self.play(
            arrow1.animate.set_color(GREEN_B),
            arrow2.animate.set_color(GREEN_B),
            arrow3.animate.set_color(RED_B),
            arrow4.animate.set_color(RED_B)
        )
        self.wait(1)
        
        # [0:18-0:20] One undoes the other.
        undoes_text = Text("One undoes the other.", font_size=36)
        undoes_text.next_to(mirror_text, DOWN)
        self.play(Write(undoes_text))
        self.wait(1)
        
        # [0:20-0:25] Simple, yet fundamental – the building blocks of all arithmetic.
        self.play(FadeOut(mirror_text), FadeOut(undoes_text))
        self.play(FadeOut(arrow1), FadeOut(arrow2), FadeOut(arrow3), FadeOut(arrow4))
        self.play(FadeOut(minus_three), FadeOut(minus_two), FadeOut(plus_two), FadeOut(plus_three))
        
        simple_text = Text("Simple, yet fundamental – the building blocks of all arithmetic.", font_size=36)
        simple_text.to_edge(UP)
        self.play(Write(simple_text))
        self.wait(2)
        
        # [0:25-0:30] It's all about moving along this single, continuous line.
        moving_text = Text("It's all about moving along this single, continuous line.", font_size=36)
        moving_text.next_to(simple_text, DOWN)
        self.play(Write(moving_text))
        
        # Highlight the continuous nature of the line
        highlight_line = Line(number_line.n2p(-8), number_line.n2p(8), color=YELLOW, stroke_width=6)
        self.play(Create(highlight_line))
        self.play(FadeOut(highlight_line))
        
        self.wait(2)
        
        # Final cleanup at [0:30]
        self.play(FadeOut(simple_text), FadeOut(moving_text), FadeOut(dot), FadeOut(number_line))
