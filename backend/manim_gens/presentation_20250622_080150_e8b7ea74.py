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

class NumberLineOperations(Scene):
    def construct(self):
        # Initial text
        title = Text("Imagine a number line.", font_size=36)
        self.play(Write(title))
        self.wait(1)
        
        # Create number line
        number_line = NumberLine(
            x_range=[-8, 8, 1],
            length=12,
            color=WHITE,
            include_numbers=True,
            label_direction=DOWN,
            font_size=24
        )
        
        self.play(FadeOut(title))
        self.play(Create(number_line))
        self.wait(0.5)
        
        # [0:05] Addition explanation
        addition_text = Text("Addition? It's a journey to the right; each number added pushes us further.", font_size=28)
        addition_text.to_edge(UP)
        
        # Visual for addition
        dot = Dot(number_line.n2p(0), color=RED, radius=0.1)
        arrow1 = Arrow(number_line.n2p(0), number_line.n2p(3), color=GREEN, buff=0)
        arrow1.shift(UP * 0.3)
        plus_label = Text("+3", font_size=20, color=GREEN)
        plus_label.next_to(arrow1, UP, buff=0.1)
        
        self.play(Write(addition_text))
        self.play(Create(dot))
        self.play(Create(arrow1), Write(plus_label))
        self.play(dot.animate.move_to(number_line.n2p(3)))
        self.wait(1)
        
        # [0:10] Subtraction explanation
        self.play(FadeOut(addition_text))
        subtraction_text = Text("Subtraction? A journey to the left; each number subtracted pulls us back.", font_size=28)
        subtraction_text.to_edge(UP)
        
        # Visual for subtraction
        arrow2 = Arrow(number_line.n2p(3), number_line.n2p(-1), color=BLUE, buff=0)
        arrow2.shift(DOWN * 0.3)
        minus_label = Text("-4", font_size=20, color=BLUE)
        minus_label.next_to(arrow2, DOWN, buff=0.1)
        
        self.play(Write(subtraction_text))
        self.play(Create(arrow2), Write(minus_label))
        self.play(dot.animate.move_to(number_line.n2p(-1)))
        self.wait(1)
        
        # [0:15] Opposites explanation
        self.play(FadeOut(subtraction_text))
        opposites_text = Text("See how they're opposites, inverse operations?", font_size=28)
        opposites_text.to_edge(UP)
        
        self.play(Write(opposites_text))
        self.wait(1)
        
        # [0:20] Mirroring movement
        self.play(FadeOut(opposites_text))
        mirror_text = Text("One undoes the other, mirroring each other's movement.", font_size=28)
        mirror_text.to_edge(UP)
        
        # Show the reverse operations
        reverse_arrow1 = Arrow(number_line.n2p(-1), number_line.n2p(3), color=GREEN, buff=0)
        reverse_arrow1.shift(UP * 0.6)
        reverse_plus_label = Text("+4", font_size=20, color=GREEN)
        reverse_plus_label.next_to(reverse_arrow1, UP, buff=0.1)
        
        self.play(Write(mirror_text))
        self.play(Create(reverse_arrow1), Write(reverse_plus_label))
        self.play(dot.animate.move_to(number_line.n2p(3)))
        self.wait(1)
        
        # [0:25] Change and movement
        self.play(FadeOut(mirror_text))
        change_text = Text("This isn't just about numbers; it's about change, movement along a scale.", font_size=28)
        change_text.to_edge(UP)
        
        self.play(Write(change_text))
        self.wait(1)
        
        # [0:30] Positive and negative change
        self.play(FadeOut(change_text))
        change_types_text = Text("Addition, positive change; subtraction, negative change.", font_size=28)
        change_types_text.to_edge(UP)
        
        # Highlight the arrows with labels
        positive_label = Text("Positive Change", font_size=20, color=GREEN)
        positive_label.next_to(arrow1, UP, buff=0.5)
        negative_label = Text("Negative Change", font_size=20, color=BLUE)
        negative_label.next_to(arrow2, DOWN, buff=0.5)
        
        self.play(Write(change_types_text))
        self.play(Write(positive_label), Write(negative_label))
        self.wait(1)
        
        # [0:35] Final statement
        self.play(FadeOut(change_types_text))
        final_text = Text("Simple, yet fundamental.", font_size=36)
        final_text.to_edge(UP)
        
        self.play(Write(final_text))
        self.wait(2)
        
        # Clear everything at the end
        self.play(FadeOut(VGroup(
            number_line, dot, arrow1, arrow2, reverse_arrow1,
            plus_label, minus_label, reverse_plus_label,
            positive_label, negative_label, final_text
        )))
