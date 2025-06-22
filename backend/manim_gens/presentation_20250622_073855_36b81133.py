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

class IntegrationAnimation(Scene):
    def construct(self):
        # [0:00] - Opening text
        opening_text = Text("Imagine trying to find the area under a curve.", font_size=36)
        self.play(Write(opening_text))
        self.wait(5)
        
        # [0:05] - Clear and show "It's tricky, right?"
        self.play(FadeOut(opening_text))
        tricky_text = Text("It's tricky, right?", font_size=36)
        self.play(Write(tricky_text))
        self.wait(0.5)
        
        # Show curve and area visualization
        self.play(FadeOut(tricky_text))
        
        # Create coordinate plane
        plane = NumberPlane(
            x_range=[-3, 3, 1],
            y_range=[-1, 3, 1],
            x_length=8,
            y_length=5,
            background_line_style={"stroke_opacity": 0.3}
        ).scale(0.8).shift(DOWN * 0.5)
        
        # Define curve function
        def curve_func(x):
            return 0.3 * x**2 + 1
        
        # Create curve
        curve = plane.plot(
            curve_func,
            x_range=[-2.5, 2.5],
            color=BLUE,
            stroke_width=4
        )
        
        # Create area under curve
        area = plane.get_area(curve, x_range=[-2, 2], color=BLUE, opacity=0.3)
        
        self.play(Create(plane), Create(curve), FadeIn(area))
        self.wait(1)
        
        # [0:10] - Show rectangles text and visualization
        rectangles_text = Text("But what if we sliced it into infinitely thin rectangles?", font_size=28)
        rectangles_text.to_edge(UP)
        self.play(Write(rectangles_text))
        
        # Create rectangles approximation
        rectangles = VGroup()
        n_rects = 8
        dx = 4 / n_rects
        for i in range(n_rects):
            x = -2 + i * dx
            height = curve_func(x)
            rect = Rectangle(
                width=dx * plane.x_axis.unit_size,
                height=height * plane.y_axis.unit_size,
                fill_color=YELLOW,
                fill_opacity=0.5,
                stroke_color=YELLOW,
                stroke_width=2
            )
            rect.move_to(plane.c2p(x + dx/2, height/2))
            rectangles.add(rect)
        
        self.play(FadeOut(area), Create(rectangles))
        self.wait(5)
        
        # [0:15] - Show sum approximation text
        self.play(FadeOut(rectangles_text))
        sum_text = Text("The sum of their areas approximates the total area.", font_size=28)
        sum_text.to_edge(UP)
        self.play(Write(sum_text))
        self.wait(5)
        
        # [0:20] - Show more rectangles for better approximation
        self.play(FadeOut(rectangles))
        
        # Create finer rectangles
        fine_rectangles = VGroup()
        n_fine = 20
        dx_fine = 4 / n_fine
        for i in range(n_fine):
            x = -2 + i * dx_fine
            height = curve_func(x)
            rect = Rectangle(
                width=dx_fine * plane.x_axis.unit_size,
                height=height * plane.y_axis.unit_size,
                fill_color=YELLOW,
                fill_opacity=0.5,
                stroke_color=YELLOW,
                stroke_width=1
            )
            rect.move_to(plane.c2p(x + dx_fine/2, height/2))
            fine_rectangles.add(rect)
        
        self.play(Create(fine_rectangles))
        self.wait(5)
        
        # [0:25] - Clear and show integration formalization text
        self.play(FadeOut(sum_text), FadeOut(fine_rectangles), FadeOut(plane), FadeOut(curve))
        
        integration_text = Text(
            "Integration formalizes this intuition, giving us a precise way\nto calculate that area – it's the continuous analogue of addition.",
            font_size=28
        )
        self.play(Write(integration_text))
        self.wait(10)
        
        # [0:35] - Show continuous addition concept
        self.play(FadeOut(integration_text))
        continuous_text = Text(
            "We're not just adding up numbers; we're adding up infinitely\nsmall quantities, accumulating them to find the total.",
            font_size=28
        )
        self.play(Write(continuous_text))
        self.wait(5)
        
        # [0:40] - Final powerful tool text
        self.play(FadeOut(continuous_text))
        final_text = Text(
            "It's a powerful tool revealing the hidden relationships\nbetween functions and their areas.",
            font_size=28
        )
        self.play(Write(final_text))
        self.wait(3)
        
        # Clear everything at the end
        self.play(FadeOut(final_text))
