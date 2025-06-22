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

class LimitConcept(Scene):
    def construct(self):
        # [0:00] - Initial question
        title = Text("What does it mean for a function to have a limit?", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(5)
        
        # [0:05] - Intuitive explanation
        self.play(FadeOut(title))
        intuitive_text = Text("Intuitively, it's about approaching a specific value.", font_size=28)
        self.play(Write(intuitive_text))
        self.wait(5)
        
        # [0:10] - Walking metaphor with visual
        self.play(FadeOut(intuitive_text))
        walking_text = Text("Imagine walking along a path towards a point.", font_size=28)
        self.play(Write(walking_text))
        
        # Create a visual path
        path = Line(LEFT * 4, RIGHT * 2, color=BLUE, stroke_width=4)
        target_point = Dot(RIGHT * 2, color=RED, radius=0.1)
        walker = Dot(LEFT * 4, color=GREEN, radius=0.08)
        
        self.play(Create(path), Create(target_point), Create(walker))
        self.play(walker.animate.move_to(RIGHT * 1.5), rate_func=smooth, run_time=2)
        self.wait(3)
        
        # [0:15] - Never quite reaching
        self.play(FadeOut(walking_text), FadeOut(path), FadeOut(target_point), FadeOut(walker))
        close_text = Text("Even if you never quite reach it, if you can get", font_size=28).shift(UP * 0.5)
        close_text2 = Text("arbitrarily close, we say the limit exists.", font_size=28).shift(DOWN * 0.5)
        self.play(Write(close_text))
        self.play(Write(close_text2))
        self.wait(10)
        
        # [0:25] - Mathematical definition
        self.play(FadeOut(close_text), FadeOut(close_text2))
        math_text = Text("Mathematically, this means we can make the output", font_size=24).shift(UP * 0.7)
        math_text2 = Text("as close to the limit as we want, by choosing", font_size=24).shift(UP * 0.2)
        math_text3 = Text("inputs sufficiently near the point in question.", font_size=24).shift(DOWN * 0.3)
        
        self.play(Write(math_text))
        self.play(Write(math_text2))
        self.play(Write(math_text3))
        self.wait(5)
        
        # [0:30] - Essence of limit
        self.play(FadeOut(math_text), FadeOut(math_text2), FadeOut(math_text3))
        essence_text = Text("That's the essence of a limit: getting arbitrarily close.", font_size=28)
        self.play(Write(essence_text))
        self.wait(5)
        
        # [0:35] - Path splitting scenario
        self.play(FadeOut(essence_text))
        split_text = Text("But what if the path splits? Then the limit might not exist.", font_size=28)
        self.play(Write(split_text))
        
        # Visual of splitting path
        main_path = Line(LEFT * 3, ORIGIN, color=BLUE, stroke_width=4)
        upper_path = Line(ORIGIN, RIGHT * 2 + UP * 1, color=BLUE, stroke_width=4)
        lower_path = Line(ORIGIN, RIGHT * 2 + DOWN * 1, color=BLUE, stroke_width=4)
        
        self.play(Create(main_path))
        self.play(Create(upper_path), Create(lower_path))
        self.wait(5)
        
        # Final statement
        self.play(FadeOut(split_text), FadeOut(main_path), FadeOut(upper_path), FadeOut(lower_path))
        final_text = Text("This idea underlies much of calculus.", font_size=28)
        self.play(Write(final_text))
        self.wait(2)
        
        self.play(FadeOut(final_text))
