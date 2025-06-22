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

class RotationalInertiaScene(Scene):
    def construct(self):
        # [0:00] - Imagine a spinning wheel
        wheel = Circle(radius=1.5, color=BLUE, stroke_width=6)
        spokes = VGroup()
        for i in range(8):
            angle = i * PI / 4
            spoke = Line(
                wheel.get_center(), 
                wheel.get_center() + 1.5 * np.array([np.cos(angle), np.sin(angle), 0]),
                color=GRAY,
                stroke_width=3
            )
            spokes.add(spoke)
        
        spinning_wheel = VGroup(wheel, spokes)
        spinning_wheel.move_to(UP * 1.5)
        
        text1 = Text("Imagine a spinning wheel.", font_size=36)
        text1.to_edge(DOWN)
        
        self.play(Write(text1))
        self.play(FadeIn(spinning_wheel))
        self.play(Rotate(spinning_wheel, 4*PI, run_time=3))
        self.wait(2)
        
        # [0:05] - Its speed affects how much it resists changes
        self.play(FadeOut(text1))
        text2 = Text("Its speed affects how much it resists changes in its rotation, right?", font_size=32)
        text2.to_edge(DOWN)
        
        self.play(Write(text2))
        
        # Show different spinning speeds
        self.play(Rotate(spinning_wheel, 2*PI, run_time=4))  # slower
        self.play(Rotate(spinning_wheel, 2*PI, run_time=1))  # faster
        self.wait(2)
        
        # [0:12] - That's rotational inertia
        self.play(FadeOut(text2))
        text3 = Text("That's rotational inertia.", font_size=36)
        text3.to_edge(DOWN)
        
        self.play(Write(text3))
        self.wait(5)
        
        # [0:12] - But it's not just speed; the mass distribution matters
        self.play(FadeOut(text3))
        text4 = Text("But it's not just speed; the mass distribution matters.", font_size=32)
        text4.to_edge(DOWN)
        
        self.play(Write(text4))
        
        # Show two different wheels - one with mass at rim, one with mass at center
        self.play(FadeOut(spinning_wheel))
        
        # Heavy rim wheel
        heavy_rim = Circle(radius=1.2, color=RED, stroke_width=12)
        heavy_rim.move_to(LEFT * 2.5 + UP * 0.5)
        heavy_rim_label = Text("Heavy rim", font_size=24, color=RED)
        heavy_rim_label.next_to(heavy_rim, DOWN)
        
        # Light rim wheel
        light_rim = Circle(radius=1.2, color=BLUE, stroke_width=4)
        light_center = Circle(radius=0.3, color=BLUE, fill_opacity=0.8)
        light_wheel = VGroup(light_rim, light_center)
        light_wheel.move_to(RIGHT * 2.5 + UP * 0.5)
        light_rim_label = Text("Light rim", font_size=24, color=BLUE)
        light_rim_label.next_to(light_wheel, DOWN)
        
        self.play(FadeIn(heavy_rim), FadeIn(heavy_rim_label))
        self.play(FadeIn(light_wheel), FadeIn(light_rim_label))
        self.wait(3)
        
        # [0:20] - A heavy rim resists changes more than a light one
        self.play(FadeOut(text4))
        text5 = Text("A heavy rim resists changes more than a light one.", font_size=32)
        text5.to_edge(DOWN)
        
        self.play(Write(text5))
        self.wait(8)
        
        # [0:20] - So rotational inertia isn't simply mass
        self.play(FadeOut(text5))
        self.play(FadeOut(heavy_rim), FadeOut(heavy_rim_label))
        self.play(FadeOut(light_wheel), FadeOut(light_rim_label))
        
        text6 = Text("So rotational inertia isn't simply mass,", font_size=32)
        text6.move_to(UP * 1)
        
        text7 = Text("it's how that mass is arranged,", font_size=32)
        text7.move_to(ORIGIN)
        
        text8 = Text("a measure of an object's resistance to changes in its spin.", font_size=28)
        text8.move_to(DOWN * 1)
        
        self.play(Write(text6))
        self.play(Write(text7))
        self.play(Write(text8))
        self.wait(5)
        
        # [0:30] - Think of it as the "spin-laziness" of an object
        self.play(FadeOut(text6), FadeOut(text7), FadeOut(text8))
        
        text9 = Text('Think of it as the "spin-laziness" of an object.', font_size=36)
        text9.move_to(ORIGIN)
        
        # Show a lazy spinning object
        lazy_wheel = Circle(radius=1, color=YELLOW, stroke_width=8)
        lazy_wheel.move_to(UP * 1.5)
        
        self.play(Write(text9))
        self.play(FadeIn(lazy_wheel))
        
        # Show very slow, reluctant rotation
        self.play(Rotate(lazy_wheel, PI/2, run_time=3, rate_func=there_and_back))
        self.play(Rotate(lazy_wheel, -PI/4, run_time=2))
        self.wait(2)
        
        # Final clear
        self.play(FadeOut(text9), FadeOut(lazy_wheel))
        self.wait(1)
