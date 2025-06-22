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

class LimitsIntroScene(Scene):
    def construct(self):
        # [0:00] - [0:05] We often think of limits as boundaries, but what does that really mean?
        title_text = Text("We often think of limits as boundaries,", font_size=36)
        subtitle_text = Text("but what does that really mean?", font_size=36)
        title_group = VGroup(title_text, subtitle_text).arrange(DOWN, buff=0.3)
        
        self.play(Write(title_group))
        self.wait(5)
        
        # [0:05] - [0:12] Imagine zooming in on a curve approaching a point. Does it settle on a single value?
        self.play(FadeOut(title_group))
        
        zoom_text1 = Text("Imagine zooming in on a curve", font_size=36)
        zoom_text2 = Text("approaching a point.", font_size=36)
        zoom_text3 = Text("Does it settle on a single value?", font_size=36)
        zoom_group = VGroup(zoom_text1, zoom_text2, zoom_text3).arrange(DOWN, buff=0.3)
        
        # Create a curve and point visualization
        plane = NumberPlane(
            x_range=[-3, 3, 1],
            y_range=[-2, 4, 1],
            x_length=6,
            y_length=4,
            background_line_style={"stroke_opacity": 0.3}
        ).scale(0.7).shift(DOWN * 0.5)
        
        def curve_func(x):
            return (x**2 - 1) / (x - 1) if x != 1 else 2
        
        curve = plane.plot(
            lambda x: x + 1,
            x_range=[-2.5, 0.99],
            color=BLUE,
            stroke_width=3
        )
        
        curve2 = plane.plot(
            lambda x: x + 1,
            x_range=[1.01, 2.5],
            color=BLUE,
            stroke_width=3
        )
        
        point = Dot(plane.c2p(1, 2), color=RED, radius=0.08)
        
        self.play(Write(zoom_group[:2]))
        self.play(Create(plane), Create(curve), Create(curve2), Create(point))
        self.play(Write(zoom_group[2]))
        self.wait(7)
        
        # [0:12] - [0:20] That's the core idea: a limit describes what a function *approaches*
        self.play(FadeOut(zoom_group), FadeOut(plane), FadeOut(curve), FadeOut(curve2), FadeOut(point))
        
        core_text1 = Text("That's the core idea: a limit describes", font_size=36)
        core_text2 = Text("what a function *approaches* as its input", font_size=36)
        core_text3 = Text("gets arbitrarily close to some value,", font_size=36)
        core_text4 = Text("not necessarily what it *equals* at that point.", font_size=36)
        core_group = VGroup(core_text1, core_text2, core_text3, core_text4).arrange(DOWN, buff=0.3)
        
        self.play(Write(core_group))
        self.wait(8)
        
        # [0:20] - [0:27] The function might not even be defined there, but the limit still might exist.
        self.play(FadeOut(core_group))
        
        undefined_text1 = Text("The function might not even be defined there,", font_size=36)
        undefined_text2 = Text("but the limit still might exist.", font_size=36)
        undefined_group = VGroup(undefined_text1, undefined_text2).arrange(DOWN, buff=0.3)
        
        # Show a function with a hole
        plane2 = NumberPlane(
            x_range=[-3, 3, 1],
            y_range=[-2, 4, 1],
            x_length=6,
            y_length=4,
            background_line_style={"stroke_opacity": 0.3}
        ).scale(0.6).shift(DOWN * 1)
        
        curve_with_hole1 = plane2.plot(
            lambda x: x + 1,
            x_range=[-2.5, 0.99],
            color=BLUE,
            stroke_width=3
        )
        
        curve_with_hole2 = plane2.plot(
            lambda x: x + 1,
            x_range=[1.01, 2.5],
            color=BLUE,
            stroke_width=3
        )
        
        hole = Circle(radius=0.08, color=WHITE, fill_opacity=1).move_to(plane2.c2p(1, 2))
        hole_outline = Circle(radius=0.08, color=BLUE, fill_opacity=0, stroke_width=2).move_to(plane2.c2p(1, 2))
        
        self.play(Write(undefined_group))
        self.play(Create(plane2), Create(curve_with_hole1), Create(curve_with_hole2))
        self.play(Create(hole), Create(hole_outline))
        self.wait(7)
        
        # [0:27] - [0:34] It's about the trend, the destination, not the final stop.
        self.play(FadeOut(undefined_group), FadeOut(plane2), FadeOut(curve_with_hole1), 
                 FadeOut(curve_with_hole2), FadeOut(hole), FadeOut(hole_outline))
        
        final_text1 = Text("It's about the trend, the destination,", font_size=40)
        final_text2 = Text("not the final stop.", font_size=40)
        final_group = VGroup(final_text1, final_text2).arrange(DOWN, buff=0.4)
        
        self.play(Write(final_group))
        self.wait(7)
        
        self.play(FadeOut(final_group))
