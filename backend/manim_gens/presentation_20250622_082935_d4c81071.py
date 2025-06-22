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

class IntegralVisualization(Scene):
    def construct(self):
        # Initial text about accumulating area
        initial_text = Text("Imagine accumulating tiny slivers of area under a curve.", font_size=36)
        self.play(Write(initial_text))
        self.wait(5)
        
        # Clear and show integration concept at [0:05]
        self.play(FadeOut(initial_text))
        
        # Set up coordinate plane and curve
        plane = NumberPlane(
            x_range=[-4, 4, 1],
            y_range=[0, 4, 1],
            x_length=8,
            y_length=6,
            background_line_style={"stroke_opacity": 0.3}
        ).scale(0.8).shift(DOWN*0.5)
        
        # Define a smooth curve function
        def curve_func(x):
            return 2 + 0.5 * x**2 * np.exp(-0.3 * x**2)
        
        curve = plane.plot(
            curve_func,
            x_range=[-3, 3],
            color=BLUE,
            stroke_width=4
        )
        
        integration_text = Text("That's the core idea behind integration.", font_size=36).to_edge(UP)
        
        self.play(Create(plane), Create(curve), Write(integration_text))
        self.wait(3)
        
        # Show rectangles at [0:15]
        rectangles_text = Text("We're summing infinitely many infinitesimally thin rectangles.", font_size=32).to_edge(UP)
        self.play(Transform(integration_text, rectangles_text))
        
        # Create rectangles under the curve
        rectangles = VGroup()
        n_rects = 20
        x_start, x_end = -2, 2
        dx = (x_end - x_start) / n_rects
        
        for i in range(n_rects):
            x = x_start + i * dx
            height = curve_func(x)
            rect = Rectangle(
                width=dx,
                height=height,
                fill_opacity=0.5,
                fill_color=YELLOW,
                stroke_width=1,
                stroke_color=WHITE
            )
            rect.align_to(plane.c2p(x, 0), DOWN + LEFT)
            rect.shift(plane.c2p(0, height/2, 0) - plane.c2p(0, 0, 0))
            rectangles.add(rect)
        
        self.play(Create(rectangles))
        self.wait(5)
        
        # Transition at [0:20]
        smooth_text = Text("Instead of discrete additions, we smoothly sweep out the area.", font_size=32).to_edge(UP)
        self.play(Transform(integration_text, smooth_text))
        
        # Transform rectangles to smooth area
        smooth_area = plane.get_area(curve, x_range=[-2, 2], color=YELLOW, opacity=0.7)
        self.play(Transform(rectangles, smooth_area))
        self.wait(5)
        
        # Final concept at [0:30]
        final_text1 = Text("The integral represents the total accumulation, a continuous sum,", font_size=28).to_edge(UP)
        final_text2 = Text("revealing the area's magnitude.", font_size=28).next_to(final_text1, DOWN)
        conclusion_text = Text("It's a powerful tool, moving beyond simple shapes to explore far more complex areas.", font_size=24).to_edge(DOWN)
        
        self.play(Transform(integration_text, final_text1), Write(final_text2))
        self.wait(3)
        self.play(Write(conclusion_text))
        self.wait(7)
        
        # Clear everything
        self.play(FadeOut(VGroup(plane, curve, rectangles, integration_text, final_text2, conclusion_text)))
