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

class CalculusIntro(Scene):
    def construct(self):
        # Opening text
        opening_text = Text("Calculus is about change.", font_size=48)
        self.play(Write(opening_text))
        self.wait(1)
        
        # [0:05] - Clear and introduce curve zooming concept
        self.play(FadeOut(opening_text))
        
        # Create a curve to demonstrate zooming
        plane = NumberPlane(
            x_range=[-6, 6],
            y_range=[-4, 4],
            background_line_style={"stroke_opacity": 0.3}
        )
        
        def curve_func(x):
            return 0.5 * x**2 - 1
        
        curve = plane.plot(
            curve_func,
            x_range=[-4, 4],
            color=BLUE,
            stroke_width=4
        )
        
        zoom_text = Text("Imagine zooming in on a curve.", font_size=36)
        zoom_text.to_edge(UP)
        
        self.play(
            Create(plane),
            Create(curve),
            Write(zoom_text)
        )
        self.wait(2)
        
        # Show zooming effect by creating a smaller section
        zoom_point = 2
        zoomed_plane = NumberPlane(
            x_range=[zoom_point-0.5, zoom_point+0.5],
            y_range=[curve_func(zoom_point)-0.5, curve_func(zoom_point)+0.5],
            background_line_style={"stroke_opacity": 0.3}
        )
        
        zoomed_curve = zoomed_plane.plot(
            curve_func,
            x_range=[zoom_point-0.5, zoom_point+0.5],
            color=BLUE,
            stroke_width=6
        )
        
        # Tangent line to show it looks straight
        tangent_slope = curve_func(zoom_point + 0.001) - curve_func(zoom_point - 0.001)
        tangent_slope /= 0.002
        
        def tangent_func(x):
            return tangent_slope * (x - zoom_point) + curve_func(zoom_point)
        
        tangent_line = zoomed_plane.plot(
            tangent_func,
            x_range=[zoom_point-0.4, zoom_point+0.4],
            color=RED,
            stroke_width=4
        )
        
        straight_text = Text("It starts to look straight, right?", font_size=32)
        straight_text.next_to(zoom_text, DOWN)
        
        self.play(
            Transform(plane, zoomed_plane),
            Transform(curve, zoomed_curve),
            Write(straight_text)
        )
        
        self.play(Create(tangent_line))
        self.wait(2)
        
        # [0:15] - Derivative explanation
        self.play(
            FadeOut(plane),
            FadeOut(curve),
            FadeOut(tangent_line),
            FadeOut(zoom_text),
            FadeOut(straight_text)
        )
        
        derivative_text = Text(
            "That's the core idea of the derivative – the instantaneous slope.",
            font_size=36
        )
        self.play(Write(derivative_text))
        self.wait(3)
        
        # [0:25] - Integration explanation
        self.play(FadeOut(derivative_text))
        
        # Create new plane and curve for integration
        integration_plane = NumberPlane(
            x_range=[-4, 4],
            y_range=[-1, 3],
            background_line_style={"stroke_opacity": 0.3}
        )
        
        def integration_curve(x):
            return x**2 / 4 + 0.5
        
        integration_curve_graph = integration_plane.plot(
            integration_curve,
            x_range=[-3, 3],
            color=GREEN,
            stroke_width=4
        )
        
        # Show area under curve with rectangles
        rectangles = VGroup()
        for i in range(-12, 13):
            x_val = i * 0.25
            if -3 <= x_val <= 3:
                height = integration_curve(x_val)
                if height > 0:
                    rect = Rectangle(
                        width=0.25,
                        height=height,
                        fill_opacity=0.5,
                        fill_color=YELLOW,
                        stroke_width=1
                    )
                    rect.move_to(integration_plane.c2p(x_val + 0.125, height/2))
                    rectangles.add(rect)
        
        integration_text1 = Text("Integration? It's the reverse;", font_size=36)
        integration_text1.to_edge(UP)
        
        integration_text2 = Text(
            "adding up infinitely many tiny slices to find the area under that curve.",
            font_size=32
        )
        integration_text2.next_to(integration_text1, DOWN)
        
        self.play(
            Create(integration_plane),
            Create(integration_curve_graph),
            Write(integration_text1)
        )
        
        self.play(
            Create(rectangles),
            Write(integration_text2)
        )
        self.wait(3)
        
        # [0:35] - Symmetry explanation
        self.play(
            FadeOut(integration_plane),
            FadeOut(integration_curve_graph),
            FadeOut(rectangles),
            FadeOut(integration_text1),
            FadeOut(integration_text2)
        )
        
        symmetry_text = Text(
            "Derivative and integral are opposites, like multiplication and division,\nrevealing a beautiful symmetry at the heart of how things change.",
            font_size=32,
            line_spacing=1.2
        )
        
        self.play(Write(symmetry_text))
        self.wait(4)
        
        # Final text
        self.play(FadeOut(symmetry_text))
        
        final_text = Text(
            "It's not just about slopes and areas;\nit's about understanding the dynamics of the universe.",
            font_size=36,
            line_spacing=1.2
        )
        
        self.play(Write(final_text))
        self.wait(3)
        
        self.play(FadeOut(final_text))
