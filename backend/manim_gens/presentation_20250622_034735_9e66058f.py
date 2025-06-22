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

class AlgebraScript(Scene):
    def construct(self):
        # [0:00-0:05] Opening statement
        opening_text = Text("Algebra: it's not just about solving for x.", font_size=36)
        self.play(Write(opening_text))
        self.wait(1)
        
        # [0:05] Clear and introduce next concept
        self.play(FadeOut(opening_text))
        
        language_text = Text("Think of it as a language for describing relationships.", font_size=32)
        self.play(Write(language_text))
        self.wait(2)
        
        # Add visual of symbols replacing numbers
        symbols_text = Text("We replace numbers with symbols, allowing us to talk about", font_size=28)
        patterns_text = Text("patterns and properties that hold true no matter", font_size=28)
        specific_text = Text("the specific numbers involved.", font_size=28)
        
        symbols_group = VGroup(symbols_text, patterns_text, specific_text).arrange(DOWN, buff=0.3)
        
        self.play(
            FadeOut(language_text),
            Write(symbols_group)
        )
        self.wait(3)
        
        # [0:15] Clear and show equation example
        self.play(FadeOut(symbols_group))
        
        see_text = Text("See how this simple equation,", font_size=32).to_edge(UP)
        equation_text = Text("y = 2x", font_size=48, color=YELLOW)
        
        self.play(Write(see_text))
        self.play(Write(equation_text))
        self.wait(1)
        
        # Add explanation about the equation
        not_just_text = Text("isn't just about finding y when x is 3, but describes", font_size=28)
        family_text = Text("a whole family of points, a line even?", font_size=28)
        explanation_group = VGroup(not_just_text, family_text).arrange(DOWN, buff=0.3).shift(DOWN*1.5)
        
        self.play(Write(explanation_group))
        
        # Add visual representation of the line
        plane = NumberPlane(
            x_range=[-3, 3, 1],
            y_range=[-6, 6, 2],
            background_line_style={"stroke_opacity": 0.3}
        ).scale(0.4).shift(DOWN*2 + RIGHT*3)
        
        line = plane.plot(
            lambda x: 2*x,
            x_range=[-3, 3],
            color=YELLOW,
            stroke_width=3
        )
        
        self.play(Create(plane), Create(line))
        self.wait(2)
        
        # [0:25] Clear and show power statement
        self.play(FadeOut(see_text), FadeOut(equation_text), FadeOut(explanation_group), FadeOut(plane), FadeOut(line))
        
        power_text = Text("That's the power – generalizing beyond specific instances", font_size=32)
        structure_text = Text("to uncover underlying structure.", font_size=32)
        power_group = VGroup(power_text, structure_text).arrange(DOWN, buff=0.5)
        
        self.play(Write(power_group))
        self.wait(3)
        
        # [0:35] Final statement about algebra's revelations
        self.play(FadeOut(power_group))
        
        reveals_text = Text("Algebra reveals the hidden geometry in equations,", font_size=30)
        relationships_text = Text("the relationships between quantities, and lets us", font_size=30)
        solve_text = Text("solve problems far beyond what mere arithmetic could handle.", font_size=30)
        
        final_group = VGroup(reveals_text, relationships_text, solve_text).arrange(DOWN, buff=0.4)
        
        self.play(Write(final_group))
        self.wait(3)
        
        # Final clear
        self.play(FadeOut(final_group))
        self.wait(1)
