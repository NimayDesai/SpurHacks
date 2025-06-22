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

class CannonballOrbit(Scene):
    def construct(self):
        # [0:00] - Opening
        title = Text("Imagine a cannonball.", font_size=48).move_to(UP * 2)
        
        # Create Earth (circle)
        earth = Circle(radius=1.5, color=BLUE, fill_opacity=0.3).move_to(DOWN * 0.5)
        earth_label = Text("Earth", font_size=24, color=WHITE).next_to(earth, DOWN, buff=0.3)
        
        # Create cannon on Earth's surface
        cannon_pos = earth.point_at_angle(PI/4)
        cannon = Rectangle(width=0.3, height=0.1, color=GRAY, fill_opacity=1).move_to(cannon_pos)
        cannon.rotate(PI/4)
        
        self.play(Write(title))
        self.play(FadeIn(earth), Write(earth_label), FadeIn(cannon))
        
        self.wait(2)  # Wait until [0:05]
        
        # [0:05] - "Fired gently, it falls to Earth"
        self.play(FadeOut(title))
        text1 = Text("Fired gently, it falls to Earth.", font_size=36).move_to(UP * 2.5)
        self.play(Write(text1))
        
        # Show gentle trajectory
        cannonball1 = Dot(radius=0.08, color=RED).move_to(cannon_pos)
        gentle_path = Arc(start_angle=PI/4, angle=-PI/3, radius=2, color=RED_A, stroke_width=2)
        gentle_path.move_arc_center_to(cannon_pos + LEFT * 0.8 + DOWN * 0.8)
        
        self.play(FadeIn(cannonball1))
        self.play(MoveAlongPath(cannonball1, gentle_path), Create(gentle_path), run_time=2)
        self.play(FadeOut(cannonball1))
        
        # [0:08] - "Fired harder, it travels further before landing"
        text2 = Text("Fired harder, it travels further before landing.", font_size=36).move_to(UP * 2.5)
        self.play(Transform(text1, text2))
        
        # Show harder trajectory
        cannonball2 = Dot(radius=0.08, color=RED).move_to(cannon_pos)
        harder_path = Arc(start_angle=PI/4, angle=-PI/2, radius=3, color=ORANGE, stroke_width=2)
        harder_path.move_arc_center_to(cannon_pos + LEFT * 1.5 + DOWN * 1.5)
        
        self.play(FadeIn(cannonball2))
        self.play(MoveAlongPath(cannonball2, harder_path), Create(harder_path), run_time=2.5)
        self.play(FadeOut(cannonball2))
        
        self.wait(2)  # Wait until [0:15]
        
        # [0:15] - "But what if we fired it *so* hard?"
        text3 = Text("But what if we fired it *so* hard?", font_size=36).move_to(UP * 2.5)
        self.play(Transform(text1, text3))
        
        self.wait(2)  # Wait until [0:20]
        
        # [0:20] - "Fast enough that the Earth curves away beneath it as quickly as it falls"
        text4 = Text("Fast enough that the Earth curves away beneath it\nas quickly as it falls.", font_size=32).move_to(UP * 2.8)
        self.play(Transform(text1, text4))
        
        # Show orbital trajectory
        cannonball3 = Dot(radius=0.08, color=YELLOW).move_to(cannon_pos)
        orbital_path = Circle(radius=2.2, color=YELLOW, stroke_width=3).move_to(earth.get_center())
        
        self.play(FadeIn(cannonball3))
        self.play(Create(orbital_path), run_time=1)
        self.play(MoveAlongPath(cannonball3, orbital_path), run_time=4)
        
        self.wait(3)  # Wait until [0:28]
        
        # [0:28] - "That's orbit! It's not escaping gravity; it's constantly *falling* around the Earth. A beautiful, perpetual freefall."
        self.play(FadeOut(text1))
        text5 = Text("That's orbit!", font_size=42, color=YELLOW).move_to(UP * 3)
        text6 = Text("It's not escaping gravity; it's constantly", font_size=28).move_to(UP * 2.2)
        text7 = Text("*falling* around the Earth.", font_size=28).move_to(UP * 1.8)
        text8 = Text("A beautiful, perpetual freefall.", font_size=32, color=LIGHT_PINK).move_to(UP * 1.2)
        
        self.play(Write(text5))
        self.play(Write(text6))
        self.play(Write(text7))
        self.play(Write(text8))
        
        # Continue orbital motion
        self.play(MoveAlongPath(cannonball3, orbital_path), run_time=3)
        
        # Final fade out
        self.play(
            FadeOut(earth),
            FadeOut(earth_label),
            FadeOut(cannon),
            FadeOut(cannonball3),
            FadeOut(orbital_path),
            FadeOut(gentle_path),
            FadeOut(harder_path),
            FadeOut(text5),
            FadeOut(text6),
            FadeOut(text7),
            FadeOut(text8)
        )
