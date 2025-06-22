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

class AlgebraCore(Scene):
    def construct(self):
        # [0:00] - Opening text
        opening_text = Text("Algebra's core idea?", font_size=48)
        self.play(Write(opening_text))
        self.wait(1)
        
        # [0:05] - First main concept
        self.play(FadeOut(opening_text))
        
        concept1 = Text("Replacing numbers with symbols,", font_size=36)
        concept1.to_edge(UP)
        self.play(Write(concept1))
        
        # Visual: Numbers transforming to symbols
        numbers = VGroup(
            Text("5", font_size=40, color=BLUE),
            Text("3", font_size=40, color=BLUE),
            Text("8", font_size=40, color=BLUE)
        ).arrange(RIGHT, buff=1)
        
        symbols = VGroup(
            Text("x", font_size=40, color=RED),
            Text("y", font_size=40, color=RED),
            Text("z", font_size=40, color=RED)
        ).arrange(RIGHT, buff=1)
        
        self.play(Write(numbers))
        self.wait(0.5)
        self.play(Transform(numbers, symbols))
        self.wait(2)
        
        concept2 = Text("allowing us to talk about relationships, not just specific values.", 
                       font_size=32)
        concept2.next_to(concept1, DOWN, buff=0.5)
        self.play(Write(concept2))
        self.wait(2)
        
        # [0:15] - Recipe analogy
        self.play(FadeOut(VGroup(concept1, concept2, numbers)))
        
        recipe_intro = Text("Think of it like a recipe:", font_size=36)
        recipe_intro.to_edge(UP)
        self.play(Write(recipe_intro))
        
        specific_recipe = Text("instead of \"2 cups flour, 1 cup sugar,\"", font_size=32)
        specific_recipe.next_to(recipe_intro, DOWN, buff=0.5)
        self.play(Write(specific_recipe))
        
        general_recipe = Text("we'd say \"x cups flour, y cups sugar.\"", font_size=32)
        general_recipe.next_to(specific_recipe, DOWN, buff=0.5)
        self.play(Write(general_recipe))
        self.wait(5)
        
        # [0:25] - Exploration concept
        self.play(FadeOut(VGroup(recipe_intro, specific_recipe, general_recipe)))
        
        exploration_text = Text("We can then explore how changing x and y affects the final product –", 
                               font_size=32)
        exploration_text.to_edge(UP)
        self.play(Write(exploration_text))
        
        general_rule = Text("a general rule, rather than a single instance.", font_size=32)
        general_rule.next_to(exploration_text, DOWN, buff=0.5)
        self.play(Write(general_rule))
        
        # Visual: Variables changing
        variable_demo = VGroup(
            Text("x = 1, y = 2", font_size=24, color=GREEN),
            Text("x = 3, y = 4", font_size=24, color=GREEN),
            Text("x = 5, y = 1", font_size=24, color=GREEN)
        ).arrange(DOWN, buff=0.3)
        variable_demo.next_to(general_rule, DOWN, buff=1)
        
        for var in variable_demo:
            self.play(Write(var))
            self.wait(0.5)
        
        self.wait(3)
        
        # [0:35] - Solving equations
        self.play(FadeOut(VGroup(exploration_text, general_rule, variable_demo)))
        
        solving_text = Text("Solving an equation?", font_size=36)
        solving_text.to_edge(UP)
        self.play(Write(solving_text))
        
        secret_recipe = Text("That's just uncovering the secret recipe ingredients,", font_size=32)
        secret_recipe.next_to(solving_text, DOWN, buff=0.5)
        self.play(Write(secret_recipe))
        
        values_text = Text("the values of x and y that make the relationship true.", font_size=32)
        values_text.next_to(secret_recipe, DOWN, buff=0.5)
        self.play(Write(values_text))
        
        # Visual: Simple equation
        equation = MathTex("2x + 3 = 11", font_size=48)
        equation.next_to(values_text, DOWN, buff=1)
        self.play(Write(equation))
        
        solution = MathTex("x = 4", font_size=48, color=GREEN)
        solution.next_to(equation, DOWN, buff=0.5)
        self.play(Write(solution))
        self.wait(5)
        
        # Final concept
        self.play(FadeOut(VGroup(solving_text, secret_recipe, values_text, equation, solution)))
        
        final_text = Text("It's about the underlying structure, not just the numbers themselves.", 
                         font_size=36)
        self.play(Write(final_text))
        self.wait(5)
        
        self.play(FadeOut(final_text))
