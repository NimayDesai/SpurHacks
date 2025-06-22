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

class DifferentialEquationsIntro(Scene):
    def construct(self):
        # [0:00] - Opening text
        opening_text = Text("What if we could describe how things change,", font_size=36)
        opening_text2 = Text("not just where they are?", font_size=36)
        opening_group = VGroup(opening_text, opening_text2).arrange(DOWN, buff=0.3)
        
        self.play(Write(opening_group))
        self.wait(5)
        
        # [0:05] - Clear and show differential equations power
        self.play(FadeOut(opening_group))
        
        power_text = Text("That's the power of differential equations.", font_size=40, color=BLUE)
        link_text = Text("They link a function to its rate of change.", font_size=36)
        power_group = VGroup(power_text, link_text).arrange(DOWN, buff=0.5)
        
        # Visual representation of function and its derivative
        axes = Axes(
            x_range=[-3, 3, 1],
            y_range=[-2, 2, 1],
            x_length=6,
            y_length=4,
            axis_config={"color": WHITE}
        ).scale(0.6).shift(DOWN * 1.5)
        
        # Original function (parabola)
        func = lambda x: 0.3 * x**2 - 1
        curve = axes.plot(func, x_range=[-2.5, 2.5], color=GREEN, stroke_width=3)
        
        # Derivative function (linear)
        deriv_func = lambda x: 0.6 * x
        deriv_curve = axes.plot(deriv_func, x_range=[-2.5, 2.5], color=RED, stroke_width=3)
        
        func_label = Text("f(x)", font_size=24, color=GREEN).next_to(curve, UP)
        deriv_label = Text("f'(x)", font_size=24, color=RED).next_to(deriv_curve, DOWN)
        
        self.play(Write(power_group))
        self.wait(2)
        self.play(Create(axes), Create(curve), Create(deriv_curve))
        self.play(Write(func_label), Write(deriv_label))
        self.wait(8)
        
        # [0:15] - Clear and show snowball example
        self.play(FadeOut(power_group), FadeOut(axes), FadeOut(curve), FadeOut(deriv_curve), 
                 FadeOut(func_label), FadeOut(deriv_label))
        
        snowball_text1 = Text("Imagine a snowball rolling downhill;", font_size=36)
        snowball_text2 = Text("its speed depends on its size,", font_size=36)
        snowball_text3 = Text("which in turn depends on how much snow it's accumulated.", font_size=36)
        snowball_group = VGroup(snowball_text1, snowball_text2, snowball_text3).arrange(DOWN, buff=0.3)
        
        # Visual of snowball rolling downhill
        hill = Line(LEFT * 4 + UP * 2, RIGHT * 4 + DOWN * 2, color=DARK_GRAY, stroke_width=8)
        
        # Snowballs of different sizes at different positions
        small_snowball = Circle(radius=0.2, color=WHITE, fill_opacity=0.8).move_to(LEFT * 3 + UP * 1.5)
        medium_snowball = Circle(radius=0.35, color=WHITE, fill_opacity=0.8).move_to(UP * 0.5)
        large_snowball = Circle(radius=0.5, color=WHITE, fill_opacity=0.8).move_to(RIGHT * 3 + DOWN * 1.5)
        
        # Speed vectors
        small_arrow = Arrow(start=small_snowball.get_center(), 
                           end=small_snowball.get_center() + RIGHT * 0.8 + DOWN * 0.4, 
                           color=YELLOW, stroke_width=3)
        medium_arrow = Arrow(start=medium_snowball.get_center(), 
                            end=medium_snowball.get_center() + RIGHT * 1.2 + DOWN * 0.6, 
                            color=YELLOW, stroke_width=3)
        large_arrow = Arrow(start=large_snowball.get_center(), 
                           end=large_snowball.get_center() + RIGHT * 1.6 + DOWN * 0.8, 
                           color=YELLOW, stroke_width=3)
        
        self.play(Write(snowball_group))
        self.wait(3)
        self.play(Create(hill))
        self.play(Create(small_snowball), Create(small_arrow))
        self.wait(1)
        self.play(Create(medium_snowball), Create(medium_arrow))
        self.wait(1)
        self.play(Create(large_snowball), Create(large_arrow))
        self.wait(5)
        
        # [0:25] - Clear and show interconnectedness
        self.play(FadeOut(snowball_group), FadeOut(hill), FadeOut(small_snowball), FadeOut(medium_snowball), 
                 FadeOut(large_snowball), FadeOut(small_arrow), FadeOut(medium_arrow), FadeOut(large_arrow))
        
        interconnect_text1 = Text("This interconnectedness, this feedback loop,", font_size=36)
        interconnect_text2 = Text("is what a differential equation captures.", font_size=36)
        solving_text1 = Text("Solving it means unraveling that dependency,", font_size=36)
        solving_text2 = Text("revealing the snowball's trajectory over time.", font_size=36)
        
        interconnect_group = VGroup(interconnect_text1, interconnect_text2).arrange(DOWN, buff=0.3)
        solving_group = VGroup(solving_text1, solving_text2).arrange(DOWN, buff=0.3)
        
        # Visual of feedback loop
        center = ORIGIN
        arrows = VGroup()
        labels = VGroup()
        
        # Create circular feedback arrows
        arc1 = Arc(radius=1.5, start_angle=0, angle=PI/2, color=BLUE, stroke_width=4)
        arc2 = Arc(radius=1.5, start_angle=PI/2, angle=PI/2, color=BLUE, stroke_width=4)
        arc3 = Arc(radius=1.5, start_angle=PI, angle=PI/2, color=BLUE, stroke_width=4)
        arc4 = Arc(radius=1.5, start_angle=3*PI/2, angle=PI/2, color=BLUE, stroke_width=4)
        
        # Add arrowheads
        arrow1 = Arrow(start=RIGHT * 1.5, end=RIGHT * 1.5 + UP * 0.1, color=BLUE, stroke_width=4, max_tip_length_to_length_ratio=0.3)
        arrow2 = Arrow(start=UP * 1.5, end=UP * 1.5 + LEFT * 0.1, color=BLUE, stroke_width=4, max_tip_length_to_length_ratio=0.3)
        arrow3 = Arrow(start=LEFT * 1.5, end=LEFT * 1.5 + DOWN * 0.1, color=BLUE, stroke_width=4, max_tip_length_to_length_ratio=0.3)
        arrow4 = Arrow(start=DOWN * 1.5, end=DOWN * 1.5 + RIGHT * 0.1, color=BLUE, stroke_width=4, max_tip_length_to_length_ratio=0.3)
        
        feedback_visual = VGroup(arc1, arc2, arc3, arc4, arrow1, arrow2, arrow3, arrow4).shift(DOWN * 1)
        
        self.play(Write(interconnect_group))
        self.wait(2)
        self.play(Create(feedback_visual))
        self.wait(3)
        
        self.play(FadeOut(interconnect_group), FadeOut(feedback_visual))
        self.play(Write(solving_group))
        
        # Trajectory visualization
        trajectory_axes = Axes(
            x_range=[0, 5, 1],
            y_range=[0, 3, 1],
            x_length=6,
            y_length=3,
            axis_config={"color": WHITE}
        ).scale(0.7).shift(DOWN * 1.5)
        
        trajectory_func = lambda x: 0.5 * x**1.5
        trajectory = trajectory_axes.plot(trajectory_func, x_range=[0.1, 4], color=GREEN, stroke_width=4)
        
        x_label = Text("Time", font_size=20).next_to(trajectory_axes.x_axis, DOWN)
        y_label = Text("Position", font_size=20).next_to(trajectory_axes.y_axis, LEFT)
        
        self.wait(3)
        self.play(Create(trajectory_axes), Write(x_label), Write(y_label))
        self.play(Create(trajectory))
        self.wait(7)
        
        # Final message
        self.play(FadeOut(solving_group), FadeOut(trajectory_axes), FadeOut(trajectory), 
                 FadeOut(x_label), FadeOut(y_label))
        
        final_text1 = Text("We're not just finding a point,", font_size=36)
        final_text2 = Text("but charting a whole continuous process,", font_size=36)
        final_text3 = Text("and that's the beauty, and challenge,", font_size=36)
        final_text4 = Text("of differential equations.", font_size=36)
        
        final_group = VGroup(final_text1, final_text2, final_text3, final_text4).arrange(DOWN, buff=0.3)
        
        self.play(Write(final_group))
        self.wait(5)
        
        self.play(FadeOut(final_group))
