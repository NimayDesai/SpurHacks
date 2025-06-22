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

class QuadraticEssence(Scene):
    def construct(self):
        # Initial scene: Imagine throwing a ball
        ball_text = Text("Imagine throwing a ball.", font_size=48)
        self.play(Write(ball_text))
        self.wait(1)
        
        # Create a simple ball trajectory visualization
        ball = Circle(radius=0.15, color=RED, fill_opacity=1)
        ball.move_to(LEFT * 5 + DOWN * 2)
        
        # Parabolic path
        path = ParametricFunction(
            lambda t: np.array([t, -0.3 * t**2 + 2, 0]),
            t_range=[-4, 4],
            color=YELLOW,
            stroke_width=3
        )
        
        self.play(FadeOut(ball_text))
        self.play(Create(path))
        self.play(MoveAlongPath(ball, path), run_time=2)
        self.wait(0.5)
        
        # [0:05] timestamp
        parabola_text = Text("Its path, a parabola, embodies the essence of quadratics", font_size=36)
        parabola_text.to_edge(UP)
        self.play(Write(parabola_text))
        self.wait(2)
        
        # Clear for next section
        self.play(FadeOut(ball), FadeOut(path), FadeOut(parabola_text))
        
        # [0:12] timestamp - These aren't just curves
        curves_text = Text("These aren't just curves; they're equations describing how", font_size=36)
        curves_text2 = Text("a quantity changes at a *constant rate of change*.", font_size=36)
        curves_group = VGroup(curves_text, curves_text2)
        curves_group.arrange(DOWN, buff=0.3)
        
        self.play(Write(curves_text))
        self.wait(1)
        self.play(Write(curves_text2))
        self.wait(3)
        
        # Show a coordinate plane with parabola
        plane = NumberPlane(
            x_range=[-3, 3, 1],
            y_range=[-1, 5, 1],
            x_length=6,
            y_length=4,
            background_line_style={"stroke_opacity": 0.3}
        )
        
        parabola = plane.plot(
            lambda x: x**2,
            x_range=[-2.5, 2.5],
            color=BLUE,
            stroke_width=4
        )
        
        self.play(FadeOut(curves_group))
        self.play(Create(plane))
        self.play(Create(parabola))
        self.wait(2)
        
        # [0:20] timestamp - Think of it
        think_text = Text("Think of it: velocity affects position, acceleration affects", font_size=32)
        think_text2 = Text("velocity—a chain reaction elegantly captured by the x-squared term.", font_size=32)
        think_group = VGroup(think_text, think_text2)
        think_group.arrange(DOWN, buff=0.3)
        think_group.to_edge(UP)
        
        self.play(Write(think_text))
        self.wait(1)
        self.play(Write(think_text2))
        self.wait(3)
        
        # Highlight the x-squared relationship
        x_squared_text = Text("x²", font_size=48, color=RED)
        x_squared_text.next_to(parabola, RIGHT, buff=1)
        
        self.play(Write(x_squared_text))
        self.wait(2)
        
        # Clear for final section
        self.play(FadeOut(think_group), FadeOut(x_squared_text))
        
        # [0:30] timestamp - Final message
        special_text = Text("So, what's special about *x* squared? It's a reflection of this", font_size=32)
        special_text2 = Text("nested dependency, revealing a fundamental relationship", font_size=32)
        special_text3 = Text("between rates of change, and thus, shaping the world around us.", font_size=32)
        
        special_group = VGroup(special_text, special_text2, special_text3)
        special_group.arrange(DOWN, buff=0.3)
        special_group.to_edge(UP)
        
        self.play(Write(special_text))
        self.wait(1)
        self.play(Write(special_text2))
        self.wait(1)
        self.play(Write(special_text3))
        self.wait(3)
        
        # Final emphasis on the parabola
        self.play(parabola.animate.set_color(YELLOW), run_time=1)
        self.wait(2)
        
        # Clear everything
        self.play(FadeOut(special_group), FadeOut(plane), FadeOut(parabola))
        self.wait(1)
