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

class EnergyConservationScene(Scene):
    def construct(self):
        # Initial scene with ball rolling down hill
        title = Text("Imagine a ball rolling down a hill.", font_size=36)
        self.play(Write(title))
        
        # Create hill and ball visual
        hill_points = [[-5, -2, 0], [-2, 2, 0], [2, 1, 0], [5, -2, 0]]
        hill = VMobject()
        hill.set_points_as_corners(hill_points)
        hill.set_stroke(WHITE, 3)
        
        ball = Circle(radius=0.2, fill_opacity=1, color=RED)
        ball.move_to([-2, 2, 0])
        
        self.play(Create(hill), FadeIn(ball))
        self.wait(1)
        
        # Ball rolling animation
        self.play(ball.animate.move_to([2, 1, 0]), run_time=2)
        self.wait(2)
        
        # [0:05] What's driving its motion? Energy!
        self.play(FadeOut(title))
        question = Text("What's driving its motion? Energy!", font_size=36)
        self.play(Write(question))
        self.wait(2)
        
        # [0:10] It starts with potential energy, stored by its height
        self.play(FadeOut(question), FadeOut(hill), FadeOut(ball))
        potential_text = Text("It starts with potential energy, stored by its height.", font_size=32)
        self.play(Write(potential_text))
        
        # Show potential energy visualization
        height_line = Line([0, -2, 0], [0, 2, 0], color=BLUE, stroke_width=4)
        pe_label = Text("PE", font_size=24, color=BLUE).next_to(height_line, RIGHT)
        ball_high = Circle(radius=0.2, fill_opacity=1, color=RED).move_to([0, 2, 0])
        
        self.play(Create(height_line), Write(pe_label), FadeIn(ball_high))
        self.wait(3)
        
        # [0:15] As it rolls, this transforms into kinetic energy, the energy of motion
        self.play(FadeOut(potential_text))
        kinetic_text = Text("As it rolls, this transforms into kinetic energy,\nthe energy of motion.", font_size=32)
        self.play(Write(kinetic_text))
        
        # Show transformation from PE to KE
        ball_low = Circle(radius=0.2, fill_opacity=1, color=RED).move_to([0, -1.5, 0])
        ke_arrow = Arrow([1, -1.5, 0], [2.5, -1.5, 0], color=GREEN, stroke_width=4)
        ke_label = Text("KE", font_size=24, color=GREEN).next_to(ke_arrow, UP)
        
        self.play(
            ball_high.animate.move_to([0, -1.5, 0]),
            Create(ke_arrow),
            Write(ke_label),
            run_time=2
        )
        self.wait(3)
        
        # [0:20] But it's not just balls; everything has energy, even seemingly still objects
        self.play(FadeOut(kinetic_text), FadeOut(height_line), FadeOut(pe_label), 
                 FadeOut(ball_high), FadeOut(ke_arrow), FadeOut(ke_label))
        everything_text = Text("But it's not just balls; everything has energy,\neven seemingly still objects.", font_size=32)
        self.play(Write(everything_text))
        
        # Show various objects with energy
        objects = VGroup(
            Square(side_length=0.8, color=YELLOW),
            Triangle(color=PURPLE).scale(0.5),
            Rectangle(width=1, height=0.6, color=ORANGE)
        )
        objects.arrange(RIGHT, buff=1).shift(DOWN)
        
        self.play(FadeIn(objects))
        self.wait(3)
        
        # [0:25] This energy can change forms, like potential to kinetic, or heat to light, but the total amount always remains constant
        self.play(FadeOut(everything_text), FadeOut(objects))
        transform_text = Text("This energy can change forms, like potential to kinetic,\nor heat to light, but the total amount always remains constant.", font_size=28)
        self.play(Write(transform_text))
        
        # Show energy transformation arrows
        pe_box = Rectangle(width=1.5, height=0.8, color=BLUE).shift(LEFT*3)
        pe_text = Text("PE", font_size=20, color=BLUE).move_to(pe_box)
        
        ke_box = Rectangle(width=1.5, height=0.8, color=GREEN).shift(RIGHT*3)
        ke_text = Text("KE", font_size=20, color=GREEN).move_to(ke_box)
        
        arrow1 = Arrow(pe_box.get_right(), ke_box.get_left(), color=WHITE)
        arrow2 = Arrow(ke_box.get_left(), pe_box.get_right(), color=WHITE)
        
        heat_box = Rectangle(width=1.5, height=0.8, color=RED).shift(UP*1.5)
        heat_text = Text("Heat", font_size=16, color=RED).move_to(heat_box)
        
        light_box = Rectangle(width=1.5, height=0.8, color=YELLOW).shift(DOWN*1.5)
        light_text = Text("Light", font_size=16, color=YELLOW).move_to(light_box)
        
        arrow3 = Arrow(heat_box.get_bottom(), light_box.get_top(), color=WHITE)
        
        energy_group = VGroup(pe_box, pe_text, ke_box, ke_text, arrow1, arrow2, 
                             heat_box, heat_text, light_box, light_text, arrow3)
        energy_group.scale(0.7).shift(DOWN*0.5)
        
        self.play(FadeIn(energy_group))
        self.wait(5)
        
        # [0:30] That's the core idea: energy is conserved. It flows, it transforms, but it never disappears
        self.play(FadeOut(transform_text), FadeOut(energy_group))
        conservation_text = Text("That's the core idea: energy is conserved.\nIt flows, it transforms, but it never disappears.", font_size=32)
        self.play(Write(conservation_text))
        
        # Final visual showing conservation
        energy_circle = Circle(radius=2, color=WHITE, stroke_width=4)
        flow_arrows = VGroup()
        for i in range(8):
            angle = i * PI / 4
            start = energy_circle.point_at_angle(angle)
            end = energy_circle.point_at_angle(angle + PI/4)
            arrow = CurvedArrow(start, end, color=LIGHT_GRAY, stroke_width=2)
            flow_arrows.add(arrow)
        
        center_text = Text("Energy", font_size=24, color=WHITE).move_to(energy_circle.get_center())
        
        conservation_visual = VGroup(energy_circle, flow_arrows, center_text)
        conservation_visual.scale(0.6).shift(DOWN*1.5)
        
        self.play(FadeIn(conservation_visual))
        self.wait(5)
        
        # Final fadeout
        self.play(FadeOut(conservation_text), FadeOut(conservation_visual))
