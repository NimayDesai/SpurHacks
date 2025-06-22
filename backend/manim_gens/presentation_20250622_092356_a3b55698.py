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
        # [0:00] - Opening text about vectors
        opening_text = Text("Vectors aren't just arrows; they're a way to represent magnitude and direction.", 
                           font_size=36)
        opening_text.move_to(UP * 2)
        
        # Show a vector arrow
        vector_arrow = Arrow(start=LEFT * 2, end=RIGHT * 2 + UP * 1, color=BLUE, buff=0)
        vector_arrow.move_to(DOWN * 0.5)
        
        self.play(Write(opening_text))
        self.play(Create(vector_arrow))
        self.wait(1)
        
        # [0:05] - Box pushing example
        self.play(FadeOut(opening_text), FadeOut(vector_arrow))
        
        box_text = Text("Imagine pushing a box – the force has strength and a specific way it pushes.", 
                       font_size=36)
        box_text.move_to(UP * 2)
        
        # Draw a box
        box = Rectangle(width=1.5, height=1, color=YELLOW, fill_opacity=0.3)
        box.move_to(LEFT * 2)
        
        # Force vector pushing the box
        force_vector = Arrow(start=LEFT * 3.5, end=LEFT * 2, color=RED, buff=0.2)
        force_label = Text("Force", font_size=24, color=RED)
        force_label.next_to(force_vector, DOWN)
        
        self.play(Write(box_text))
        self.play(Create(box), Create(force_vector), Write(force_label))
        self.wait(2)
        
        # [0:10] - "That's a vector!"
        self.play(FadeOut(box_text), FadeOut(box), FadeOut(force_vector), FadeOut(force_label))
        
        thats_vector_text = Text("That's a vector!", font_size=48, color=GREEN)
        self.play(Write(thats_vector_text))
        self.wait(2)
        
        # [0:15] - Vector addition and scaling
        self.play(FadeOut(thats_vector_text))
        
        addition_text = Text("We can add them, scaling their impact by stretching or shrinking.", 
                           font_size=36)
        addition_text.move_to(UP * 2.5)
        
        # Show vector addition
        v1 = Arrow(start=ORIGIN, end=RIGHT * 2, color=BLUE, buff=0)
        v2 = Arrow(start=RIGHT * 2, end=RIGHT * 2 + UP * 1.5, color=GREEN, buff=0)
        v_sum = Arrow(start=ORIGIN, end=RIGHT * 2 + UP * 1.5, color=PURPLE, buff=0)
        v_sum.set_stroke(width=6)
        
        v1_label = Text("v1", font_size=24).next_to(v1, DOWN)
        v2_label = Text("v2", font_size=24).next_to(v2, RIGHT)
        sum_label = Text("v1 + v2", font_size=24).next_to(v_sum, LEFT)
        
        # Show scaling example
        scaled_vector = Arrow(start=LEFT * 3, end=LEFT * 1, color=RED, buff=0)
        original_vector = Arrow(start=LEFT * 3, end=LEFT * 0.5, color=RED_A, buff=0)
        scale_label = Text("2×", font_size=24).next_to(scaled_vector, UP)
        
        self.play(Write(addition_text))
        self.play(Create(v1), Write(v1_label))
        self.play(Create(v2), Write(v2_label))
        self.play(Create(v_sum), Write(sum_label))
        self.play(Create(original_vector), Create(scaled_vector), Write(scale_label))
        self.wait(2)
        
        # Clear addition visuals
        self.play(FadeOut(VGroup(v1, v2, v_sum, v1_label, v2_label, sum_label, 
                                scaled_vector, original_vector, scale_label)))
        
        # [0:20] - Subtraction
        subtraction_text = Text("Subtraction? It's just adding the opposite direction.", 
                               font_size=36)
        subtraction_text.move_to(UP * 1)
        
        # Show vector subtraction
        vec_a = Arrow(start=LEFT * 1, end=RIGHT * 1, color=BLUE, buff=0)
        vec_b = Arrow(start=ORIGIN, end=UP * 1.5, color=GREEN, buff=0)
        vec_b_opposite = Arrow(start=RIGHT * 1, end=RIGHT * 1 + DOWN * 1.5, color=RED, buff=0)
        vec_diff = Arrow(start=LEFT * 1, end=RIGHT * 1 + DOWN * 1.5, color=PURPLE, buff=0)
        
        a_label = Text("a", font_size=24).next_to(vec_a, DOWN)
        b_label = Text("b", font_size=24).next_to(vec_b, LEFT)
        neg_b_label = Text("-b", font_size=24).next_to(vec_b_opposite, RIGHT)
        diff_label = Text("a - b", font_size=24).next_to(vec_diff, DOWN)
        
        self.play(FadeOut(addition_text))
        self.play(Write(subtraction_text))
        self.play(Create(vec_a), Write(a_label))
        self.play(Create(vec_b), Write(b_label))
        self.play(Create(vec_b_opposite), Write(neg_b_label))
        self.play(Create(vec_diff), Write(diff_label))
        self.wait(2)
        
        # [0:25] - Final message
        self.play(FadeOut(VGroup(subtraction_text, vec_a, vec_b, vec_b_opposite, vec_diff,
                                a_label, b_label, neg_b_label, diff_label)))
        
        final_text = Text("See how these seemingly simple ideas unlock a powerful language\nfor describing movement, forces, and much more?", 
                         font_size=36, line_spacing=1.2)
        
        self.play(Write(final_text))
        self.wait(3)
        
        # Clear everything at the end
        self.play(FadeOut(final_text))
