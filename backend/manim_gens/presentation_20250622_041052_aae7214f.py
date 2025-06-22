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

class StandingWaveScene(Scene):
    def construct(self):
        # [0:00] Imagine a jump rope, shaken just right.
        title = Text("Imagine a jump rope, shaken just right.", font_size=36)
        title.move_to(UP * 2)
        
        # Create a jump rope visualization
        rope_points = []
        for i in range(50):
            x = -6 + i * 0.24
            y = 0.5 * np.sin(2 * PI * x / 3)
            rope_points.append([x, y, 0])
        
        rope = VMobject()
        rope.set_points_smoothly(rope_points)
        rope.set_color(YELLOW)
        rope.set_stroke_width(6)
        
        self.play(Write(title))
        self.play(Create(rope))
        self.wait(5)
        
        # [0:05] See how the rope isn't traveling, but a pattern is?
        self.play(FadeOut(title))
        text1 = Text("See how the rope isn't traveling, but a pattern is?", font_size=36)
        text1.move_to(UP * 2)
        
        # Animate the rope showing standing wave pattern
        def update_rope(mob, dt):
            new_points = []
            for i in range(50):
                x = -6 + i * 0.24
                y = 0.8 * np.sin(2 * PI * x / 3) * np.cos(2 * PI * self.renderer.time * 2)
                new_points.append([x, y, 0])
            mob.set_points_smoothly(new_points)
        
        rope.add_updater(update_rope)
        
        self.play(Write(text1))
        self.wait(10)
        
        # [0:15] That's a standing wave – energy trapped in place.
        self.play(FadeOut(text1))
        text2 = Text("That's a standing wave – energy trapped in place.", font_size=36)
        text2.move_to(UP * 2)
        
        self.play(Write(text2))
        self.wait(10)
        
        # [0:25] It's the superposition of two waves, traveling in opposite directions
        self.play(FadeOut(text2))
        text3 = Text("It's the superposition of two waves, traveling in", font_size=32)
        text3_cont = Text("opposite directions, perfectly canceling their", font_size=32)
        text3_cont2 = Text("movement but reinforcing their amplitude.", font_size=32)
        
        text3.move_to(UP * 2.5)
        text3_cont.move_to(UP * 2)
        text3_cont2.move_to(UP * 1.5)
        
        # Remove the updater and show two traveling waves
        rope.clear_updaters()
        self.play(FadeOut(rope))
        
        # Create two traveling waves
        wave1_points = []
        wave2_points = []
        for i in range(50):
            x = -6 + i * 0.24
            y1 = 0.4 * np.sin(2 * PI * x / 3)
            y2 = 0.4 * np.sin(2 * PI * x / 3)
            wave1_points.append([x, y1 + 0.5, 0])
            wave2_points.append([x, y2 - 0.5, 0])
        
        wave1 = VMobject()
        wave1.set_points_smoothly(wave1_points)
        wave1.set_color(RED)
        wave1.set_stroke_width(4)
        
        wave2 = VMobject()
        wave2.set_points_smoothly(wave2_points)
        wave2.set_color(BLUE)
        wave2.set_stroke_width(4)
        
        # Add arrows to show direction
        arrow1 = Arrow(LEFT * 3, RIGHT * 3, color=RED).move_to(UP * 1)
        arrow2 = Arrow(RIGHT * 3, LEFT * 3, color=BLUE).move_to(DOWN * 1)
        
        self.play(Write(text3), Write(text3_cont), Write(text3_cont2))
        self.play(Create(wave1), Create(wave2))
        self.play(Create(arrow1), Create(arrow2))
        self.wait(10)
        
        # [0:35] Certain frequencies, determined by the rope's length, create these stable patterns.
        self.play(FadeOut(text3), FadeOut(text3_cont), FadeOut(text3_cont2))
        self.play(FadeOut(wave1), FadeOut(wave2), FadeOut(arrow1), FadeOut(arrow2))
        
        text4 = Text("Certain frequencies, determined by the rope's length,", font_size=32)
        text4_cont = Text("create these stable patterns.", font_size=32)
        text4.move_to(UP * 2.5)
        text4_cont.move_to(UP * 2)
        
        # Show different harmonics
        harmonics = VGroup()
        for n in range(1, 4):
            harmonic_points = []
            for i in range(50):
                x = -6 + i * 0.24
                y = 0.3 * np.sin(n * PI * (x + 6) / 12)
                harmonic_points.append([x, y + (3-n) * 0.8, 0])
            
            harmonic = VMobject()
            harmonic.set_points_smoothly(harmonic_points)
            harmonic.set_color([RED, GREEN, BLUE][n-1])
            harmonic.set_stroke_width(3)
            harmonics.add(harmonic)
        
        self.play(Write(text4), Write(text4_cont))
        self.play(Create(harmonics))
        self.wait(10)
        
        # Final text: Think of it as a resonant vibration – a harmonious dance of opposing forces.
        self.play(FadeOut(text4), FadeOut(text4_cont), FadeOut(harmonics))
        
        final_text = Text("Think of it as a resonant vibration –", font_size=32)
        final_text_cont = Text("a harmonious dance of opposing forces.", font_size=32)
        final_text.move_to(UP * 0.5)
        final_text_cont.move_to(DOWN * 0.5)
        
        # Create final standing wave animation
        final_rope_points = []
        for i in range(50):
            x = -6 + i * 0.24
            y = 0
            final_rope_points.append([x, y, 0])
        
        final_rope = VMobject()
        final_rope.set_points_smoothly(final_rope_points)
        final_rope.set_color(PURPLE)
        final_rope.set_stroke_width(6)
        
        def update_final_rope(mob, dt):
            new_points = []
            for i in range(50):
                x = -6 + i * 0.24
                y = 0.6 * np.sin(2 * PI * (x + 6) / 12) * np.cos(2 * PI * self.renderer.time * 1.5)
                new_points.append([x, y, 0])
            mob.set_points_smoothly(new_points)
        
        final_rope.add_updater(update_final_rope)
        
        self.play(Write(final_text), Write(final_text_cont))
        self.play(Create(final_rope))
        self.wait(5)
        
        # Clear everything at the end
        self.play(FadeOut(final_text), FadeOut(final_text_cont), FadeOut(final_rope))
