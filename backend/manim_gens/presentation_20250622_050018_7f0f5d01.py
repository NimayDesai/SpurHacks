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

class FunctionIntroduction(Scene):
    def construct(self):
        # Opening: Imagine a machine
        title = Text("Imagine a machine.", font_size=48)
        self.play(Write(title))
        self.wait(1)
        
        # Create machine visual
        machine_box = Rectangle(width=4, height=2, color=BLUE, stroke_width=3)
        machine_label = Text("MACHINE", font_size=24, color=WHITE)
        machine_group = VGroup(machine_box, machine_label)
        
        # Input arrow and label
        input_arrow = Arrow(start=LEFT*3, end=LEFT*1, color=GREEN, stroke_width=4)
        input_label = Text("INPUT", font_size=20, color=GREEN).next_to(input_arrow, UP)
        
        # Output arrow and label
        output_arrow = Arrow(start=RIGHT*1, end=RIGHT*3, color=RED, stroke_width=4)
        output_label = Text("OUTPUT", font_size=20, color=RED).next_to(output_arrow, UP)
        
        machine_diagram = VGroup(machine_group, input_arrow, input_label, output_arrow, output_label)
        
        self.play(FadeOut(title))
        self.play(FadeIn(machine_diagram))
        
        # Add process text
        process_text = Text("You feed it an input, it processes, and spits out an output.", 
                          font_size=32).to_edge(DOWN)
        self.play(Write(process_text))
        self.wait(0.5)
        
        # [0:05] timestamp
        self.play(FadeOut(process_text))
        
        # That's essentially what a function is
        function_text = Text("That's essentially what a function is:", font_size=36)
        transform_text = Text("a process that transforms something.", font_size=36)
        function_group = VGroup(function_text, transform_text).arrange(DOWN, buff=0.3)
        
        self.play(FadeOut(machine_diagram))
        self.play(Write(function_group))
        self.wait(1)
        
        # [0:10] timestamp
        self.play(FadeOut(function_group))
        
        # Arrow mapping visualization
        arrow_text = Text("We often visualize this with arrows,", font_size=32)
        mapping_text = Text("mapping inputs to outputs.", font_size=32)
        arrow_group = VGroup(arrow_text, mapping_text).arrange(DOWN, buff=0.3).to_edge(UP)
        
        self.play(Write(arrow_group))
        
        # Create mapping diagram
        inputs = VGroup(
            Text("1", font_size=28),
            Text("2", font_size=28),
            Text("3", font_size=28)
        ).arrange(DOWN, buff=0.5).shift(LEFT*3)
        
        outputs = VGroup(
            Text("2", font_size=28),
            Text("4", font_size=28),
            Text("6", font_size=28)
        ).arrange(DOWN, buff=0.5).shift(RIGHT*3)
        
        arrows = VGroup(
            Arrow(inputs[0].get_right(), outputs[0].get_left(), color=YELLOW),
            Arrow(inputs[1].get_right(), outputs[1].get_left(), color=YELLOW),
            Arrow(inputs[2].get_right(), outputs[2].get_left(), color=YELLOW)
        )
        
        mapping_diagram = VGroup(inputs, outputs, arrows)
        
        self.play(FadeIn(mapping_diagram))
        self.wait(1)
        
        # Key is the rule
        rule_text = Text("But the key is the *rule* – the consistent process", font_size=30)
        connecting_text = Text("connecting input and output.", font_size=30)
        rule_group = VGroup(rule_text, connecting_text).arrange(DOWN, buff=0.2).to_edge(DOWN)
        
        self.play(Write(rule_group))
        self.wait(2)
        
        # [0:18] timestamp
        self.play(FadeOut(arrow_group), FadeOut(mapping_diagram), FadeOut(rule_group))
        
        # Recipe analogy
        recipe_title = Text("Think of it like a recipe:", font_size=40)
        self.play(Write(recipe_title))
        self.wait(1)
        
        # Recipe components
        ingredients_text = Text("the ingredients are your inputs,", font_size=32, color=GREEN)
        cake_text = Text("the cake is your output,", font_size=32, color=RED)
        recipe_function_text = Text("and the recipe itself is the function.", font_size=32, color=BLUE)
        
        recipe_group = VGroup(ingredients_text, cake_text, recipe_function_text).arrange(DOWN, buff=0.4)
        
        self.play(FadeOut(recipe_title))
        self.play(Write(recipe_group))
        self.wait(2)
        
        # [0:28] timestamp
        self.play(FadeOut(recipe_group))
        
        # Final understanding message
        understanding_text = Text("Understanding this core idea unlocks", font_size=36)
        possibilities_text = Text("a whole world of mathematical possibilities.", font_size=36)
        final_group = VGroup(understanding_text, possibilities_text).arrange(DOWN, buff=0.3)
        
        self.play(Write(final_group))
        self.wait(3)
        
        # Final fadeout
        self.play(FadeOut(final_group))
        self.wait(1)
