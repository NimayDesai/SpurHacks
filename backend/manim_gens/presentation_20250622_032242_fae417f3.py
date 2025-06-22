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
        # Opening text
        opening_text = Text("Algebra's core idea?  Replacing numbers with symbols.", 
                          font_size=36, color=WHITE)
        self.play(Write(opening_text))
        self.wait(5)
        
        # Clear and show puzzle concept
        self.play(FadeOut(opening_text))
        puzzle_text = Text("Think of it like a puzzle where letters stand in for unknown quantities.", 
                          font_size=36, color=WHITE)
        
        # Show visual representation of puzzle
        number_equation = MathTex("5 + 3 = 8", font_size=48, color=BLUE)
        arrow = Arrow(LEFT, RIGHT, color=YELLOW)
        symbol_equation = MathTex("x + 3 = 8", font_size=48, color=GREEN)
        
        puzzle_group = VGroup(number_equation, arrow, symbol_equation).arrange(RIGHT, buff=1)
        
        self.play(Write(puzzle_text))
        self.wait(1)
        puzzle_text.animate.shift(UP * 1.5)
        self.play(puzzle_text.animate.shift(UP * 1.5))
        self.play(Write(number_equation))
        self.play(GrowArrow(arrow))
        self.play(Write(symbol_equation))
        self.wait(5)
        
        # Clear and show rules
        self.play(FadeOut(puzzle_text), FadeOut(puzzle_group))
        rules_text = Text("We use rules – like adding the same thing to both sides –\nto manipulate these symbols and solve for the unknowns.", 
                         font_size=32, color=WHITE)
        
        # Show rule demonstration
        equation1 = MathTex("x + 3 = 8", font_size=40, color=WHITE)
        equation2 = MathTex("x + 3 - 3 = 8 - 3", font_size=40, color=YELLOW)
        equation3 = MathTex("x = 5", font_size=40, color=GREEN)
        
        equation_group = VGroup(equation1, equation2, equation3).arrange(DOWN, buff=0.8)
        
        self.play(Write(rules_text))
        self.wait(1)
        self.play(rules_text.animate.shift(UP * 2))
        self.play(Write(equation1))
        self.play(Transform(equation1.copy(), equation2))
        self.play(Write(equation2))
        self.play(Transform(equation2.copy(), equation3))
        self.play(Write(equation3))
        self.wait(5)
        
        # Clear and show relationships
        self.play(FadeOut(rules_text), FadeOut(equation_group))
        relationships_text = Text("It's about uncovering relationships between numbers,\nnot just calculating answers.", 
                                font_size=36, color=WHITE)
        
        # Show relationship visual
        plane = NumberPlane(x_range=[-3, 3], y_range=[-3, 3], 
                          background_line_style={"stroke_opacity": 0.3})
        line = plane.plot(lambda x: 2*x + 1, x_range=[-2, 2], color=RED, stroke_width=4)
        line_label = MathTex("y = 2x + 1", color=RED).next_to(line, UP)
        
        self.play(Write(relationships_text))
        self.wait(1)
        self.play(relationships_text.animate.shift(UP * 2.5))
        self.play(Create(plane))
        self.play(Create(line))
        self.play(Write(line_label))
        self.wait(5)
        
        # Clear and show generalization
        self.play(FadeOut(relationships_text), FadeOut(plane), FadeOut(line), FadeOut(line_label))
        generalize_text = Text("This allows us to generalize patterns, to find the solution\nfor any number, not just a specific one.", 
                              font_size=32, color=WHITE)
        
        # Show generalization visual
        specific = MathTex("3^2 = 9", font_size=36, color=BLUE)
        general = MathTex("x^2 = x \\cdot x", font_size=36, color=GREEN)
        pattern = MathTex("(a + b)^2 = a^2 + 2ab + b^2", font_size=36, color=PURPLE)
        
        math_group = VGroup(specific, general, pattern).arrange(DOWN, buff=1)
        
        self.play(Write(generalize_text))
        self.wait(1)
        self.play(generalize_text.animate.shift(UP * 2))
        self.play(Write(specific))
        self.play(Write(general))
        self.play(Write(pattern))
        self.wait(5)
        
        # Clear and show final message
        self.play(FadeOut(generalize_text), FadeOut(math_group))
        final_text = Text("See how this simple shift unlocks\na whole new world of mathematical power?", 
                         font_size=36, color=GOLD)
        
        # Show power visual - mathematical symbols radiating outward
        symbols = VGroup(
            MathTex("x", color=RED),
            MathTex("y", color=GREEN),
            MathTex("z", color=BLUE),
            MathTex("a", color=YELLOW),
            MathTex("b", color=PURPLE),
            MathTex("c", color=PINK)
        )
        
        for i, symbol in enumerate(symbols):
            angle = i * 60 * DEGREES
            symbol.move_to(2 * np.array([np.cos(angle), np.sin(angle), 0]))
        
        self.play(Write(final_text))
        self.wait(1)
        self.play(final_text.animate.shift(UP * 1.5))
        
        for symbol in symbols:
            self.play(Write(symbol), run_time=0.3)
        
        # Animate symbols expanding outward
        self.play(*[symbol.animate.scale(1.5).set_opacity(0.7) for symbol in symbols])
        self.wait(5)
        
        # Final fadeout
        self.play(FadeOut(final_text), FadeOut(symbols))
