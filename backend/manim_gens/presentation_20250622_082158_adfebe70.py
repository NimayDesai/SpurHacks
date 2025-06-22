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

class WaterContainerArithmetic(Scene):
    def construct(self):
        # Initial text about pouring water
        initial_text = Text("Imagine pouring water into a container.")
        self.play(Write(initial_text))
        self.wait(2)
        
        # Create container and initial water
        container = Rectangle(width=3, height=4, color=WHITE, stroke_width=3)
        container.shift(DOWN * 0.5)
        
        # Initial water level
        water = Rectangle(width=2.8, height=1, color=BLUE, fill_opacity=0.7)
        water.align_to(container, DOWN)
        water.shift(UP * 0.1)
        
        self.play(FadeOut(initial_text))
        self.play(Create(container), FadeIn(water))
        
        # [0:05] Addition text and visual
        addition_text = Text("Addition? That's simply pouring more water in – increasing the total amount.")
        addition_text.scale(0.7)
        addition_text.to_edge(UP)
        
        self.play(Write(addition_text))
        
        # Show water level rising (addition)
        new_water = Rectangle(width=2.8, height=2, color=BLUE, fill_opacity=0.7)
        new_water.align_to(container, DOWN)
        new_water.shift(UP * 0.1)
        
        self.play(Transform(water, new_water))
        self.wait(1)
        
        # [0:10] Subtraction text and visual
        self.play(FadeOut(addition_text))
        subtraction_text = Text("Subtraction? It's the opposite; we're taking some water out, decreasing the total.")
        subtraction_text.scale(0.7)
        subtraction_text.to_edge(UP)
        
        self.play(Write(subtraction_text))
        
        # Show water level falling (subtraction)
        less_water = Rectangle(width=2.8, height=0.8, color=BLUE, fill_opacity=0.7)
        less_water.align_to(container, DOWN)
        less_water.shift(UP * 0.1)
        
        self.play(Transform(water, less_water))
        self.wait(2)
        
        # [0:20] Visual understanding text
        self.play(FadeOut(subtraction_text))
        visual_text = Text("See how the levels rise and fall? That's a visual way to grasp these\nfundamental operations. It's not just about numbers; it's about changes in quantity.")
        visual_text.scale(0.6)
        visual_text.to_edge(UP)
        
        self.play(Write(visual_text))
        
        # Demonstrate rising and falling again
        medium_water = Rectangle(width=2.8, height=1.5, color=BLUE, fill_opacity=0.7)
        medium_water.align_to(container, DOWN)
        medium_water.shift(UP * 0.1)
        
        self.play(Transform(water, medium_water))
        self.play(Transform(water, less_water))
        self.play(Transform(water, medium_water))
        self.wait(1)
        
        # [0:25] Essence text
        self.play(FadeOut(visual_text))
        essence_text = Text("The essence is about combining or separating, growing or shrinking.")
        essence_text.scale(0.7)
        essence_text.to_edge(UP)
        
        self.play(Write(essence_text))
        self.wait(2)
        
        # Final text
        self.play(FadeOut(essence_text))
        final_text = Text("And that understanding lays the groundwork for everything that follows.")
        final_text.scale(0.7)
        final_text.to_edge(UP)
        
        self.play(Write(final_text))
        self.wait(2)
        
        # Clear everything
        self.play(FadeOut(final_text), FadeOut(container), FadeOut(water))
        self.wait(1)
