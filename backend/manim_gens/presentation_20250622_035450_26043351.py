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
        # [0:00-0:05] Calculus is all about change.
        title = Text("Calculus is all about change.", font_size=48)
        self.play(Write(title))
        self.wait(5)
        
        # [0:05] Imagine zooming in on a curve – incredibly close.
        self.play(FadeOut(title))
        
        plane = NumberPlane(
            x_range=[-5, 5, 1],
            y_range=[-3, 3, 1],
            background_line_style={"stroke_opacity": 0.4}
        ).scale(0.8)
        
        curve_func = lambda x: 0.1 * x**3 - 0.5 * x + 1
        curve = plane.plot(
            curve_func,
            x_range=[-4, 4],
            color=BLUE,
            stroke_width=4
        )
        
        zoom_text = Text("Imagine zooming in on a curve – incredibly close.", font_size=36)
        zoom_text.to_edge(UP)
        
        self.play(Write(zoom_text))
        self.play(Create(plane), Create(curve))
        
        # Zoom in effect
        zoom_point = [1, curve_func(1), 0]
        zoomed_plane = NumberPlane(
            x_range=[0.5, 1.5, 0.1],
            y_range=[0.3, 1.1, 0.1],
            background_line_style={"stroke_opacity": 0.6}
        ).scale(2)
        
        zoomed_curve = zoomed_plane.plot(
            curve_func,
            x_range=[0.5, 1.5],
            color=BLUE,
            stroke_width=6
        )
        
        self.play(
            Transform(plane, zoomed_plane),
            Transform(curve, zoomed_curve)
        )
        self.wait(2)
        
        # Show it looks straight
        straight_text = Text("It starts to look straight, right?", font_size=36)
        straight_text.to_edge(DOWN)
        
        # Draw tangent line
        slope = 3 * 0.1 * 1**2 - 0.5  # derivative at x=1
        tangent_line = Line(
            zoomed_plane.coords_to_point(0.7, curve_func(1) + slope * (0.7 - 1)),
            zoomed_plane.coords_to_point(1.3, curve_func(1) + slope * (1.3 - 1)),
            color=RED,
            stroke_width=4
        )
        
        self.play(Write(straight_text))
        self.play(Create(tangent_line))
        self.wait(3)
        
        # [0:15] That's the core idea behind the derivative: finding the instantaneous slope.
        self.play(FadeOut(zoom_text), FadeOut(straight_text))
        
        derivative_text = Text("That's the core idea behind the derivative:", font_size=36)
        slope_text = Text("finding the instantaneous slope.", font_size=36)
        derivative_text.to_edge(UP)
        slope_text.next_to(derivative_text, DOWN)
        
        self.play(Write(derivative_text))
        self.play(Write(slope_text))
        self.wait(5)
        
        # [0:25] The integral, on the other hand, is about accumulation.
        self.play(FadeOut(derivative_text), FadeOut(slope_text), FadeOut(plane), FadeOut(curve), FadeOut(tangent_line))
        
        # Reset to original view
        new_plane = NumberPlane(
            x_range=[-3, 3, 1],
            y_range=[-1, 3, 1],
            background_line_style={"stroke_opacity": 0.4}
        ).scale(0.8)
        
        integral_func = lambda x: x**2 * 0.3 + 0.5
        integral_curve = new_plane.plot(
            integral_func,
            x_range=[-2.5, 2.5],
            color=GREEN,
            stroke_width=4
        )
        
        integral_text = Text("The integral, on the other hand, is about accumulation.", font_size=36)
        integral_text.to_edge(UP)
        
        self.play(Write(integral_text))
        self.play(Create(new_plane), Create(integral_curve))
        
        # Show area under curve with rectangles
        area_text = Text("Think of it as summing up infinitely many tiny slices", font_size=32)
        area_text2 = Text("under a curve to find the area.", font_size=32)
        area_text.to_edge(DOWN, buff=1)
        area_text2.next_to(area_text, DOWN, buff=0.2)
        
        self.play(Write(area_text))
        self.play(Write(area_text2))
        
        # Create rectangles to show Riemann sum
        rectangles = VGroup()
        x_start, x_end = -2, 2
        n_rects = 16
        dx = (x_end - x_start) / n_rects
        
        for i in range(n_rects):
            x = x_start + i * dx
            height = integral_func(x)
            if height > 0:
                rect = Rectangle(
                    width=dx * new_plane.x_axis.unit_size,
                    height=height * new_plane.y_axis.unit_size,
                    stroke_width=1,
                    stroke_color=YELLOW,
                    fill_color=YELLOW,
                    fill_opacity=0.6
                )
                rect.move_to(new_plane.coords_to_point(x + dx/2, height/2))
                rectangles.add(rect)
        
        self.play(Create(rectangles))
        self.wait(5)
        
        # [0:35] These seemingly different concepts – slope and area – are intimately linked
        self.play(FadeOut(integral_text), FadeOut(area_text), FadeOut(area_text2))
        
        connection_text = Text("These seemingly different concepts – slope and area –", font_size=32)
        linked_text = Text("are intimately linked through the", font_size=32)
        theorem_text = Text("fundamental theorem of calculus.", font_size=32)
        
        connection_text.to_edge(UP, buff=0.5)
        linked_text.next_to(connection_text, DOWN, buff=0.2)
        theorem_text.next_to(linked_text, DOWN, buff=0.2)
        
        self.play(Write(connection_text))
        self.play(Write(linked_text))
        self.play(Write(theorem_text))
        
        # Show both derivative and integral concepts together
        derivative_arrow = Arrow(
            new_plane.coords_to_point(0, 2),
            new_plane.coords_to_point(1, 2.3),
            color=RED,
            stroke_width=3
        )
        derivative_label = Text("Slope", font_size=24, color=RED)
        derivative_label.next_to(derivative_arrow, UP)
        
        integral_arrow = Arrow(
            new_plane.coords_to_point(-1, -0.5),
            new_plane.coords_to_point(0, 0.5),
            color=YELLOW,
            stroke_width=3
        )
        integral_label = Text("Area", font_size=24, color=YELLOW)
        integral_label.next_to(integral_arrow, LEFT)
        
        self.play(
            Create(derivative_arrow), Write(derivative_label),
            Create(integral_arrow), Write(integral_label)
        )
        self.wait(3)
        
        # Final message about beautiful symmetry
        self.play(
            FadeOut(connection_text), FadeOut(linked_text), FadeOut(theorem_text),
            FadeOut(derivative_arrow), FadeOut(derivative_label),
            FadeOut(integral_arrow), FadeOut(integral_label)
        )
        
        symmetry_text = Text("It's a beautiful symmetry, revealing a profound", font_size=32)
        connection_final = Text("connection between change and accumulation.", font_size=32)
        
        symmetry_text.to_edge(UP, buff=1)
        connection_final.next_to(symmetry_text, DOWN, buff=0.3)
        
        self.play(Write(symmetry_text))
        self.play(Write(connection_final))
        self.wait(3)
        
        # Clear all elements at the end
        self.play(FadeOut(Group(*self.mobjects)))
