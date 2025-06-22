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

class CalculusAnimation(Scene):
    def construct(self):
        # Opening line: "Calculus is about change."
        opening_text = Text("Calculus is about change.", font_size=48)
        self.play(Write(opening_text))
        self.wait(5)
        
        # Clear and transition to curve visualization at [0:05]
        self.play(FadeOut(opening_text))
        
        # Create coordinate plane and curve
        plane = NumberPlane(
            x_range=[-4, 4, 1],
            y_range=[-3, 3, 1],
            background_line_style={"stroke_opacity": 0.4}
        ).scale(0.8)
        
        # Define a smooth curve function
        def curve_func(x):
            return 0.3 * x**3 - 0.5 * x**2 - x + 1
        
        # Create the main curve
        curve = plane.plot(
            curve_func,
            x_range=[-3, 3],
            color=YELLOW,
            stroke_width=4
        )
        
        # Text for zoom explanation
        zoom_text = Text("Imagine zooming in on a curve –", font_size=36).to_edge(UP)
        straight_text = Text("it starts to look straight.", font_size=36).next_to(zoom_text, DOWN)
        
        self.play(Create(plane), Create(curve))
        self.play(Write(zoom_text))
        self.play(Write(straight_text))
        
        # Show zooming effect by focusing on a small section
        zoom_point = 1.5
        zoom_curve = plane.plot(
            curve_func,
            x_range=[zoom_point-0.3, zoom_point+0.3],
            color=RED,
            stroke_width=8
        )
        
        # Create a tangent line to show it looks straight when zoomed
        slope = 3 * 0.3 * zoom_point**2 - 2 * 0.5 * zoom_point - 1
        tangent_line = Line(
            plane.c2p(zoom_point-0.3, curve_func(zoom_point) + slope*(-0.3)),
            plane.c2p(zoom_point+0.3, curve_func(zoom_point) + slope*(0.3)),
            color=GREEN,
            stroke_width=6
        )
        
        self.play(Create(zoom_curve), Create(tangent_line))
        self.wait(2)
        
        # Core idea text
        core_text = Text("That's the core idea: approximating curves", font_size=32).to_edge(UP)
        segments_text = Text("with tiny line segments.", font_size=32).next_to(core_text, DOWN)
        
        self.play(Transform(zoom_text, core_text), Transform(straight_text, segments_text))
        self.wait(8)
        
        # Clear for differentiation section at [0:15]
        self.play(FadeOut(zoom_text), FadeOut(straight_text), FadeOut(zoom_curve), FadeOut(tangent_line))
        
        # Differentiation explanation at [0:15]
        diff_text1 = Text("Differentiation finds the slope of those segments,", font_size=32).to_edge(UP)
        diff_text2 = Text("revealing instantaneous rate of change.", font_size=32).next_to(diff_text1, DOWN)
        
        self.play(Write(diff_text1))
        self.play(Write(diff_text2))
        
        # Show multiple tangent lines at different points
        tangent_points = [-2, -1, 0, 1, 2]
        tangent_lines = []
        
        for point in tangent_points:
            slope = 3 * 0.3 * point**2 - 2 * 0.5 * point - 1
            tangent = Line(
                plane.c2p(point-0.5, curve_func(point) + slope*(-0.5)),
                plane.c2p(point+0.5, curve_func(point) + slope*(0.5)),
                color=GREEN,
                stroke_width=3
            )
            tangent_lines.append(tangent)
        
        self.play(*[Create(line) for line in tangent_lines])
        self.wait(8)
        
        # Clear for integration section at [0:25]
        self.play(FadeOut(diff_text1), FadeOut(diff_text2), *[FadeOut(line) for line in tangent_lines])
        
        # Integration explanation at [0:25]
        int_text1 = Text("Integration is the reverse, accumulating those tiny changes", font_size=28).to_edge(UP)
        int_text2 = Text("to find the area under the curve – total change over time.", font_size=28).next_to(int_text1, DOWN)
        
        self.play(Write(int_text1))
        self.play(Write(int_text2))
        
        # Show area under curve with rectangles
        rectangles = []
        x_vals = np.linspace(-2, 2, 20)
        
        for i in range(len(x_vals)-1):
            x_start = x_vals[i]
            x_end = x_vals[i+1]
            height = max(0, curve_func(x_start))
            if height > 0:
                rect = Rectangle(
                    width=plane.x_axis.unit_size * (x_end - x_start),
                    height=plane.y_axis.unit_size * height,
                    fill_opacity=0.3,
                    fill_color=BLUE,
                    stroke_width=1
                ).move_to(plane.c2p(x_start + (x_end-x_start)/2, height/2))
                rectangles.append(rect)
        
        self.play(*[Create(rect) for rect in rectangles])
        self.wait(8)
        
        # Final philosophical statement at [0:35]
        self.play(FadeOut(int_text1), FadeOut(int_text2), *[FadeOut(rect) for rect in rectangles])
        
        final_text1 = Text("It's about connecting the local to the global,", font_size=36).to_edge(UP)
        final_text2 = Text("the infinitesimal to the finite.", font_size=36).next_to(final_text1, DOWN)
        
        self.play(Write(final_text1))
        self.play(Write(final_text2))
        self.wait(3)
        
        # Final clear
        self.play(FadeOut(final_text1), FadeOut(final_text2), FadeOut(plane), FadeOut(curve))
