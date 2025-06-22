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

class PendulumMotion(Scene):
    def construct(self):
        # [0:00] - Imagine a pendulum swinging
        pendulum_text = Text("Imagine a pendulum swinging.", font_size=36)
        pendulum_text.move_to(UP * 2)
        
        # Create pendulum visual
        pivot = Dot(UP * 2, color=BLACK)
        string_length = 3
        pendulum_string = Line(UP * 2, UP * 2 + DOWN * string_length, color=GRAY)
        pendulum_bob = Circle(radius=0.2, color=BLUE, fill_opacity=1)
        pendulum_bob.move_to(UP * 2 + DOWN * string_length)
        
        pendulum_group = VGroup(pivot, pendulum_string, pendulum_bob)
        
        self.play(Write(pendulum_text))
        self.play(Create(pendulum_group))
        
        # Animate pendulum swinging
        def update_pendulum(mob, dt):
            angle = 0.8 * np.sin(2 * self.renderer.time)
            new_bob_pos = UP * 2 + string_length * (np.sin(angle) * RIGHT + np.cos(angle) * DOWN)
            pendulum_bob.move_to(new_bob_pos)
            pendulum_string.put_start_and_end_on(UP * 2, new_bob_pos)
        
        pendulum_bob.add_updater(update_pendulum)
        pendulum_string.add_updater(lambda m, dt: None)
        
        self.wait(5)
        
        # [0:05] - Its motion repeats, right?
        self.play(FadeOut(pendulum_text))
        repeat_text = Text("Its motion repeats, right?", font_size=36)
        repeat_text.move_to(UP * 2)
        self.play(Write(repeat_text))
        self.wait(5)
        
        # [0:10] - That's because gravity constantly pulls it back towards its resting point
        self.play(FadeOut(repeat_text))
        gravity_text = Text("That's because gravity constantly pulls it back\ntowards its resting point.", font_size=32)
        gravity_text.move_to(UP * 2.5)
        
        # Add gravity arrow
        gravity_arrow = Arrow(pendulum_bob.get_center() + UP * 0.5, pendulum_bob.get_center() + DOWN * 0.5, color=RED)
        gravity_label = Text("Gravity", font_size=24, color=RED)
        gravity_label.next_to(gravity_arrow, RIGHT)
        
        # Add resting point indicator
        rest_point = Dot(UP * 2 + DOWN * string_length, color=GREEN)
        rest_label = Text("Resting Point", font_size=24, color=GREEN)
        rest_label.move_to(DOWN * 2.5)
        
        self.play(Write(gravity_text))
        self.play(Create(gravity_arrow), Write(gravity_label))
        self.play(Create(rest_point), Write(rest_label))
        self.wait(5)
        
        # [0:15] - But inertia keeps it moving past that point
        self.play(FadeOut(gravity_text), FadeOut(gravity_arrow), FadeOut(gravity_label), FadeOut(rest_point), FadeOut(rest_label))
        inertia_text = Text("But inertia keeps it moving past that point.", font_size=36)
        inertia_text.move_to(UP * 2)
        
        # Add velocity vector
        velocity_arrow = Arrow(ORIGIN, RIGHT * 1.5, color=BLUE)
        velocity_arrow.add_updater(lambda m: m.move_to(pendulum_bob.get_center()))
        velocity_label = Text("Inertia", font_size=24, color=BLUE)
        velocity_label.add_updater(lambda m: m.next_to(velocity_arrow, UP))
        
        self.play(Write(inertia_text))
        self.play(Create(velocity_arrow), Write(velocity_label))
        self.wait(5)
        
        # [0:20] - This tug-of-war between restorative force and momentum creates a beautiful cycle: harmonic motion
        self.play(FadeOut(inertia_text), FadeOut(velocity_arrow), FadeOut(velocity_label))
        harmonic_text = Text("This tug-of-war between restorative force and momentum\ncreates a beautiful cycle: harmonic motion.", font_size=32)
        harmonic_text.move_to(UP * 2.5)
        
        # Create sine wave to represent harmonic motion
        axes = Axes(
            x_range=[0, 4*PI, PI/2],
            y_range=[-2, 2, 1],
            x_length=6,
            y_length=3,
            axis_config={"include_tip": False}
        ).move_to(DOWN * 1.5)
        
        sine_curve = axes.plot(
            lambda x: np.sin(x),
            x_range=[0, 4*PI],
            color=YELLOW,
            stroke_width=4
        )
        
        wave_label = Text("Harmonic Motion", font_size=24, color=YELLOW)
        wave_label.next_to(axes, DOWN)
        
        self.play(Write(harmonic_text))
        self.play(Create(axes), Create(sine_curve), Write(wave_label))
        self.wait(5)
        
        # [0:25] - The further it swings, the stronger gravity pulls, speeding up the return
        self.play(FadeOut(harmonic_text))
        force_text = Text("The further it swings, the stronger gravity pulls,\nspeeding up the return.", font_size=32)
        force_text.move_to(UP * 2.5)
        
        self.play(Write(force_text))
        self.wait(5)
        
        # [0:30] - This isn't limited to pendulums; springs, even atoms, exhibit this same dance of opposing forces. It's the fundamental rhythm of the universe.
        pendulum_bob.clear_updaters()
        pendulum_string.clear_updaters()
        
        self.play(FadeOut(force_text), FadeOut(pendulum_group), FadeOut(axes), FadeOut(sine_curve), FadeOut(wave_label))
        
        final_text = Text("This isn't limited to pendulums; springs, even atoms,\nexhibit this same dance of opposing forces.\nIt's the fundamental rhythm of the universe.", font_size=32)
        final_text.move_to(ORIGIN)
        
        # Create visual representations
        spring = VGroup()
        for i in range(10):
            coil = Circle(radius=0.1, color=GREEN)
            coil.move_to(LEFT * 3 + UP * (i * 0.3 - 1.5))
            spring.add(coil)
        
        atom = VGroup()
        nucleus = Circle(radius=0.15, color=RED, fill_opacity=1)
        electron_orbit = Circle(radius=0.8, color=BLUE, stroke_width=2)
        electron = Circle(radius=0.05, color=BLUE, fill_opacity=1)
        electron.move_to(electron_orbit.point_at_angle(0))
        atom.add(nucleus, electron_orbit, electron)
        atom.move_to(RIGHT * 3)
        
        universe_dots = VGroup()
        for i in range(20):
            dot = Dot(color=WHITE, radius=0.03)
            dot.move_to([
                np.random.uniform(-6, 6),
                np.random.uniform(-3, 3),
                0
            ])
            universe_dots.add(dot)
        
        self.play(Write(final_text))
        self.play(Create(spring), Create(atom), Create(universe_dots))
        self.wait(5)
        
        # Clear everything at the end
        self.play(FadeOut(final_text), FadeOut(spring), FadeOut(atom), FadeOut(universe_dots))
