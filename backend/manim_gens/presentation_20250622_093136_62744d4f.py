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

class ProjectileMotion(Scene):
    def construct(self):
        # [0:00] Imagine launching a ball.
        title = Text("Imagine launching a ball.", font_size=36)
        self.play(Write(title))
        
        # Create a ball
        ball = Circle(radius=0.2, color=BLUE, fill_opacity=1)
        ball.move_to(LEFT * 5 + DOWN * 2)
        self.play(FadeIn(ball))
        self.wait(1)
        
        # [0:05] Gravity pulls it down, constantly accelerating it vertically.
        self.play(FadeOut(title))
        gravity_text = Text("Gravity pulls it down, constantly accelerating it vertically.", font_size=32)
        gravity_text.to_edge(UP)
        self.play(Write(gravity_text))
        
        # Show gravity arrow
        gravity_arrow = Arrow(start=UP, end=DOWN, color=RED, stroke_width=6)
        gravity_arrow.next_to(ball, UP)
        self.play(FadeIn(gravity_arrow))
        self.wait(2)
        
        # [0:10] But what about horizontally?
        self.play(FadeOut(gravity_text), FadeOut(gravity_arrow))
        horizontal_text = Text("But what about horizontally?", font_size=32)
        horizontal_text.to_edge(UP)
        self.play(Write(horizontal_text))
        
        # Show horizontal arrow
        horizontal_arrow = Arrow(start=LEFT, end=RIGHT, color=GREEN, stroke_width=6)
        horizontal_arrow.next_to(ball, UP)
        self.play(FadeIn(horizontal_arrow))
        self.wait(2)
        
        # [0:15] Ignoring air resistance, its horizontal speed remains constant.
        self.play(FadeOut(horizontal_text), FadeOut(horizontal_arrow))
        constant_text = Text("Ignoring air resistance, its horizontal speed remains constant.", font_size=28)
        constant_text.to_edge(UP)
        self.play(Write(constant_text))
        
        # Show constant horizontal motion
        horizontal_velocity_arrow = Arrow(start=ORIGIN, end=RIGHT*2, color=GREEN, stroke_width=4)
        horizontal_velocity_arrow.next_to(ball, RIGHT)
        self.play(FadeIn(horizontal_velocity_arrow))
        self.wait(2)
        
        # [0:20] See how these independent motions combine? The ball traces a curved path, a parabola.
        self.play(FadeOut(constant_text), FadeOut(horizontal_velocity_arrow))
        combine_text = Text("See how these independent motions combine?", font_size=28)
        combine_text.to_edge(UP)
        parabola_text = Text("The ball traces a curved path, a parabola.", font_size=28)
        parabola_text.next_to(combine_text, DOWN)
        
        self.play(Write(combine_text))
        self.play(Write(parabola_text))
        
        # Reset ball position and show parabolic motion
        ball.move_to(LEFT * 5 + DOWN * 2)
        
        # Create coordinate system
        axes = Axes(
            x_range=[-6, 6, 1],
            y_range=[-3, 3, 1],
            x_length=10,
            y_length=6,
            axis_config={"color": GRAY}
        )
        
        # Define parabolic path
        def parabola_func(x):
            return -0.1 * (x + 5) ** 2 + 2
        
        parabola = axes.plot(
            parabola_func,
            x_range=[-5, 5],
            color=YELLOW,
            stroke_width=4
        )
        
        self.play(Create(axes))
        self.play(Create(parabola))
        
        # Animate ball along parabola
        self.play(
            MoveAlongPath(ball, parabola),
            run_time=3
        )
        self.wait(1)
        
        # [0:25] It's the beautiful interplay of a constant horizontal velocity and a constantly changing vertical velocity.
        self.play(FadeOut(combine_text), FadeOut(parabola_text))
        interplay_text = Text("It's the beautiful interplay of a constant horizontal velocity", font_size=24)
        interplay_text.to_edge(UP)
        interplay_text2 = Text("and a constantly changing vertical velocity.", font_size=24)
        interplay_text2.next_to(interplay_text, DOWN)
        
        self.play(Write(interplay_text))
        self.play(Write(interplay_text2))
        
        # Show velocity components
        h_velocity = Arrow(start=ORIGIN, end=RIGHT*1.5, color=GREEN, stroke_width=4)
        v_velocity = Arrow(start=ORIGIN, end=DOWN*1, color=RED, stroke_width=4)
        h_velocity.move_to(ball.get_center() + RIGHT*0.8)
        v_velocity.move_to(ball.get_center() + DOWN*0.6)
        
        h_label = Text("Constant", font_size=16, color=GREEN)
        h_label.next_to(h_velocity, UP, buff=0.1)
        v_label = Text("Changing", font_size=16, color=RED)
        v_label.next_to(v_velocity, RIGHT, buff=0.1)
        
        self.play(FadeIn(h_velocity), FadeIn(v_velocity))
        self.play(Write(h_label), Write(v_label))
        self.wait(2)
        
        # [0:30] This seemingly complex motion is just two simple motions working together.
        self.play(
            FadeOut(interplay_text), 
            FadeOut(interplay_text2),
            FadeOut(h_velocity),
            FadeOut(v_velocity),
            FadeOut(h_label),
            FadeOut(v_label)
        )
        
        final_text = Text("This seemingly complex motion is just two simple", font_size=28)
        final_text.to_edge(UP)
        final_text2 = Text("motions working together.", font_size=28)
        final_text2.next_to(final_text, DOWN)
        
        self.play(Write(final_text))
        self.play(Write(final_text2))
        self.wait(2)
        
        # Final cleanup
        self.play(
            FadeOut(final_text),
            FadeOut(final_text2),
            FadeOut(ball),
            FadeOut(axes),
            FadeOut(parabola)
        )
