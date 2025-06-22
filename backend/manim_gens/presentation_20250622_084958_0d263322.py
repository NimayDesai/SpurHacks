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
        intro_text = Text("Imagine zooming in on a curve.", font_size=36)
        self.play(Write(intro_text))
        self.wait(1)
        
        # Create a curve to zoom into
        plane = NumberPlane(
            x_range=[-3, 3, 1],
            y_range=[-2, 2, 1],
            background_line_style={"stroke_opacity": 0.3}
        )
        
        def curve_func(x):
            return 0.3 * x**2 - 0.1 * x + 0.5
        
        curve = plane.plot(
            curve_func,
            x_range=[-3, 3],
            color=BLUE,
            stroke_width=3
        )
        
        self.play(FadeOut(intro_text))
        self.play(Create(plane), Create(curve))
        self.wait(4)
        
        # [0:05-0:15] Zoom in incredibly close
        zoom_text = Text("Incredibly close, until it looks almost straight.", font_size=36)
        zoom_text.to_edge(UP)
        
        # Create zoomed view
        zoomed_plane = NumberPlane(
            x_range=[-0.5, 0.5, 0.1],
            y_range=[-0.2, 0.8, 0.1],
            background_line_style={"stroke_opacity": 0.4}
        )
        
        zoomed_curve = zoomed_plane.plot(
            curve_func,
            x_range=[-0.5, 0.5],
            color=BLUE,
            stroke_width=4
        )
        
        self.play(Write(zoom_text))
        self.play(
            Transform(plane, zoomed_plane),
            Transform(curve, zoomed_curve)
        )
        self.wait(5)
        
        derivative_text = Text("That tiny line segment? That's the core idea behind the derivative.", font_size=32)
        derivative_text.to_edge(DOWN)
        
        # Highlight a small segment of the curve
        point = 0.2
        segment_start = zoomed_plane.c2p(point - 0.1, curve_func(point - 0.1))
        segment_end = zoomed_plane.c2p(point + 0.1, curve_func(point + 0.1))
        segment = Line(segment_start, segment_end, color=YELLOW, stroke_width=6)
        
        self.play(Write(derivative_text))
        self.play(Create(segment))
        self.wait(5)
        
        # [0:15-0:25] Instantaneous rate of change explanation
        self.play(FadeOut(zoom_text), FadeOut(derivative_text))
        
        rate_text = Text("It represents the instantaneous rate of change –", font_size=32)
        rate_text.to_edge(UP)
        slope_text = Text("the slope of that near-straight line.", font_size=32)
        slope_text.next_to(rate_text, DOWN)
        
        # Show tangent line
        slope = 2 * 0.3 * point - 0.1  # derivative of the function at point
        tangent_line = zoomed_plane.plot(
            lambda x: curve_func(point) + slope * (x - point),
            x_range=[-0.5, 0.5],
            color=RED,
            stroke_width=3
        )
        
        self.play(Write(rate_text))
        self.play(Write(slope_text))
        self.play(Create(tangent_line))
        self.wait(5)
        
        calculus_text = Text("Differential calculus is all about finding these slopes,", font_size=30)
        calculus_text.to_edge(DOWN)
        revealing_text = Text("revealing how a function's values change at any given point.", font_size=30)
        revealing_text.next_to(calculus_text, DOWN)
        
        self.play(Write(calculus_text))
        self.play(Write(revealing_text))
        self.wait(5)
        
        # [0:25-0:35] Applications and conclusion
        self.play(
            FadeOut(rate_text),
            FadeOut(slope_text),
            FadeOut(calculus_text),
            FadeOut(revealing_text)
        )
        
        unlock_text = Text("It unlocks powerful tools for understanding", font_size=32)
        unlock_text.to_edge(UP)
        
        apps_text = Text("velocity, acceleration, optimization—", font_size=32)
        apps_text.next_to(unlock_text, DOWN)
        
        dynamics_text = Text("essentially, the dynamics of change itself.", font_size=32)
        dynamics_text.next_to(apps_text, DOWN)
        
        self.play(Write(unlock_text))
        self.play(Write(apps_text))
        self.play(Write(dynamics_text))
        self.wait(5)
        
        # Final fade out at [0:35]
        self.play(
            FadeOut(unlock_text),
            FadeOut(apps_text),
            FadeOut(dynamics_text),
            FadeOut(plane),
            FadeOut(curve),
            FadeOut(segment),
            FadeOut(tangent_line)
        )
