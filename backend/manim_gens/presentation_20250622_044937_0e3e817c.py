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

class FunctionScene(Scene):
    def construct(self):
        # [0:00] Imagine a machine: you input something, it outputs something else. That's a function,
        machine_text = Text("Imagine a machine: you input something, it outputs something else. That's a function,", 
                           font_size=36).to_edge(UP)
        
        # Visual representation of a machine
        input_box = Rectangle(width=1.5, height=1, color=BLUE).shift(LEFT * 3)
        machine_box = Rectangle(width=2, height=1.5, color=GREEN).shift(ORIGIN)
        output_box = Rectangle(width=1.5, height=1, color=RED).shift(RIGHT * 3)
        
        input_label = Text("INPUT", font_size=24, color=WHITE).move_to(input_box.get_center())
        machine_label = Text("MACHINE", font_size=20, color=WHITE).move_to(machine_box.get_center())
        output_label = Text("OUTPUT", font_size=24, color=WHITE).move_to(output_box.get_center())
        
        arrow1 = Arrow(input_box.get_right(), machine_box.get_left(), color=WHITE)
        arrow2 = Arrow(machine_box.get_right(), output_box.get_left(), color=WHITE)
        
        self.play(Write(machine_text))
        self.play(Create(input_box), Create(machine_box), Create(output_box))
        self.play(Write(input_label), Write(machine_label), Write(output_label))
        self.play(Create(arrow1), Create(arrow2))
        self.wait(1)
        
        # [0:05] a relationship mapping inputs to outputs.
        self.play(FadeOut(machine_text))
        relationship_text = Text("a relationship mapping inputs to outputs.", font_size=36).to_edge(UP)
        self.play(Write(relationship_text))
        self.wait(2)
        
        # [0:10] Think of squaring a number; input 3, output 9.
        self.play(FadeOut(relationship_text))
        self.play(FadeOut(input_box), FadeOut(machine_box), FadeOut(output_box),
                 FadeOut(input_label), FadeOut(machine_label), FadeOut(output_label),
                 FadeOut(arrow1), FadeOut(arrow2))
        
        squaring_text = Text("Think of squaring a number; input 3, output 9.", font_size=36).to_edge(UP)
        
        # Visual for squaring function
        input_3 = Text("3", font_size=48, color=BLUE).shift(LEFT * 3)
        square_symbol = Text("x²", font_size=48, color=GREEN).shift(ORIGIN)
        output_9 = Text("9", font_size=48, color=RED).shift(RIGHT * 3)
        
        arrow_sq1 = Arrow(input_3.get_right() + RIGHT * 0.3, square_symbol.get_left() + LEFT * 0.3, color=WHITE)
        arrow_sq2 = Arrow(square_symbol.get_right() + RIGHT * 0.3, output_9.get_left() + LEFT * 0.3, color=WHITE)
        
        self.play(Write(squaring_text))
        self.play(Write(input_3), Write(square_symbol), Write(output_9))
        self.play(Create(arrow_sq1), Create(arrow_sq2))
        self.wait(2)
        
        # [0:15] But functions aren't just about numbers;
        self.play(FadeOut(squaring_text))
        self.play(FadeOut(input_3), FadeOut(square_symbol), FadeOut(output_9),
                 FadeOut(arrow_sq1), FadeOut(arrow_sq2))
        
        not_numbers_text = Text("But functions aren't just about numbers;", font_size=36).to_edge(UP)
        self.play(Write(not_numbers_text))
        self.wait(2)
        
        # [0:20] they can describe any transformation.
        self.play(FadeOut(not_numbers_text))
        transformation_text = Text("they can describe any transformation.", font_size=36).to_edge(UP)
        
        # Visual for transformation - shape morphing
        circle = Circle(radius=1, color=BLUE).shift(LEFT * 2)
        arrow_transform = Arrow(LEFT * 0.5, RIGHT * 0.5, color=WHITE)
        square = Square(side_length=1.5, color=RED).shift(RIGHT * 2)
        
        self.play(Write(transformation_text))
        self.play(Create(circle), Create(arrow_transform), Create(square))
        self.wait(2)
        
        # [0:25] A function guarantees a single output for each input,
        self.play(FadeOut(transformation_text))
        self.play(FadeOut(circle), FadeOut(arrow_transform), FadeOut(square))
        
        guarantee_text = Text("A function guarantees a single output for each input,", font_size=36).to_edge(UP)
        
        # Visual showing one-to-one mapping
        inputs = VGroup(*[Text(str(i), font_size=32, color=BLUE).shift(LEFT * 3 + UP * (1-i) * 0.8) for i in range(3)])
        outputs = VGroup(*[Text(str(i**2), font_size=32, color=RED).shift(RIGHT * 3 + UP * (1-i) * 0.8) for i in range(3)])
        arrows_map = VGroup(*[Arrow(inputs[i].get_right() + RIGHT * 0.2, outputs[i].get_left() + LEFT * 0.2, color=WHITE) for i in range(3)])
        
        self.play(Write(guarantee_text))
        self.play(Write(inputs), Write(outputs))
        self.play(Create(arrows_map))
        self.wait(2)
        
        # [0:30] ensuring predictability and structure—the cornerstone of much of mathematics.
        self.play(FadeOut(guarantee_text))
        self.play(FadeOut(inputs), FadeOut(outputs), FadeOut(arrows_map))
        
        cornerstone_text = Text("ensuring predictability and structure—the cornerstone of much of mathematics.", 
                               font_size=36).to_edge(UP)
        self.play(Write(cornerstone_text))
        self.wait(2)
        
        # We'll explore how their properties shape our understanding of the world.
        self.play(FadeOut(cornerstone_text))
        final_text = Text("We'll explore how their properties shape our understanding of the world.", 
                         font_size=36).to_edge(UP)
        self.play(Write(final_text))
        self.wait(2)
        
        self.play(FadeOut(final_text))
