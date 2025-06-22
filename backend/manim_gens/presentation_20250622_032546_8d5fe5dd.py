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

class VectorNavigationScene(Scene):
    def construct(self):
        # [0:00-0:05] Imagine trying to navigate a city with only a compass.
        city_text = Text("Imagine trying to navigate a city with only a compass.", font_size=36)
        compass = Circle(radius=1, color=WHITE).shift(DOWN*0.5)
        compass_needle = Line(ORIGIN, UP*0.8, color=RED, stroke_width=4).shift(DOWN*0.5)
        compass_group = VGroup(compass, compass_needle)
        
        self.play(Write(city_text))
        self.play(Create(compass_group))
        self.wait(2)
        
        # [0:05] You know the direction, but not the distance.
        self.play(FadeOut(city_text, compass_group))
        direction_text = Text("You know the direction, but not the distance.", font_size=36)
        direction_arrow = Arrow(ORIGIN, RIGHT*2, color=BLUE, stroke_width=4)
        question_marks = VGroup(
            Text("?", font_size=48, color=YELLOW).shift(UP*0.5),
            Text("?", font_size=48, color=YELLOW).shift(DOWN*0.5)
        )
        
        self.play(Write(direction_text))
        self.play(Create(direction_arrow))
        self.play(Write(question_marks))
        self.wait(2)
        
        # [0:10] Now, imagine vectors.
        self.play(FadeOut(direction_text, direction_arrow, question_marks))
        vectors_text = Text("Now, imagine vectors.", font_size=36)
        self.play(Write(vectors_text))
        self.wait(2)
        
        # [0:15] They're like compass readings with a scale – direction *and* magnitude.
        self.play(FadeOut(vectors_text))
        compass_scale_text = Text("They're like compass readings with a scale – direction *and* magnitude.", font_size=32)
        vector_example = Arrow(ORIGIN, RIGHT*3 + UP*1.5, color=GREEN, stroke_width=6, buff=0)
        direction_label = Text("direction", font_size=24, color=BLUE).next_to(vector_example, UP)
        magnitude_label = Text("magnitude", font_size=24, color=RED).next_to(vector_example, DOWN)
        
        self.play(Write(compass_scale_text))
        self.play(Create(vector_example))
        self.play(Write(direction_label), Write(magnitude_label))
        self.wait(2)
        
        # [0:20] We can visually represent them as arrows.
        self.play(FadeOut(compass_scale_text, vector_example, direction_label, magnitude_label))
        arrows_text = Text("We can visually represent them as arrows.", font_size=36)
        arrow1 = Arrow(LEFT*2, RIGHT*1, color=BLUE, stroke_width=4, buff=0)
        arrow2 = Arrow(ORIGIN, UP*2, color=RED, stroke_width=4, buff=0)
        arrow3 = Arrow(RIGHT*1.5, RIGHT*3 + DOWN*1, color=YELLOW, stroke_width=4, buff=0)
        arrows_group = VGroup(arrow1, arrow2, arrow3)
        
        self.play(Write(arrows_text))
        self.play(Create(arrows_group))
        self.wait(2)
        
        # [0:25] Adding vectors? Just chain the arrows end-to-end.
        self.play(FadeOut(arrows_text, arrows_group))
        adding_text = Text("Adding vectors? Just chain the arrows end-to-end.", font_size=32)
        
        # Create two vectors to add
        vector_a = Arrow(LEFT*2, LEFT*2 + RIGHT*2, color=BLUE, stroke_width=6, buff=0)
        vector_b = Arrow(LEFT*2 + RIGHT*2, LEFT*2 + RIGHT*2 + UP*1.5, color=RED, stroke_width=6, buff=0)
        
        self.play(Write(adding_text))
        self.play(Create(vector_a))
        self.play(Create(vector_b))
        self.wait(2)
        
        # [0:30] The final arrow from start to finish is the sum – the resultant vector.
        self.play(FadeOut(adding_text))
        resultant_text = Text("The final arrow from start to finish is the sum – the resultant vector.", font_size=28)
        resultant_vector = Arrow(LEFT*2, LEFT*2 + RIGHT*2 + UP*1.5, color=GREEN, stroke_width=8, buff=0)
        
        self.play(Write(resultant_text))
        self.play(Create(resultant_vector))
        self.wait(2)
        
        # [0:35] Suddenly, navigation becomes precise, powerful.
        self.play(FadeOut(resultant_text, vector_a, vector_b, resultant_vector))
        final_text = Text("Suddenly, navigation becomes precise, powerful.", font_size=36)
        self.play(Write(final_text))
        self.wait(2)
        
        self.play(FadeOut(final_text))
