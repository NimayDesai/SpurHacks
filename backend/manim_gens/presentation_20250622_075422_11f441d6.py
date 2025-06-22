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

class NumberLineScene(Scene):
    def construct(self):
        # Initial setup
        number_line = NumberLine(
            x_range=[-8, 8, 1],
            length=12,
            include_numbers=True,
            numbers_to_include=range(-8, 9),
            font_size=24
        )
        number_line.move_to(ORIGIN)
        
        # Starting text
        text1 = Text("Imagine counting forward along a number line: that's addition.", font_size=32)
        text1.to_edge(UP)
        
        self.play(Write(text1))
        self.play(Create(number_line))
        
        # Create a dot to represent position
        dot = Dot(color=RED, radius=0.1)
        dot.move_to(number_line.number_to_point(0))
        self.play(FadeIn(dot))
        
        self.wait(5)  # [0:05]
        
        # Clear and show next part
        self.play(FadeOut(text1))
        text2 = Text("Each step represents adding one.", font_size=32)
        text2.to_edge(UP)
        self.play(Write(text2))
        
        # Show forward movement (addition)
        for i in range(1, 4):
            self.play(dot.animate.move_to(number_line.number_to_point(i)), run_time=0.5)
        
        self.wait(5)  # [0:10]
        
        # Clear and show subtraction
        self.play(FadeOut(text2))
        text3 = Text("Now, reverse direction: that's subtraction.", font_size=32)
        text3.to_edge(UP)
        self.play(Write(text3))
        
        # Show backward movement (subtraction)
        for i in range(2, -1, -1):
            self.play(dot.animate.move_to(number_line.number_to_point(i)), run_time=0.5)
        
        self.wait(5)  # [0:15]
        
        # Clear and show next part
        self.play(FadeOut(text3))
        text4 = Text("Subtracting three means taking three steps backward.", font_size=32)
        text4.to_edge(UP)
        self.play(Write(text4))
        
        # Move dot to position 3 first
        self.play(dot.animate.move_to(number_line.number_to_point(3)))
        
        # Show subtracting three steps
        for i in range(2, -1, -1):
            self.play(dot.animate.move_to(number_line.number_to_point(i)), run_time=0.7)
        
        self.wait(5)  # [0:20]
        
        # Clear and show next part
        self.play(FadeOut(text4))
        text5 = Text("It's just the inverse of addition; undoing the steps you've already taken.", font_size=30)
        text5.to_edge(UP)
        self.play(Write(text5))
        
        # Show the inverse relationship
        # First go forward
        for i in range(1, 4):
            self.play(dot.animate.move_to(number_line.number_to_point(i)), run_time=0.4)
        
        # Then go backward (undoing)
        for i in range(2, -1, -1):
            self.play(dot.animate.move_to(number_line.number_to_point(i)), run_time=0.4)
        
        self.wait(5)  # [0:25]
        
        # Clear and show next part
        self.play(FadeOut(text5))
        text6 = Text("See how they're intimately connected?", font_size=32)
        text6.to_edge(UP)
        self.play(Write(text6))
        
        # Show connection with arrows
        plus_arrow = Arrow(start=ORIGIN, end=RIGHT*2, color=GREEN)
        plus_arrow.next_to(number_line, DOWN, buff=0.5)
        plus_text = Text("+", font_size=24, color=GREEN)
        plus_text.next_to(plus_arrow, DOWN, buff=0.2)
        
        minus_arrow = Arrow(start=RIGHT*2, end=ORIGIN, color=RED)
        minus_arrow.next_to(plus_arrow, DOWN, buff=0.3)
        minus_text = Text("-", font_size=24, color=RED)
        minus_text.next_to(minus_arrow, DOWN, buff=0.2)
        
        self.play(Create(plus_arrow), Write(plus_text))
        self.play(Create(minus_arrow), Write(minus_text))
        
        self.wait(5)  # [0:30]
        
        # Final message
        self.play(FadeOut(text6))
        text7 = Text("Addition and subtraction aren't separate operations, but two sides of the same coin,", font_size=28)
        text8 = Text("movements along a number line.", font_size=28)
        text7.to_edge(UP)
        text8.next_to(text7, DOWN, buff=0.3)
        
        self.play(Write(text7))
        self.play(Write(text8))
        
        # Final demonstration
        self.play(dot.animate.move_to(number_line.number_to_point(4)), run_time=1)
        self.play(dot.animate.move_to(number_line.number_to_point(-2)), run_time=1)
        self.play(dot.animate.move_to(number_line.number_to_point(1)), run_time=1)
        
        # Clear everything
        self.play(
            FadeOut(text7),
            FadeOut(text8),
            FadeOut(number_line),
            FadeOut(dot),
            FadeOut(plus_arrow),
            FadeOut(plus_text),
            FadeOut(minus_arrow),
            FadeOut(minus_text)
        )
