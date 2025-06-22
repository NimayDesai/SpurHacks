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
        # Opening text: "Calculus? It's all about change."
        opening_text = Text("Calculus? It's all about change.", font_size=48)
        self.play(Write(opening_text))
        self.wait(5)
        
        # Clear opening text
        self.play(FadeOut(opening_text))
        
        # [0:05] "Imagine zooming in on a curve – really, really close."
        zoom_text = Text("Imagine zooming in on a curve – really, really close.", font_size=40)
        zoom_text.to_edge(UP)
        
        # Create a coordinate plane and curve
        plane = NumberPlane(
            x_range=[-6, 6, 1],
            y_range=[-4, 4, 1],
            axis_config={"color": BLUE},
            background_line_style={
                "stroke_color": BLUE_D,
                "stroke_width": 1,
                "stroke_opacity": 0.3
            }
        )
        
        # Define a curve function
        def curve_func(x):
            return 0.1 * x**3 - 0.5 * x**2 + 2
        
        curve = plane.plot(
            curve_func,
            x_range=[-4.5, 4.5],
            color=YELLOW,
            stroke_width=4
        )
        
        self.play(Write(zoom_text))
        self.play(Create(plane), Create(curve))
        self.wait(5)
        
        # [0:10] "It starts to look straight, right? That's the core idea: approximating curves with tiny lines."
        self.play(FadeOut(zoom_text))
        
        straight_text = Text("It starts to look straight, right? That's the core idea:", font_size=36)
        straight_text.to_edge(UP)
        approx_text = Text("approximating curves with tiny lines.", font_size=36)
        approx_text.next_to(straight_text, DOWN)
        
        # Zoom in on a section of the curve
        zoom_point = 1.5
        zoomed_plane = NumberPlane(
            x_range=[zoom_point-0.5, zoom_point+0.5, 0.1],
            y_range=[curve_func(zoom_point)-0.3, curve_func(zoom_point)+0.3, 0.1],
            axis_config={"color": BLUE},
            background_line_style={
                "stroke_color": BLUE_D,
                "stroke_width": 1,
                "stroke_opacity": 0.3
            }
        )
        
        zoomed_curve = zoomed_plane.plot(
            curve_func,
            x_range=[zoom_point-0.4, zoom_point+0.4],
            color=YELLOW,
            stroke_width=6
        )
        
        # Create tangent line approximation
        slope = 3 * 0.1 * zoom_point**2 - 2 * 0.5 * zoom_point
        tangent_line = zoomed_plane.plot(
            lambda x: curve_func(zoom_point) + slope * (x - zoom_point),
            x_range=[zoom_point-0.4, zoom_point+0.4],
            color=RED,
            stroke_width=4
        )
        
        self.play(Write(straight_text), Write(approx_text))
        self.play(Transform(plane, zoomed_plane), Transform(curve, zoomed_curve))
        self.play(Create(tangent_line))
        self.wait(5)
        
        # [0:15] "We use these approximations to find slopes – instantaneous rates of change – and areas under curves, representing accumulation."
        self.play(FadeOut(straight_text), FadeOut(approx_text))
        
        slopes_text = Text("We use these approximations to find slopes –", font_size=32)
        slopes_text.to_edge(UP)
        rates_text = Text("instantaneous rates of change – and areas under curves,", font_size=32)
        rates_text.next_to(slopes_text, DOWN)
        accum_text = Text("representing accumulation.", font_size=32)
        accum_text.next_to(rates_text, DOWN)
        
        self.play(Write(slopes_text), Write(rates_text), Write(accum_text))
        
        # Show area under curve
        original_plane = NumberPlane(
            x_range=[-6, 6, 1],
            y_range=[-4, 4, 1],
            axis_config={"color": BLUE},
            background_line_style={
                "stroke_color": BLUE_D,
                "stroke_width": 1,
                "stroke_opacity": 0.3
            }
        )
        
        original_curve = original_plane.plot(
            lambda x: x**2/4 + 1,
            x_range=[-3, 3],
            color=YELLOW,
            stroke_width=4
        )
        
        area = original_plane.get_area(
            original_curve,
            x_range=[-2, 2],
            color=GREEN,
            opacity=0.5
        )
        
        self.play(
            Transform(plane, original_plane),
            Transform(curve, original_curve),
            FadeOut(tangent_line)
        )
        self.play(Create(area))
        self.wait(10)
        
        # [0:25] "It's powerful because it lets us model dynamic systems, from planetary orbits to population growth."
        self.play(
            FadeOut(slopes_text), 
            FadeOut(rates_text), 
            FadeOut(accum_text),
            FadeOut(plane),
            FadeOut(curve),
            FadeOut(area)
        )
        
        powerful_text = Text("It's powerful because it lets us model dynamic systems,", font_size=36)
        powerful_text.to_edge(UP)
        examples_text = Text("from planetary orbits to population growth.", font_size=36)
        examples_text.next_to(powerful_text, DOWN)
        
        # Create visual representations
        orbit_center = LEFT * 3
        orbit = Circle(radius=1.5, color=BLUE).move_to(orbit_center)
        planet = Dot(color=YELLOW, radius=0.1).move_to(orbit_center + RIGHT * 1.5)
        
        # Population growth curve
        growth_plane = NumberPlane(
            x_range=[0, 5, 1],
            y_range=[0, 4, 1],
            axis_config={"color": GRAY},
            background_line_style={
                "stroke_color": GRAY,
                "stroke_width": 1,
                "stroke_opacity": 0.3
            }
        ).scale(0.8).move_to(RIGHT * 3)
        
        growth_curve = growth_plane.plot(
            lambda x: 0.5 * np.exp(0.5 * x),
            x_range=[0, 4],
            color=GREEN,
            stroke_width=3
        )
        
        self.play(Write(powerful_text), Write(examples_text))
        self.play(Create(orbit), Create(planet))
        self.play(Create(growth_plane), Create(growth_curve))
        
        # Animate planet orbit
        self.play(Rotate(planet, angle=PI, about_point=orbit_center), run_time=3)
        self.wait(7)
        
        # [0:35] "At its heart, calculus is about understanding how things change, bit by infinitesimal bit."
        self.play(
            FadeOut(powerful_text),
            FadeOut(examples_text),
            FadeOut(orbit),
            FadeOut(planet),
            FadeOut(growth_plane),
            FadeOut(growth_curve)
        )
        
        heart_text = Text("At its heart, calculus is about understanding", font_size=40)
        change_text = Text("how things change, bit by infinitesimal bit.", font_size=40)
        change_text.next_to(heart_text, DOWN)
        
        self.play(Write(heart_text), Write(change_text))
        self.wait(3)
        
        # Final fade out
        self.play(FadeOut(heart_text), FadeOut(change_text))
