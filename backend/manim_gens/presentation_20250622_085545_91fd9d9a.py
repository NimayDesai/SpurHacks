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

class IntegralExplanation(Scene):
    def construct(self):
        # [0:00-0:05] - Opening text and blob
        opening_text = Text("Imagine trying to find the area of a weirdly shaped blob.", 
                           font_size=36).to_edge(UP)
        
        # Create a weird blob shape
        blob = Polygon(
            [-2, -1, 0], [-1, -2, 0], [0, -1.5, 0], [1, -2, 0], 
            [2, -0.5, 0], [1.5, 0.5, 0], [0.5, 1, 0], [-0.5, 1.2, 0], 
            [-1.5, 0.8, 0], [-2, 0, 0],
            color=BLUE, fill_opacity=0.5
        )
        
        self.play(Write(opening_text))
        self.play(FadeIn(blob))
        self.wait(1)
        
        # [0:05] - Clear and show next text
        self.play(FadeOut(opening_text), FadeOut(blob))
        
        formula_text = Text("We can't use simple formulas, right?", 
                           font_size=36).to_edge(UP)
        self.play(Write(formula_text))
        self.wait(1)
        
        # [0:10] - Show rectangles chopping the blob
        self.play(FadeOut(formula_text))
        
        rectangle_text = Text("But what if we chopped it into lots of tiny rectangles?", 
                             font_size=36).to_edge(UP)
        
        # Recreate blob and add rectangles
        blob = Polygon(
            [-2, -1, 0], [-1, -2, 0], [0, -1.5, 0], [1, -2, 0], 
            [2, -0.5, 0], [1.5, 0.5, 0], [0.5, 1, 0], [-0.5, 1.2, 0], 
            [-1.5, 0.8, 0], [-2, 0, 0],
            color=BLUE, fill_opacity=0.3
        )
        
        # Create rectangles that approximate the blob
        rectangles = VGroup()
        for i in range(-8, 9):
            x = i * 0.25
            if -2 <= x <= 2:
                # Approximate height based on blob shape
                height = 1.5 - 0.3 * x * x + 0.2 * abs(x)
                if height > 0:
                    rect = Rectangle(width=0.25, height=height, 
                                   color=YELLOW, fill_opacity=0.6)
                    rect.move_to([x, height/2 - 0.5, 0])
                    rectangles.add(rect)
        
        self.play(Write(rectangle_text))
        self.play(FadeIn(blob))
        self.play(FadeIn(rectangles))
        self.wait(1)
        
        # [0:15] - Sum approximation
        self.play(FadeOut(rectangle_text))
        
        sum_text = Text("The sum of their areas is a pretty good approximation.", 
                       font_size=36).to_edge(UP)
        self.play(Write(sum_text))
        self.wait(1)
        
        # [0:20] - Infinitely many rectangles
        self.play(FadeOut(sum_text), FadeOut(blob), FadeOut(rectangles))
        
        infinite_text = Text("Now, imagine infinitely many, infinitesimally thin rectangles.", 
                            font_size=36).to_edge(UP)
        
        # Show much thinner rectangles
        thin_rectangles = VGroup()
        for i in range(-40, 41):
            x = i * 0.05
            if -2 <= x <= 2:
                height = 1.5 - 0.3 * x * x + 0.2 * abs(x)
                if height > 0:
                    rect = Rectangle(width=0.05, height=height, 
                                   color=RED, fill_opacity=0.8)
                    rect.move_to([x, height/2 - 0.5, 0])
                    thin_rectangles.add(rect)
        
        self.play(Write(infinite_text))
        self.play(FadeIn(thin_rectangles))
        self.wait(1)
        
        # [0:25] - The integral definition
        self.play(FadeOut(infinite_text), FadeOut(thin_rectangles))
        
        integral_text1 = Text("That sum, that limit as the rectangles shrink, is the integral.", 
                             font_size=36).to_edge(UP)
        integral_text2 = Text("It's the ultimate area-finding machine.", 
                             font_size=36).next_to(integral_text1, DOWN, buff=0.5)
        
        # Show a smooth curve representing the limit
        axes = Axes(
            x_range=[-3, 3, 1],
            y_range=[-1, 2, 1],
            x_length=6,
            y_length=3,
            axis_config={"color": WHITE}
        ).scale(0.8)
        
        curve_func = lambda x: 1.5 - 0.3 * x * x + 0.2 * abs(x)
        curve = axes.plot(curve_func, x_range=[-2, 2], color=GREEN, stroke_width=4)
        area = axes.get_area(curve, x_range=[-2, 2], color=GREEN, opacity=0.4)
        
        self.play(Write(integral_text1))
        self.play(Write(integral_text2))
        self.play(FadeIn(axes))
        self.play(Create(curve))
        self.play(FadeIn(area))
        self.wait(1)
        
        # [0:30] - Broader applications
        self.play(FadeOut(integral_text1), FadeOut(integral_text2), 
                 FadeOut(axes), FadeOut(curve), FadeOut(area))
        
        broader_text1 = Text("It's not just about areas, though;", 
                            font_size=36).to_edge(UP)
        broader_text2 = Text("it's about accumulating infinitely small contributions", 
                            font_size=36).next_to(broader_text1, DOWN, buff=0.3)
        broader_text3 = Text("to get a total value.", 
                            font_size=36).next_to(broader_text2, DOWN, buff=0.3)
        
        self.play(Write(broader_text1))
        self.play(Write(broader_text2))
        self.play(Write(broader_text3))
        self.wait(1)
        
        # Final statement
        self.play(FadeOut(broader_text1), FadeOut(broader_text2), FadeOut(broader_text3))
        
        final_text = Text("A powerful idea, with far-reaching consequences.", 
                         font_size=40)
        
        self.play(Write(final_text))
        self.wait(2)
        
        self.play(FadeOut(final_text))
