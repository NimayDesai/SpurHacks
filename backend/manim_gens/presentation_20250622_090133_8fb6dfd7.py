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

class VectorScene(Scene):
    def construct(self):
        # [0:00] - Imagine an arrow
        arrow1 = Arrow(start=ORIGIN, end=[2, 1, 0], color=BLUE, stroke_width=6)
        self.play(Create(arrow1))
        
        # [0:05] - Its length shows magnitude, its direction, well, its direction
        self.wait(5)
        text1 = Text("Its length shows magnitude, its direction, well, its direction.", font_size=36)
        text1.to_edge(UP)
        self.play(Write(text1))
        
        # Visual emphasis on length and direction
        length_line = Line(ORIGIN, [2, 1, 0], color=YELLOW, stroke_width=8)
        direction_arc = Arc(angle=np.arctan(0.5), radius=0.5, color=GREEN, stroke_width=4)
        self.play(Create(length_line), Create(direction_arc))
        self.wait(1)
        self.play(FadeOut(length_line), FadeOut(direction_arc))
        
        # [0:10] - That's a vector
        self.wait(5)
        self.play(FadeOut(text1))
        text2 = Text("That's a vector.", font_size=36)
        text2.to_edge(UP)
        self.play(Write(text2))
        
        # [0:18] - But it's more than just an arrow; it's a displacement, a force, a velocity—anything with both size and direction
        self.wait(8)
        self.play(FadeOut(text2))
        text3 = Text("But it's more than just an arrow; it's a displacement, a force, a velocity—", font_size=28)
        text4 = Text("anything with both size and direction.", font_size=28)
        text3.to_edge(UP)
        text4.next_to(text3, DOWN)
        self.play(Write(text3), Write(text4))
        
        # Show different vector representations
        displacement_arrow = Arrow(start=[-3, -1, 0], end=[-1, 0, 0], color=RED, stroke_width=4)
        force_arrow = Arrow(start=[0, -2, 0], end=[1, -1, 0], color=GREEN, stroke_width=4)
        velocity_arrow = Arrow(start=[2, -1, 0], end=[4, 0, 0], color=PURPLE, stroke_width=4)
        
        displacement_label = Text("displacement", font_size=20, color=RED)
        force_label = Text("force", font_size=20, color=GREEN)
        velocity_label = Text("velocity", font_size=20, color=PURPLE)
        
        displacement_label.next_to(displacement_arrow, DOWN)
        force_label.next_to(force_arrow, DOWN)
        velocity_label.next_to(velocity_arrow, DOWN)
        
        self.play(
            Create(displacement_arrow), Write(displacement_label),
            Create(force_arrow), Write(force_label),
            Create(velocity_arrow), Write(velocity_label)
        )
        
        # [0:22] - See how we can add them? Tip to tail
        self.wait(4)
        self.play(
            FadeOut(text3), FadeOut(text4),
            FadeOut(displacement_arrow), FadeOut(displacement_label),
            FadeOut(force_arrow), FadeOut(force_label),
            FadeOut(velocity_arrow), FadeOut(velocity_label),
            FadeOut(arrow1)
        )
        
        text5 = Text("See how we can add them? Tip to tail.", font_size=36)
        text5.to_edge(UP)
        self.play(Write(text5))
        
        # Demonstrate vector addition tip to tail
        vector_a = Arrow(start=[-2, 0, 0], end=[0, 1, 0], color=BLUE, stroke_width=4)
        vector_b = Arrow(start=[0, 1, 0], end=[2, 0, 0], color=RED, stroke_width=4)
        vector_sum = Arrow(start=[-2, 0, 0], end=[2, 0, 0], color=YELLOW, stroke_width=6)
        
        self.play(Create(vector_a))
        self.wait(0.5)
        self.play(Create(vector_b))
        self.wait(0.5)
        self.play(Create(vector_sum))
        
        # [0:25] - It's intuitive, geometric
        self.wait(3)
        self.play(FadeOut(text5))
        text6 = Text("It's intuitive, geometric.", font_size=36)
        text6.to_edge(UP)
        self.play(Write(text6))
        
        # [0:30] - And this simple idea unlocks a universe of understanding in physics and beyond
        self.wait(5)
        self.play(FadeOut(text6))
        text7 = Text("And this simple idea unlocks a universe of understanding", font_size=28)
        text8 = Text("in physics and beyond.", font_size=28)
        text7.to_edge(UP)
        text8.next_to(text7, DOWN)
        self.play(Write(text7), Write(text8))
        
        # Final visual flourish
        self.play(
            vector_a.animate.set_color(GOLD),
            vector_b.animate.set_color(GOLD),
            vector_sum.animate.set_color(GOLD)
        )
        
        self.wait(2)
        
        # Clear everything at the end
        self.play(
            FadeOut(text7), FadeOut(text8),
            FadeOut(vector_a), FadeOut(vector_b), FadeOut(vector_sum)
        )
