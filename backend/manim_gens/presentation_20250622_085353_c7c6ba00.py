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

class DerivativeVisualization(Scene):
    def construct(self):
        # [0:00-0:05] Initial text about zooming in on a curve
        initial_text = Text("Imagine zooming in on a curve.", font_size=48)
        self.play(Write(initial_text))
        
        # Create a coordinate plane and curve
        plane = NumberPlane(
            x_range=[-4, 4, 1],
            y_range=[-3, 3, 1],
            background_line_style={"stroke_opacity": 0.4}
        ).scale(0.8).shift(DOWN*0.5)
        
        # Define a curve function
        def curve_func(x):
            return 0.3 * x**3 - 0.8 * x**2 + 0.2 * x + 1
        
        curve = plane.plot(
            curve_func,
            x_range=[-3, 3],
            color=BLUE,
            stroke_width=3
        )
        
        self.play(FadeOut(initial_text))
        self.play(Create(plane), Create(curve))
        self.wait(1)
        
        # [0:05] What's the curve doing at a single point?
        question_text = Text("What's the curve *doing* at a single point?", font_size=44)
        question_text.to_edge(UP)
        
        # Mark a point on the curve
        point_x = 1
        point_y = curve_func(point_x)
        point = Dot(plane.c2p(point_x, point_y), color=RED, radius=0.08)
        
        self.play(Write(question_text))
        self.play(Create(point))
        self.wait(2)
        
        # [0:15] It's not just a point, but a direction - a slope
        self.play(FadeOut(question_text))
        direction_text = Text("It's not just a point, but a direction – a slope.", font_size=44)
        direction_text.to_edge(UP)
        
        derivative_text = Text("The derivative is precisely that instantaneous rate of change.", font_size=40)
        derivative_text.next_to(direction_text, DOWN, buff=0.3)
        
        # Calculate slope at the point (derivative)
        h = 0.001
        slope = (curve_func(point_x + h) - curve_func(point_x - h)) / (2 * h)
        
        # Create tangent line
        tangent_line = Line(
            plane.c2p(point_x - 1, point_y - slope),
            plane.c2p(point_x + 1, point_y + slope),
            color=YELLOW,
            stroke_width=4
        )
        
        self.play(Write(direction_text))
        self.play(Write(derivative_text))
        self.play(Create(tangent_line))
        self.wait(3)
        
        # [0:25] Best possible straight line approximation
        self.play(FadeOut(direction_text), FadeOut(derivative_text))
        approximation_text = Text("Think of it as the best possible straight line approximation,", font_size=40)
        approximation_text.to_edge(UP)
        
        kissing_text = Text("perfectly kissing the curve at that point.", font_size=40)
        kissing_text.next_to(approximation_text, DOWN, buff=0.3)
        
        self.play(Write(approximation_text))
        self.play(Write(kissing_text))
        
        # Animate the tangent line "kissing" the curve
        self.play(
            tangent_line.animate.set_stroke(width=6),
            point.animate.set_color(YELLOW).scale(1.5)
        )
        self.wait(3)
        
        # [0:35] Final powerful tool description
        self.play(FadeOut(approximation_text), FadeOut(kissing_text))
        powerful_text = Text("It's a powerful tool, revealing how a function behaves at every moment,", font_size=36)
        powerful_text.to_edge(UP)
        
        analyze_text = Text("allowing us to analyze its growth, its peaks, and its valleys.", font_size=36)
        analyze_text.next_to(powerful_text, DOWN, buff=0.3)
        
        self.play(Write(powerful_text))
        self.play(Write(analyze_text))
        
        # Show multiple tangent lines at different points to illustrate the concept
        tangent_lines = VGroup()
        points = VGroup()
        
        for x_val in [-2, -0.5, 0.5, 2]:
            y_val = curve_func(x_val)
            h = 0.001
            local_slope = (curve_func(x_val + h) - curve_func(x_val - h)) / (2 * h)
            
            local_point = Dot(plane.c2p(x_val, y_val), color=YELLOW, radius=0.06)
            local_tangent = Line(
                plane.c2p(x_val - 0.8, y_val - 0.8 * local_slope),
                plane.c2p(x_val + 0.8, y_val + 0.8 * local_slope),
                color=YELLOW,
                stroke_width=3
            )
            
            tangent_lines.add(local_tangent)
            points.add(local_point)
        
        self.play(Create(points), Create(tangent_lines))
        self.wait(3)
        
        # Clear everything at the end
        self.play(FadeOut(VGroup(*self.mobjects)))
        self.wait(1)
