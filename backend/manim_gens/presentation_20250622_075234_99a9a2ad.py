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

class NumberLineScript(Scene):
    def construct(self):
        # Create number line
        number_line = NumberLine(
            x_range=[-8, 8, 1],
            length=12,
            include_numbers=True,
            numbers_to_include=range(-8, 9),
            font_size=24
        )
        
        # Initial text
        initial_text = Text("Imagine a number line.", font_size=36)
        self.play(Write(initial_text))
        self.wait(1)
        
        # Show number line
        self.play(FadeOut(initial_text))
        self.play(Create(number_line))
        self.wait(1)
        
        # [0:05] Addition text and animation
        addition_text = Text("Addition? That's a journey to the right,", font_size=32)
        addition_text.to_edge(UP)
        self.play(Write(addition_text))
        
        # Show addition movement
        dot = Dot(color=BLUE).move_to(number_line.number_to_point(0))
        self.play(Create(dot))
        arrow_right = Arrow(
            start=number_line.number_to_point(0),
            end=number_line.number_to_point(3),
            color=GREEN,
            stroke_width=4
        )
        self.play(Create(arrow_right))
        self.play(dot.animate.move_to(number_line.number_to_point(3)))
        
        moving_text = Text("moving forward by the amount added.", font_size=32)
        moving_text.next_to(addition_text, DOWN)
        self.play(Write(moving_text))
        self.wait(1)
        
        # Clear for next section
        self.play(FadeOut(addition_text), FadeOut(moving_text), FadeOut(arrow_right))
        
        # [0:10] Subtraction text and animation
        subtraction_text = Text("Subtraction? A step to the left,", font_size=32)
        subtraction_text.to_edge(UP)
        self.play(Write(subtraction_text))
        
        # Show subtraction movement
        arrow_left = Arrow(
            start=number_line.number_to_point(3),
            end=number_line.number_to_point(1),
            color=RED,
            stroke_width=4
        )
        self.play(Create(arrow_left))
        self.play(dot.animate.move_to(number_line.number_to_point(1)))
        
        traveling_text = Text("traveling backward.", font_size=32)
        traveling_text.next_to(subtraction_text, DOWN)
        self.play(Write(traveling_text))
        self.wait(1)
        
        # Clear for next section
        self.play(FadeOut(subtraction_text), FadeOut(traveling_text), FadeOut(arrow_left))
        
        # [0:15] Larger subtraction
        larger_sub_text = Text("But what if we subtract a larger number than we have?", font_size=32)
        larger_sub_text.to_edge(UP)
        self.play(Write(larger_sub_text))
        
        # Show movement past zero
        arrow_past_zero = Arrow(
            start=number_line.number_to_point(1),
            end=number_line.number_to_point(-3),
            color=PURPLE,
            stroke_width=4
        )
        self.play(Create(arrow_past_zero))
        self.play(dot.animate.move_to(number_line.number_to_point(-3)))
        self.wait(1)
        
        # Clear for next section
        self.play(FadeOut(larger_sub_text), FadeOut(arrow_past_zero))
        
        # [0:20] Continue past zero text
        continue_text = Text("We simply continue past zero, into the negative territory.", font_size=32)
        continue_text.to_edge(UP)
        self.play(Write(continue_text))
        
        direction_text = Text("It's all about direction and distance,", font_size=32)
        direction_text.next_to(continue_text, DOWN)
        self.play(Write(direction_text))
        self.wait(1)
        
        # Clear for final section
        self.play(FadeOut(continue_text), FadeOut(direction_text))
        
        # Final unified system text
        unified_text = Text("a unified system of movement along a single line.", font_size=32)
        unified_text.to_edge(UP)
        self.play(Write(unified_text))
        
        # [0:28] Final text about interconnectedness
        final_text = Text("This simple framework reveals the beautiful", font_size=32)
        final_text.next_to(unified_text, DOWN)
        interconnected_text = Text("interconnectedness of addition and subtraction.", font_size=32)
        interconnected_text.next_to(final_text, DOWN)
        
        self.play(Write(final_text))
        self.play(Write(interconnected_text))
        self.wait(2)
        
        # Clear everything at the end
        self.play(FadeOut(unified_text), FadeOut(final_text), FadeOut(interconnected_text), 
                  FadeOut(dot), FadeOut(number_line))
