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

class InternalExternalForces(Scene):
    def construct(self):
        # Initial text about tug-of-war
        initial_text = Text("Imagine a tug-of-war,", font_size=36)
        self.play(Write(initial_text))
        self.wait(5)
        
        # [0:05] - Clear and show tug-of-war with forces
        self.play(FadeOut(initial_text))
        
        # Create tug-of-war visual
        rope = Line(LEFT * 3, RIGHT * 3, color=YELLOW, stroke_width=8)
        team1 = Rectangle(width=1, height=2, color=BLUE).shift(LEFT * 4)
        team2 = Rectangle(width=1, height=2, color=RED).shift(RIGHT * 4)
        
        # Force arrows
        force1 = Arrow(LEFT * 3.5, LEFT * 2.5, color=BLUE, stroke_width=6)
        force2 = Arrow(RIGHT * 3.5, RIGHT * 2.5, color=RED, stroke_width=6)
        
        forces_text = Text("but instead of ropes, we have forces.", font_size=32).shift(UP * 2)
        
        self.play(
            Create(rope),
            Create(team1),
            Create(team2),
            Write(forces_text)
        )
        self.play(
            Create(force1),
            Create(force2)
        )
        self.wait(5)
        
        # [0:15] - Internal forces explanation
        self.play(FadeOut(forces_text))
        
        # Show internal forces within rope
        internal_forces = VGroup()
        for i in range(5):
            x_pos = -2.5 + i
            internal_arrow1 = Arrow([x_pos, -0.2, 0], [x_pos + 0.4, -0.2, 0], 
                                  color=GREEN, stroke_width=3)
            internal_arrow2 = Arrow([x_pos + 0.6, 0.2, 0], [x_pos + 0.2, 0.2, 0], 
                                  color=GREEN, stroke_width=3)
            internal_forces.add(internal_arrow1, internal_arrow2)
        
        internal_text = Text("Internal forces, like the tension within the rope itself,", 
                           font_size=28).shift(UP * 2.5)
        cancel_text = Text("cancel each other out – they don't affect the overall motion.", 
                         font_size=28).shift(UP * 1.8)
        
        self.play(Write(internal_text))
        self.play(Create(internal_forces))
        self.play(Write(cancel_text))
        self.wait(3)
        
        # Show cancellation
        self.play(FadeOut(internal_forces, scale=0.5))
        self.wait(2)
        
        # [0:25] - External forces explanation
        self.play(FadeOut(internal_text), FadeOut(cancel_text))
        
        external_text1 = Text("External forces, however, like the teams pulling on the rope,", 
                            font_size=28).shift(UP * 2.5)
        external_text2 = Text("determine the net force and thus the rope's acceleration.", 
                            font_size=28).shift(UP * 1.8)
        
        # Highlight external forces
        self.play(Write(external_text1))
        self.play(
            force1.animate.set_color(YELLOW),
            force2.animate.set_color(YELLOW),
            team1.animate.set_color(YELLOW),
            team2.animate.set_color(YELLOW)
        )
        self.play(Write(external_text2))
        
        # Show net force (assuming team1 is stronger)
        net_force = Arrow(ORIGIN, RIGHT * 1.5, color=PURPLE, stroke_width=8)
        net_text = Text("Net Force", font_size=24, color=PURPLE).next_to(net_force, DOWN)
        
        self.play(Create(net_force), Write(net_text))
        self.wait(5)
        
        # [0:35] - Final concept explanation
        self.play(
            FadeOut(external_text1),
            FadeOut(external_text2),
            FadeOut(net_force),
            FadeOut(net_text)
        )
        
        isolation_text1 = Text("So, isolating the system and focusing solely on", 
                             font_size=28).shift(UP * 2.5)
        isolation_text2 = Text("the external interactions is key to understanding its behavior.", 
                             font_size=28).shift(UP * 1.8)
        
        self.play(Write(isolation_text1))
        self.play(Write(isolation_text2))
        
        # Highlight the system boundary
        system_boundary = DashedVMobject(
            Rectangle(width=8, height=3, color=WHITE).shift(DOWN * 0.5),
            num_dashes=20
        )
        self.play(Create(system_boundary))
        self.wait(5)
        
        # Final summary
        self.play(
            FadeOut(isolation_text1),
            FadeOut(isolation_text2),
            FadeOut(system_boundary)
        )
        
        final_text1 = Text("This is the essence of internal and external forces –", 
                         font_size=32).shift(UP * 1)
        final_text2 = Text("a simple yet powerful idea.", 
                         font_size=32).shift(DOWN * 1)
        
        self.play(Write(final_text1))
        self.play(Write(final_text2))
        self.wait(3)
        
        # Clear everything
        self.play(
            FadeOut(rope),
            FadeOut(team1),
            FadeOut(team2),
            FadeOut(force1),
            FadeOut(force2),
            FadeOut(final_text1),
            FadeOut(final_text2)
        )
