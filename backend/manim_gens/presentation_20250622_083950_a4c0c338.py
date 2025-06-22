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

class ElectronWaves(Scene):
    def construct(self):
        # [0:00] - Initial text about electrons as probability clouds
        text1 = Text("Imagine electrons not as tiny planets orbiting a nucleus,", font_size=36)
        text2 = Text("but as fuzzy clouds of probability.", font_size=36)
        text1.move_to(UP * 0.5)
        text2.move_to(DOWN * 0.5)
        
        # Visual: Fuzzy probability cloud around nucleus
        nucleus = Circle(radius=0.2, color=RED, fill_opacity=1)
        nucleus.move_to(ORIGIN)
        
        # Create fuzzy electron cloud
        cloud_points = []
        for i in range(200):
            angle = i * 0.1
            r = 1.5 + 0.5 * np.sin(3 * angle) + 0.3 * np.random.random()
            x = r * np.cos(angle)
            y = r * np.sin(angle)
            cloud_points.append([x, y, 0])
        
        cloud_dots = VGroup(*[Dot(point, radius=0.02, color=BLUE, fill_opacity=0.3) 
                             for point in cloud_points])
        cloud_dots.move_to(RIGHT * 3)
        nucleus.move_to(RIGHT * 3)
        
        self.play(Write(text1), Write(text2))
        self.play(FadeIn(nucleus), FadeIn(cloud_dots))
        self.wait(1)
        
        # [0:05] - Transition to quantum leap concept
        self.play(FadeOut(text1), FadeOut(text2), FadeOut(nucleus), FadeOut(cloud_dots))
        
        text3 = Text("This is the quantum leap: electrons exist in specific energy levels,", font_size=36)
        text4 = Text("like rungs on a ladder, not anywhere in between.", font_size=36)
        text3.move_to(UP * 0.5)
        text4.move_to(DOWN * 0.5)
        
        # Visual: Energy level ladder
        ladder = VGroup()
        for i in range(5):
            rung = Line(LEFT * 2, RIGHT * 2, color=WHITE, stroke_width=4)
            rung.move_to(UP * (i - 2) * 1.2)
            ladder.add(rung)
        
        # Add energy level labels
        for i, rung in enumerate(ladder):
            level_text = Text(f"n={i+1}", font_size=24, color=YELLOW)
            level_text.next_to(rung, LEFT)
            ladder.add(level_text)
        
        ladder.move_to(RIGHT * 3)
        
        self.play(Write(text3), Write(text4))
        self.play(Create(ladder))
        self.wait(5)
        
        # [0:15] - Transition to bonding concept
        self.play(FadeOut(text3), FadeOut(text4), FadeOut(ladder))
        
        text5 = Text("These energy levels dictate how atoms interact,", font_size=36)
        text6 = Text("forming bonds that are governed by the wave-like nature of electrons.", font_size=36)
        text5.move_to(UP * 0.5)
        text6.move_to(DOWN * 0.5)
        
        # Visual: Two atoms with overlapping electron waves
        atom1 = Circle(radius=0.3, color=RED, fill_opacity=1)
        atom2 = Circle(radius=0.3, color=BLUE, fill_opacity=1)
        atom1.move_to(LEFT * 2 + RIGHT * 3)
        atom2.move_to(RIGHT * 2 + RIGHT * 3)
        
        # Wave-like electron representation
        wave1 = FunctionGraph(
            lambda x: 0.3 * np.sin(4 * x), 
            x_range=[-2, 2], 
            color=YELLOW,
            stroke_width=3
        )
        wave2 = FunctionGraph(
            lambda x: 0.3 * np.cos(4 * x), 
            x_range=[-2, 2], 
            color=GREEN,
            stroke_width=3
        )
        wave1.move_to(RIGHT * 3)
        wave2.move_to(RIGHT * 3 + UP * 0.5)
        
        self.play(Write(text5), Write(text6))
        self.play(FadeIn(atom1), FadeIn(atom2))
        self.play(Create(wave1), Create(wave2))
        self.wait(5)
        
        # [0:25] - Transition to chemical reactions
        self.play(FadeOut(text5), FadeOut(text6), FadeOut(atom1), FadeOut(atom2), 
                 FadeOut(wave1), FadeOut(wave2))
        
        text7 = Text("So, chemical reactions aren't just billiard balls colliding;", font_size=36)
        text8 = Text("they're intricate dances of probability waves,", font_size=36)
        text9 = Text("merging and separating to create new arrangements of matter.", font_size=36)
        text7.move_to(UP * 1)
        text8.move_to(ORIGIN)
        text9.move_to(DOWN * 1)
        
        # Visual: Wave interference pattern
        plane = NumberPlane(
            x_range=[-4, 4], y_range=[-3, 3],
            x_length=6, y_length=4,
            background_line_style={"stroke_opacity": 0.3}
        )
        plane.move_to(RIGHT * 3)
        
        # Create interference pattern
        wave_func = lambda x: 0.5 * np.sin(2 * x) + 0.3 * np.cos(3 * x)
        wave_curve = plane.plot(
            wave_func,
            x_range=[-4, 4],
            color=PURPLE,
            stroke_width=4
        )
        
        self.play(Write(text7), Write(text8), Write(text9))
        self.play(Create(plane), Create(wave_curve))
        self.wait(5)
        
        # [0:35] - Final fade out
        self.play(FadeOut(text7), FadeOut(text8), FadeOut(text9), 
                 FadeOut(plane), FadeOut(wave_curve))
        self.wait(1)
