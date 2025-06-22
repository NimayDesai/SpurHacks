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

class DerivativeExplanation(Scene):
    def construct(self):
        # Initial text about zooming in on a curve
        zoom_text = Text("Imagine zooming in on a curve.", font_size=36)
        self.play(Write(zoom_text))
        self.wait(5)
        
        # Clear and show what's its instantaneous slope
        self.play(FadeOut(zoom_text))
        slope_question = Text("What's its instantaneous slope? That's the derivative.", font_size=36)
        self.play(Write(slope_question))
        self.wait(5)
        
        # Clear and show explanation about average slope
        self.play(FadeOut(slope_question))
        average_text = Text("It's not just the average slope over a range, but the slope at a single, precise point.", font_size=32)
        self.play(Write(average_text))
        self.wait(5)
        
        # Clear and show direction explanation
        self.play(FadeOut(average_text))
        direction_text = Text("Think of it as the direction the function is heading at that moment.", font_size=34)
        self.play(Write(direction_text))
        self.wait(5)
        
        # Clear and show tangent line explanation with visual
        self.play(FadeOut(direction_text))
        tangent_text = Text("Visually, it's the slope of the tangent line—a line that just barely kisses the curve.", font_size=30)
        
        # Create coordinate plane
        plane = NumberPlane(
            x_range=[-3, 3, 1],
            y_range=[-2, 4, 1],
            x_length=6,
            y_length=4,
            background_line_style={"stroke_opacity": 0.3}
        ).scale(0.7).shift(DOWN * 0.5)
        
        # Create a curve (parabola)
        def curve_func(x):
            return 0.5 * x**2 + 0.5
            
        curve = plane.plot(
            curve_func,
            x_range=[-2.5, 2.5],
            color=BLUE,
            stroke_width=3
        )
        
        # Point on curve
        point_x = 1
        point_y = curve_func(point_x)
        point = Dot(plane.coords_to_point(point_x, point_y), color=RED, radius=0.08)
        
        # Tangent line
        slope = point_x  # derivative of 0.5x^2 + 0.5 is x
        tangent_line = Line(
            plane.coords_to_point(point_x - 1, point_y - slope),
            plane.coords_to_point(point_x + 1, point_y + slope),
            color=YELLOW,
            stroke_width=3
        )
        
        self.play(Write(tangent_text))
        self.play(Create(plane), Create(curve), Create(point), Create(tangent_line))
        self.wait(5)
        
        # Clear and show final concept
        self.play(FadeOut(tangent_text), FadeOut(plane), FadeOut(curve), FadeOut(point), FadeOut(tangent_line))
        final_text = Text("The derivative captures the rate of change, a fundamental concept in calculus.", font_size=32)
        self.play(Write(final_text))
        self.wait(5)
        
        # Final clear
        self.play(FadeOut(final_text))
