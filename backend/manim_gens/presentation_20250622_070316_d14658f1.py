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

class ParabolaScene(Scene):
    def construct(self):
        # [0:00] We all know lines, right?
        line_text = Text("We all know lines, right?", font_size=36)
        line = Line(LEFT * 3, RIGHT * 3, color=BLUE, stroke_width=4)
        
        self.play(Write(line_text))
        self.play(Create(line))
        self.wait(5)
        
        # [0:05] But what if a line bends? That's a parabola, the graph of a quadratic.
        self.play(FadeOut(line_text, line))
        
        bend_text = Text("But what if a line bends? That's a parabola, the graph of a quadratic.", font_size=30)
        bend_text.to_edge(UP)
        
        plane = NumberPlane(
            x_range=[-4, 4, 1],
            y_range=[-2, 6, 1],
            x_length=8,
            y_length=6,
            background_line_style={"stroke_opacity": 0.3}
        )
        
        parabola = plane.plot(
            lambda x: x**2,
            x_range=[-3, 3],
            color=RED,
            stroke_width=4
        )
        
        self.play(Write(bend_text))
        self.play(Create(plane))
        self.play(Create(parabola))
        self.wait(5)
        
        # [0:10] Think of it as a line's reflection, stretched or squeezed depending on its equation.
        self.play(FadeOut(bend_text))
        
        reflection_text = Text("Think of it as a line's reflection, stretched or squeezed depending on its equation.", font_size=28)
        reflection_text.to_edge(UP)
        
        stretched_parabola = plane.plot(
            lambda x: 2*x**2,
            x_range=[-2.5, 2.5],
            color=GREEN,
            stroke_width=4
        )
        
        squeezed_parabola = plane.plot(
            lambda x: 0.5*x**2,
            x_range=[-3.5, 3.5],
            color=BLUE,
            stroke_width=4
        )
        
        self.play(Write(reflection_text))
        self.play(Transform(parabola, stretched_parabola))
        self.wait(2)
        self.play(Transform(parabola, squeezed_parabola))
        self.wait(3)
        
        # [0:15] Notice how the coefficient of x² determines the parabola's steepness.
        self.play(FadeOut(reflection_text))
        
        coefficient_text = Text("Notice how the coefficient of x² determines the parabola's steepness.", font_size=28)
        coefficient_text.to_edge(UP)
        
        equation1 = Text("y = 2x²", font_size=24, color=GREEN).to_edge(LEFT).shift(UP*2)
        equation2 = Text("y = 0.5x²", font_size=24, color=BLUE).to_edge(LEFT).shift(UP*1.5)
        
        steep_parabola = plane.plot(
            lambda x: 2*x**2,
            x_range=[-2.5, 2.5],
            color=GREEN,
            stroke_width=4
        )
        
        self.play(Write(coefficient_text))
        self.play(Write(equation1), Write(equation2))
        self.play(Transform(parabola, steep_parabola))
        self.wait(5)
        
        # [0:20] And the constant term? That's its vertical shift.
        self.play(FadeOut(coefficient_text, equation1, equation2))
        
        shift_text = Text("And the constant term? That's its vertical shift.", font_size=30)
        shift_text.to_edge(UP)
        
        shifted_parabola = plane.plot(
            lambda x: x**2 + 2,
            x_range=[-3, 3],
            color=PURPLE,
            stroke_width=4
        )
        
        shift_equation = Text("y = x² + 2", font_size=24, color=PURPLE).to_edge(LEFT).shift(UP*2)
        
        self.play(Write(shift_text))
        self.play(Write(shift_equation))
        self.play(Transform(parabola, shifted_parabola))
        self.wait(5)
        
        # [0:25] The turning point, the vertex, holds a special significance – it's the minimum or maximum value.
        self.play(FadeOut(shift_text, shift_equation))
        
        vertex_text = Text("The turning point, the vertex, holds a special significance –", font_size=26)
        vertex_text2 = Text("it's the minimum or maximum value.", font_size=26)
        vertex_group = VGroup(vertex_text, vertex_text2).arrange(DOWN).to_edge(UP)
        
        original_parabola = plane.plot(
            lambda x: x**2,
            x_range=[-3, 3],
            color=RED,
            stroke_width=4
        )
        
        vertex_dot = Dot(plane.c2p(0, 0), color=YELLOW, radius=0.1)
        vertex_label = Text("Vertex (0,0)", font_size=20, color=YELLOW).next_to(vertex_dot, UP)
        
        self.play(Write(vertex_group))
        self.play(Transform(parabola, original_parabola))
        self.play(Create(vertex_dot), Write(vertex_label))
        self.wait(5)
        
        # [0:30] Finally, the roots? Those are where the parabola kisses the x-axis.
        self.play(FadeOut(vertex_group))
        
        roots_text = Text("Finally, the roots? Those are where the parabola kisses the x-axis.", font_size=28)
        roots_text.to_edge(UP)
        
        roots_parabola = plane.plot(
            lambda x: x**2 - 4,
            x_range=[-3, 3],
            color=ORANGE,
            stroke_width=4
        )
        
        root1 = Dot(plane.c2p(-2, 0), color=GREEN, radius=0.08)
        root2 = Dot(plane.c2p(2, 0), color=GREEN, radius=0.08)
        root_label1 = Text("(-2,0)", font_size=18, color=GREEN).next_to(root1, DOWN)
        root_label2 = Text("(2,0)", font_size=18, color=GREEN).next_to(root2, DOWN)
        
        self.play(Write(roots_text))
        self.play(Transform(parabola, roots_parabola))
        self.play(FadeOut(vertex_dot, vertex_label))
        self.play(Create(root1), Create(root2))
        self.play(Write(root_label1), Write(root_label2))
        self.wait(5)
        
        # [0:35] It's all interconnected, a beautiful dance of numbers and shapes.
        self.play(FadeOut(roots_text))
        
        final_text = Text("It's all interconnected, a beautiful dance of numbers and shapes.", font_size=30)
        final_text.to_edge(UP)
        
        self.play(Write(final_text))
        self.wait(3)
        
        # Clear everything at the end
        self.play(FadeOut(final_text, parabola, plane, root1, root2, root_label1, root_label2))
