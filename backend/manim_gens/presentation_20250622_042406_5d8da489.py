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

class ForceScript(Scene):
    def construct(self):
        # [0:00-0:05] Forces, what are they?
        title = Text("Forces, what are they?", font_size=48)
        self.play(Write(title))
        self.wait(5)
        
        # [0:05] Clear title and show first statement
        self.play(FadeOut(title))
        
        # [0:05-0:10] Intuitively, we think of a push or a pull. But it's more than that.
        push_pull_text = Text("Intuitively, we think of a push or a pull.", font_size=36)
        push_pull_text.move_to(UP * 2)
        
        # Visual: arrows showing push and pull
        push_arrow = Arrow(LEFT * 2, RIGHT * 2, color=RED, stroke_width=8)
        push_arrow.move_to(UP * 0.5)
        push_label = Text("PUSH", font_size=24, color=RED)
        push_label.next_to(push_arrow, UP)
        
        pull_arrow = Arrow(RIGHT * 2, LEFT * 2, color=BLUE, stroke_width=8)
        pull_arrow.move_to(DOWN * 0.5)
        pull_label = Text("PULL", font_size=24, color=BLUE)
        pull_label.next_to(pull_arrow, DOWN)
        
        self.play(Write(push_pull_text))
        self.play(Create(push_arrow), Write(push_label))
        self.play(Create(pull_arrow), Write(pull_label))
        
        more_text = Text("But it's more than that.", font_size=36)
        more_text.move_to(DOWN * 2.5)
        self.play(Write(more_text))
        self.wait(2)
        
        # [0:10] Clear and show next statement
        self.play(FadeOut(push_pull_text), FadeOut(push_arrow), FadeOut(push_label), 
                 FadeOut(pull_arrow), FadeOut(pull_label), FadeOut(more_text))
        
        # [0:10-0:15] A force is an interaction, something that changes an object's motion or its shape.
        interaction_text = Text("A force is an interaction, something that changes", font_size=36)
        interaction_text.move_to(UP * 1)
        motion_text = Text("an object's motion or its shape.", font_size=36)
        motion_text.move_to(UP * 0.3)
        
        # Visual: object changing motion
        box = Square(side_length=0.8, color=GREEN, fill_opacity=0.7)
        box.move_to(LEFT * 3)
        
        # Arrow showing force
        force_arrow = Arrow(LEFT * 1.5, RIGHT * 1.5, color=YELLOW, stroke_width=6)
        force_arrow.move_to(DOWN * 0.5)
        
        # Box after motion
        box_moved = Square(side_length=0.8, color=GREEN, fill_opacity=0.7)
        box_moved.move_to(RIGHT * 3)
        
        self.play(Write(interaction_text))
        self.play(Write(motion_text))
        self.play(Create(box))
        self.play(Create(force_arrow))
        self.play(Transform(box, box_moved))
        self.wait(2)
        
        # [0:15] Clear and show next statement
        self.play(FadeOut(interaction_text), FadeOut(motion_text), 
                 FadeOut(box), FadeOut(force_arrow))
        
        # [0:15-0:20] Imagine a ball – it's not moving until something acts upon it, exerts a force.
        ball_text = Text("Imagine a ball – it's not moving until something", font_size=36)
        ball_text.move_to(UP * 1.5)
        acts_text = Text("acts upon it, exerts a force.", font_size=36)
        acts_text.move_to(UP * 0.8)
        
        # Visual: stationary ball
        ball = Circle(radius=0.4, color=ORANGE, fill_opacity=0.8)
        ball.move_to(LEFT * 2)
        
        self.play(Write(ball_text))
        self.play(Write(acts_text))
        self.play(Create(ball))
        
        # Show force acting on ball
        ball_force = Arrow(LEFT * 0.5, RIGHT * 0.5, color=RED, stroke_width=6)
        ball_force.next_to(ball, RIGHT, buff=0.1)
        
        ball_moved = Circle(radius=0.4, color=ORANGE, fill_opacity=0.8)
        ball_moved.move_to(RIGHT * 2)
        
        self.play(Create(ball_force))
        self.play(Transform(ball, ball_moved))
        self.wait(2)
        
        # [0:20] Clear and show next statement
        self.play(FadeOut(ball_text), FadeOut(acts_text), 
                 FadeOut(ball), FadeOut(ball_force))
        
        # [0:20-0:25] Gravity pulls it down, friction slows it.
        gravity_text = Text("Gravity pulls it down, friction slows it.", font_size=36)
        gravity_text.move_to(UP * 2)
        
        # Visual: ball with gravity and friction forces
        demo_ball = Circle(radius=0.4, color=ORANGE, fill_opacity=0.8)
        demo_ball.move_to(ORIGIN)
        
        gravity_arrow = Arrow(ORIGIN, DOWN * 1.5, color=PURPLE, stroke_width=6)
        gravity_arrow.next_to(demo_ball, DOWN, buff=0)
        gravity_label = Text("Gravity", font_size=24, color=PURPLE)
        gravity_label.next_to(gravity_arrow, DOWN)
        
        friction_arrow = Arrow(ORIGIN, LEFT * 1.5, color=LIGHT_GRAY, stroke_width=6)
        friction_arrow.next_to(demo_ball, LEFT, buff=0)
        friction_label = Text("Friction", font_size=24, color=LIGHT_GRAY)
        friction_label.next_to(friction_arrow, LEFT)
        
        self.play(Write(gravity_text))
        self.play(Create(demo_ball))
        self.play(Create(gravity_arrow), Write(gravity_label))
        self.play(Create(friction_arrow), Write(friction_label))
        self.wait(2)
        
        # [0:25] Clear and show next statement
        self.play(FadeOut(gravity_text), FadeOut(demo_ball), FadeOut(gravity_arrow), 
                 FadeOut(gravity_label), FadeOut(friction_arrow), FadeOut(friction_label))
        
        # [0:25-0:30] Forces aren't things themselves; they're interactions between things.
        not_things_text = Text("Forces aren't things themselves;", font_size=36)
        not_things_text.move_to(UP * 1)
        interactions_text = Text("they're interactions between things.", font_size=36)
        interactions_text.move_to(UP * 0.3)
        
        # Visual: two objects with interaction between them
        obj1 = Circle(radius=0.5, color=BLUE, fill_opacity=0.7)
        obj1.move_to(LEFT * 2)
        
        obj2 = Circle(radius=0.5, color=RED, fill_opacity=0.7)
        obj2.move_to(RIGHT * 2)
        
        interaction_line = Line(LEFT * 1.5, RIGHT * 1.5, color=YELLOW, stroke_width=4)
        interaction_line.move_to(DOWN * 1)
        
        self.play(Write(not_things_text))
        self.play(Write(interactions_text))
        self.play(Create(obj1), Create(obj2))
        self.play(Create(interaction_line))
        self.wait(2)
        
        # [0:30] Clear and show final statement
        self.play(FadeOut(not_things_text), FadeOut(interactions_text), 
                 FadeOut(obj1), FadeOut(obj2), FadeOut(interaction_line))
        
        # [0:30] Understanding these interactions is key to understanding the world around us.
        final_text = Text("Understanding these interactions is key to", font_size=36)
        final_text.move_to(UP * 0.5)
        world_text = Text("understanding the world around us.", font_size=36)
        world_text.move_to(DOWN * 0.5)
        
        self.play(Write(final_text))
        self.play(Write(world_text))
        self.wait(3)
        
        # Final fadeout
        self.play(FadeOut(final_text), FadeOut(world_text))
