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

class KinematicsScene(Scene):
    def construct(self):
        # Initial text about kinematics
        title = Text("Kinematics: it's all about motion, but without worrying *why* things move.", 
                    font_size=36, color=WHITE).scale(0.8)
        title.to_edge(UP)
        
        self.play(Write(title))
        self.wait(5)  # [0:05]
        
        # Clear and show dance analogy
        self.play(FadeOut(title))
        
        dance_text = Text("Think of it like describing a dance: where are the dancers,\nhow fast are they moving, and how is that speed changing?", 
                         font_size=32, color=WHITE).scale(0.9)
        dance_text.move_to(UP * 2)
        
        # Create simple dancers visualization
        dancer1 = Circle(radius=0.3, color=BLUE, fill_opacity=0.7).move_to(LEFT * 3)
        dancer2 = Circle(radius=0.3, color=RED, fill_opacity=0.7).move_to(RIGHT * 2)
        
        # Add movement arrows
        arrow1 = Arrow(start=dancer1.get_center() + DOWN * 0.5, 
                      end=dancer1.get_center() + DOWN * 0.5 + RIGHT * 1.5, 
                      color=BLUE, stroke_width=3)
        arrow2 = Arrow(start=dancer2.get_center() + DOWN * 0.5, 
                      end=dancer2.get_center() + DOWN * 0.5 + LEFT * 1, 
                      color=RED, stroke_width=3)
        
        self.play(Write(dance_text))
        self.play(FadeIn(dancer1), FadeIn(dancer2))
        self.play(Create(arrow1), Create(arrow2))
        
        self.wait(10)  # [0:15]
        
        # Clear and show vectors explanation
        self.play(FadeOut(dance_text), FadeOut(dancer1), FadeOut(dancer2), 
                 FadeOut(arrow1), FadeOut(arrow2))
        
        vectors_text = Text("We use vectors to track position, velocity – the rate of change\nof position – and acceleration – the rate of change of velocity.", 
                           font_size=32, color=WHITE).scale(0.85)
        vectors_text.move_to(UP * 2.5)
        
        # Create coordinate system
        plane = NumberPlane(
            x_range=[-4, 4, 1],
            y_range=[-2, 2, 1],
            background_line_style={"stroke_opacity": 0.3},
            axis_config={"stroke_width": 2}
        ).scale(0.7).move_to(DOWN * 0.5)
        
        # Position vector
        pos_vector = Arrow(start=plane.c2p(0, 0), end=plane.c2p(2, 1), 
                          color=GREEN, stroke_width=4)
        pos_label = Text("Position", font_size=24, color=GREEN).next_to(pos_vector, UR)
        
        # Velocity vector
        vel_vector = Arrow(start=plane.c2p(2, 1), end=plane.c2p(3.5, 1.5), 
                          color=BLUE, stroke_width=4)
        vel_label = Text("Velocity", font_size=24, color=BLUE).next_to(vel_vector, UR)
        
        # Acceleration vector
        acc_vector = Arrow(start=plane.c2p(2, 1), end=plane.c2p(2.5, 0.2), 
                          color=RED, stroke_width=4)
        acc_label = Text("Acceleration", font_size=24, color=RED).next_to(acc_vector, DR)
        
        self.play(Write(vectors_text))
        self.play(Create(plane))
        self.play(Create(pos_vector), Write(pos_label))
        self.play(Create(vel_vector), Write(vel_label))
        self.play(Create(acc_vector), Write(acc_label))
        
        self.wait(10)  # [0:25]
        
        # Clear and show final relationship
        self.play(FadeOut(vectors_text), FadeOut(plane), FadeOut(pos_vector), 
                 FadeOut(pos_label), FadeOut(vel_vector), FadeOut(vel_label),
                 FadeOut(acc_vector), FadeOut(acc_label))
        
        relationship_text = Text("See how these quantities relate? It's a chain reaction,\nelegantly describing the dance of motion itself.", 
                                font_size=34, color=WHITE).scale(0.9)
        relationship_text.move_to(UP * 1.5)
        
        # Create chain reaction visualization
        pos_box = Rectangle(width=2, height=0.8, color=GREEN, fill_opacity=0.3).move_to(LEFT * 3)
        pos_text = Text("Position", font_size=20, color=GREEN).move_to(pos_box.get_center())
        
        vel_box = Rectangle(width=2, height=0.8, color=BLUE, fill_opacity=0.3).move_to(ORIGIN)
        vel_text = Text("Velocity", font_size=20, color=BLUE).move_to(vel_box.get_center())
        
        acc_box = Rectangle(width=2, height=0.8, color=RED, fill_opacity=0.3).move_to(RIGHT * 3)
        acc_text = Text("Acceleration", font_size=20, color=RED).move_to(acc_box.get_center())
        
        # Derivative arrows
        arrow_pos_vel = Arrow(start=pos_box.get_right(), end=vel_box.get_left(), 
                             color=WHITE, stroke_width=3)
        arrow_vel_acc = Arrow(start=vel_box.get_right(), end=acc_box.get_left(), 
                             color=WHITE, stroke_width=3)
        
        deriv_label1 = Text("d/dt", font_size=16, color=WHITE).next_to(arrow_pos_vel, UP, buff=0.1)
        deriv_label2 = Text("d/dt", font_size=16, color=WHITE).next_to(arrow_vel_acc, UP, buff=0.1)
        
        self.play(Write(relationship_text))
        self.play(Create(pos_box), Write(pos_text))
        self.play(Create(arrow_pos_vel), Write(deriv_label1))
        self.play(Create(vel_box), Write(vel_text))
        self.play(Create(arrow_vel_acc), Write(deriv_label2))
        self.play(Create(acc_box), Write(acc_text))
        
        self.wait(10)  # [0:35]
        
        # Final fade out
        self.play(FadeOut(relationship_text), FadeOut(pos_box), FadeOut(pos_text),
                 FadeOut(vel_box), FadeOut(vel_text), FadeOut(acc_box), FadeOut(acc_text),
                 FadeOut(arrow_pos_vel), FadeOut(arrow_vel_acc), 
                 FadeOut(deriv_label1), FadeOut(deriv_label2))
