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

class IdealGasLawExplanation(Scene):
    def construct(self):
        # Initial text about gas as particles
        intro_text = Text("Imagine a gas as a swarm of tiny, bouncy particles.", font_size=40)
        intro_text.move_to(ORIGIN)
        
        # Create container box
        container = Rectangle(width=6, height=4, color=WHITE, stroke_width=3)
        container.move_to(ORIGIN)
        
        # Create particles as small circles
        particles = VGroup()
        for i in range(15):
            particle = Circle(radius=0.08, color=BLUE, fill_opacity=0.8)
            particle.move_to([
                np.random.uniform(-2.8, 2.8),
                np.random.uniform(-1.8, 1.8),
                0
            ])
            particles.add(particle)
        
        # Show intro text first
        self.play(Write(intro_text))
        self.wait(1)
        
        # Transition to particles visualization at [0:05]
        self.play(FadeOut(intro_text))
        self.play(Create(container))
        self.play(FadeIn(particles))
        
        # Text about collisions creating pressure at [0:05]
        pressure_text = Text("Their collisions create pressure.", font_size=36)
        pressure_text.to_edge(UP, buff=0.5)
        self.play(Write(pressure_text))
        self.wait(2)
        
        # Clear and show more particles text at [0:10]
        self.play(FadeOut(pressure_text))
        more_particles_text = Text("More particles? More collisions, more pressure.", font_size=36)
        more_particles_text.to_edge(UP, buff=0.5)
        self.play(Write(more_particles_text))
        
        # Add more particles to demonstrate
        new_particles = VGroup()
        for i in range(10):
            particle = Circle(radius=0.08, color=BLUE, fill_opacity=0.8)
            particle.move_to([
                np.random.uniform(-2.8, 2.8),
                np.random.uniform(-1.8, 1.8),
                0
            ])
            new_particles.add(particle)
        
        self.play(FadeIn(new_particles))
        particles.add(new_particles)
        self.wait(2)
        
        # Temperature section at [0:15]
        self.play(FadeOut(more_particles_text))
        temp_text = Text("Higher temperature? Faster particles, harder collisions, again, higher pressure.", font_size=32)
        temp_text.to_edge(UP, buff=0.5)
        self.play(Write(temp_text))
        
        # Change particle colors to show temperature increase
        self.play(*[particle.animate.set_color(RED) for particle in particles])
        self.wait(2)
        
        # Volume section at [0:20]
        self.play(FadeOut(temp_text))
        volume_text = Text("And what about volume? More space means fewer collisions per second, lower pressure.", font_size=30)
        volume_text.to_edge(UP, buff=0.5)
        self.play(Write(volume_text))
        
        # Expand container to show volume increase
        larger_container = Rectangle(width=8, height=5, color=WHITE, stroke_width=3)
        larger_container.move_to(ORIGIN)
        self.play(Transform(container, larger_container))
        
        # Spread particles out
        for particle in particles:
            new_pos = [
                np.random.uniform(-3.8, 3.8),
                np.random.uniform(-2.3, 2.3),
                0
            ]
            self.play(particle.animate.move_to(new_pos), run_time=0.3)
        
        self.wait(2)
        
        # Final explanation at [0:30]
        self.play(FadeOut(volume_text), FadeOut(container), FadeOut(particles))
        
        final_text1 = Text("This simple picture beautifully captures the essence of the ideal gas law:", font_size=32)
        final_text1.move_to(UP * 1.5)
        
        formula_text = Text("pressure times volume equals a constant times temperature times the number of particles", font_size=28)
        formula_text.move_to(ORIGIN)
        
        final_text2 = Text("It's a surprisingly powerful connection between seemingly disparate properties.", font_size=32)
        final_text2.move_to(DOWN * 1.5)
        
        self.play(Write(final_text1))
        self.wait(1)
        self.play(Write(formula_text))
        self.wait(1)
        self.play(Write(final_text2))
        self.wait(3)
        
        # Clear everything at the end
        self.play(FadeOut(final_text1), FadeOut(formula_text), FadeOut(final_text2))
