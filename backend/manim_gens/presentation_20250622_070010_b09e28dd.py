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

class FunctionExplanation(Scene):
    def construct(self):
        # [0:00-0:05] "What is a function?"
        title = Text("What is a function?", font_size=48)
        self.play(Write(title))
        self.wait(5)
        
        # [0:05] Clear title and introduce machine concept
        self.play(FadeOut(title))
        
        # [0:05-0:15] "It's a machine, really. You feed it an input, it follows a set of rules, and spits out an output."
        machine_text = Text("It's a machine, really.", font_size=36)
        machine_text.move_to(UP * 2)
        self.play(Write(machine_text))
        
        # Visual machine representation
        machine_box = RoundedRectangle(
            width=4, height=2, 
            corner_radius=0.2, 
            color=BLUE, 
            stroke_width=3
        )
        machine_label = Text("FUNCTION", font_size=24, color=WHITE)
        machine_label.move_to(machine_box.get_center())
        
        # Input arrow and label
        input_arrow = Arrow(LEFT * 3, LEFT * 0.5, color=GREEN, stroke_width=4)
        input_text = Text("Input", font_size=24, color=GREEN)
        input_text.next_to(input_arrow, UP)
        
        # Output arrow and label
        output_arrow = Arrow(RIGHT * 0.5, RIGHT * 3, color=RED, stroke_width=4)
        output_text = Text("Output", font_size=24, color=RED)
        output_text.next_to(output_arrow, UP)
        
        machine_group = VGroup(machine_box, machine_label)
        
        self.play(Create(machine_group))
        self.play(Create(input_arrow), Write(input_text))
        
        process_text = Text("You feed it an input, it follows a set of rules,", font_size=28)
        process_text.move_to(DOWN * 1.5)
        self.play(Write(process_text))
        
        self.play(Create(output_arrow), Write(output_text))
        output_text2 = Text("and spits out an output.", font_size=28)
        output_text2.move_to(DOWN * 2.5)
        self.play(Write(output_text2))
        
        self.wait(1)
        
        # [0:15] Clear previous content
        self.play(FadeOut(VGroup(
            machine_text, machine_group, input_arrow, input_text, 
            output_arrow, output_text, process_text, output_text2
        )))
        
        # [0:15-0:20] "Think of a simple recipe: ingredients in, cake out."
        recipe_text = Text("Think of a simple recipe:", font_size=36)
        recipe_text.move_to(UP * 1.5)
        self.play(Write(recipe_text))
        
        # Recipe visualization
        ingredients_text = Text("Ingredients", font_size=28, color=GREEN)
        ingredients_text.move_to(LEFT * 3)
        
        recipe_box = RoundedRectangle(
            width=3, height=1.5, 
            corner_radius=0.2, 
            color=BLUE, 
            stroke_width=3
        )
        recipe_label = Text("RECIPE", font_size=20, color=WHITE)
        recipe_label.move_to(recipe_box.get_center())
        
        cake_text = Text("Cake", font_size=28, color=RED)
        cake_text.move_to(RIGHT * 3)
        
        recipe_arrow1 = Arrow(LEFT * 1.8, LEFT * 0.3, color=YELLOW, stroke_width=3)
        recipe_arrow2 = Arrow(RIGHT * 0.3, RIGHT * 1.8, color=YELLOW, stroke_width=3)
        
        in_out_text = Text("ingredients in, cake out.", font_size=32)
        in_out_text.move_to(DOWN * 1.5)
        
        self.play(Write(ingredients_text))
        self.play(Create(recipe_box), Write(recipe_label))
        self.play(Create(recipe_arrow1), Create(recipe_arrow2))
        self.play(Write(cake_text))
        self.play(Write(in_out_text))
        
        self.wait(5)
        
        # [0:20] Clear recipe content
        self.play(FadeOut(VGroup(
            recipe_text, ingredients_text, recipe_box, recipe_label,
            cake_text, recipe_arrow1, recipe_arrow2, in_out_text
        )))
        
        # [0:20-0:25] "The rules define the relationship between input and output – a mapping."
        rules_text = Text("The rules define the relationship", font_size=36)
        rules_text.move_to(UP * 1)
        self.play(Write(rules_text))
        
        relationship_text = Text("between input and output – a mapping.", font_size=36)
        relationship_text.move_to(DOWN * 0.5)
        self.play(Write(relationship_text))
        
        self.wait(5)
        
        # [0:25] Clear rules text
        self.play(FadeOut(VGroup(rules_text, relationship_text)))
        
        # [0:25-0:30] "We can visualize this mapping;"
        visualize_text = Text("We can visualize this mapping;", font_size=36)
        self.play(Write(visualize_text))
        
        self.wait(5)
        
        # [0:30] Clear and show visualization
        self.play(FadeOut(visualize_text))
        
        # [0:30-0:35] "it's not just about the answer, but the process, the transformation itself."
        # Create a coordinate plane and function graph
        plane = NumberPlane(
            x_range=[-4, 4, 1],
            y_range=[-3, 3, 1],
            background_line_style={"stroke_color": GRAY, "stroke_width": 1}
        )
        
        # Simple function curve
        def func(x):
            return 0.3 * x**2 - 1
            
        curve = plane.plot(
            func,
            x_range=[-3, 3],
            color=YELLOW,
            stroke_width=4
        )
        
        self.play(Create(plane))
        self.play(Create(curve))
        
        process_focus_text = Text("it's not just about the answer,", font_size=28)
        process_focus_text.move_to(UP * 3)
        self.play(Write(process_focus_text))
        
        transformation_text = Text("but the process, the transformation itself.", font_size=28)
        transformation_text.move_to(UP * 2.5)
        self.play(Write(transformation_text))
        
        self.wait(5)
        
        # [0:35] Clear visualization content
        self.play(FadeOut(VGroup(plane, curve, process_focus_text, transformation_text)))
        
        # [0:35-end] "That's the essence of a function: a consistent, predictable transformation."
        essence_text1 = Text("That's the essence of a function:", font_size=36)
        essence_text1.move_to(UP * 0.5)
        self.play(Write(essence_text1))
        
        essence_text2 = Text("a consistent, predictable transformation.", font_size=36)
        essence_text2.move_to(DOWN * 0.5)
        self.play(Write(essence_text2))
        
        self.wait(3)
        
        # Final fadeout
        self.play(FadeOut(VGroup(essence_text1, essence_text2)))
