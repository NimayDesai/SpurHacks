from manim import *

class TorqueVisualization(Scene):
    def construct(self):
        # [0:00-0:05] Imagine a spinning wheel
        wheel = Circle(radius=2, color=WHITE, stroke_width=6)
        wheel_center = Dot(color=WHITE)
        
        text1 = Text("Imagine a spinning wheel.", font_size=36)
        text1.to_edge(UP)
        
        self.play(Write(text1))
        self.play(Create(wheel), Create(wheel_center))
        self.play(Rotate(wheel, PI/2, rate_func=smooth))
        self.wait(1)
        
        # [0:05] Clear and new content
        self.play(FadeOut(text1))
        
        text2 = Text("Its speed, we intuitively understand, depends on how much force is applied.", 
                    font_size=32)
        text2.to_edge(UP)
        
        # Add force arrow
        force_arrow = Arrow(start=wheel.get_right() + RIGHT, 
                           end=wheel.get_right(), 
                           color=RED, 
                           stroke_width=6)
        force_label = Text("Force", font_size=24, color=RED)
        force_label.next_to(force_arrow, RIGHT)
        
        self.play(Write(text2))
        self.play(Create(force_arrow), Write(force_label))
        self.wait(5)
        
        # [0:15] Clear and new content  
        self.play(FadeOut(text2))
        
        text3 = Text("But what about its *angular* speed – how quickly it rotates?", 
                    font_size=32)
        text3.to_edge(UP)
        
        # Show angular velocity indicator
        angular_arrow = Arc(radius=1.5, start_angle=0, angle=PI/2, color=BLUE, stroke_width=4)
        angular_arrow.add_tip(tip_length=0.2)
        omega_label = Tex(r"\omega", font_size=36, color=BLUE)
        omega_label.move_to(UP * 0.5 + LEFT * 0.5)
        
        self.play(Write(text3))
        self.play(Create(angular_arrow), Write(omega_label))
        self.wait(5)
        
        # [0:25] Clear and new content
        self.play(FadeOut(text3))
        
        text4 = Text("That's determined not just by force, but by where that force is applied – its *lever arm*.", 
                    font_size=30)
        text4.to_edge(UP)
        
        # Show lever arm
        lever_arm = Line(start=wheel_center.get_center(), 
                        end=wheel.get_right(), 
                        color=GREEN, 
                        stroke_width=4)
        lever_label = Text("lever arm", font_size=24, color=GREEN)
        lever_label.next_to(lever_arm, DOWN)
        
        self.play(Write(text4))
        self.play(Create(lever_arm), Write(lever_label))
        self.wait(5)
        
        # [0:35] Clear and new content
        self.play(FadeOut(text4))
        
        text5 = Text("A small force far from the center can spin it just as fast\nas a large force close to the center.", 
                    font_size=30)
        text5.to_edge(UP)
        
        # Show comparison: small force far vs large force close
        small_force = Arrow(start=wheel.get_right() + RIGHT*0.5, 
                           end=wheel.get_right(), 
                           color=YELLOW, 
                           stroke_width=4)
        small_label = Text("small force\nfar from center", font_size=20, color=YELLOW)
        small_label.next_to(small_force, UP)
        
        # Clear previous elements first
        self.play(FadeOut(force_arrow), FadeOut(force_label), 
                 FadeOut(angular_arrow), FadeOut(omega_label))
        
        self.play(Write(text5))
        self.play(Create(small_force), Write(small_label))
        self.wait(3)
        
        # Show large force close to center
        large_force = Arrow(start=wheel.get_center() + UP*0.8 + UP*0.5, 
                           end=wheel.get_center() + UP*0.8, 
                           color=ORANGE, 
                           stroke_width=8)
        large_label = Text("large force\nclose to center", font_size=20, color=ORANGE)
        large_label.next_to(large_force, UP)
        
        short_lever = Line(start=wheel_center.get_center(), 
                          end=wheel.get_center() + UP*0.8, 
                          color=GREEN, 
                          stroke_width=4)
        
        self.play(Create(large_force), Write(large_label), Transform(lever_arm, short_lever))
        self.wait(2)
        
        # Final message
        self.play(FadeOut(text5))
        
        text6 = Text("This is torque: a rotational force that depends on both\nmagnitude and distance – a simple, yet profound, idea.", 
                    font_size=30)
        text6.to_edge(UP)
        
        # Show torque equation
        torque_eq = Tex(r"\tau = F \times r", font_size=48)
        torque_eq.move_to(DOWN * 2)
        
        self.play(Write(text6))
        self.play(Write(torque_eq))
        self.wait(5)
        
        # Final clear
        self.play(FadeOut(VGroup(*self.mobjects)))