from manim import *
import numpy as np

class QuantumMechanicsExplanation(Scene):
    def construct(self):
        # (0:00) We intuitively imagine the world as collections of tiny balls.
        text1 = Text("We intuitively imagine the world as collections of tiny balls.", 
                    font_size=36).move_to(UP * 2)
        
        # Visual: Several small circles representing "tiny balls"
        balls = VGroup()
        for i in range(8):
            ball = Circle(radius=0.15, color=BLUE, fill_opacity=0.8)
            ball.move_to([np.random.uniform(-3, 3), np.random.uniform(-1, 1), 0])
            balls.add(ball)
        
        self.play(Write(text1))
        self.play(Create(balls))
        self.wait(2)
        
        # A marble, even shrunk down billions of times, still has a clear location, a definite speed.
        text2 = Text("A marble, even shrunk down billions of times, still has a clear location, a definite speed.", 
                    font_size=32).move_to(DOWN * 1.5)
        
        # Visual: Single marble with position and velocity vectors
        marble = Circle(radius=0.2, color=RED, fill_opacity=0.9).move_to(LEFT * 2)
        position_arrow = Arrow(ORIGIN, marble.get_center(), color=GREEN)
        velocity_arrow = Arrow(marble.get_center(), marble.get_center() + RIGHT * 1.5, color=YELLOW)
        
        self.play(Write(text2))
        self.play(Create(marble), Create(position_arrow), Create(velocity_arrow))
        self.wait(3)
        
        # That's classical physics.
        text3 = Text("That's classical physics.", font_size=36).move_to(DOWN * 2.5)
        self.play(Write(text3))
        self.wait(3)
        
        # Clear screen for next section
        self.play(FadeOut(text1), FadeOut(text2), FadeOut(text3), 
                 FadeOut(balls), FadeOut(marble), FadeOut(position_arrow), FadeOut(velocity_arrow))
        
        # (0:15) But when we zoom in, truly zoom, to the realm of electrons and photons, this simple picture dissolves.
        text4 = Text("But when we zoom in, truly zoom, to the realm of electrons and photons,", 
                    font_size=32).move_to(UP * 1)
        text5 = Text("this simple picture dissolves.", font_size=32).move_to(UP * 0.5)
        
        # Visual: Zooming effect and dissolving particles
        zoom_circle = Circle(radius=3, color=WHITE)
        dissolving_particles = VGroup()
        for i in range(6):
            particle = Dot(radius=0.1, color=BLUE)
            particle.move_to([np.random.uniform(-2, 2), np.random.uniform(-1, 1), 0])
            dissolving_particles.add(particle)
        
        self.play(Write(text4))
        self.play(Write(text5))
        self.play(Create(zoom_circle), Create(dissolving_particles))
        self.play(zoom_circle.animate.scale(0.3), dissolving_particles.animate.set_opacity(0.3))
        self.wait(5)
        
        # Clear screen
        self.play(FadeOut(text4), FadeOut(text5), FadeOut(zoom_circle), FadeOut(dissolving_particles))
        
        # (0:25) Instead of a tiny ball at a specific spot, quantum mechanics suggests these fundamental particles exist as a spread-out "cloud" of possibilities.
        text6 = Text("Instead of a tiny ball at a specific spot, quantum mechanics suggests", 
                    font_size=30).move_to(UP * 1.5)
        text7 = Text("these fundamental particles exist as a spread-out \"cloud\" of possibilities.", 
                    font_size=30).move_to(UP * 1)
        
        # Visual: Transition from ball to probability cloud
        classical_ball = Circle(radius=0.15, color=BLUE, fill_opacity=0.9).move_to(LEFT * 2)
        
        # Create probability cloud using many small dots with varying opacity
        cloud = VGroup()
        for i in range(200):
            x = np.random.normal(0, 1)
            y = np.random.normal(0, 0.5)
            opacity = np.exp(-(x**2 + y**2)/2) * 0.8
            dot = Dot(radius=0.02, color=YELLOW, fill_opacity=opacity)
            dot.move_to([x + 2, y, 0])
            cloud.add(dot)
        
        self.play(Write(text6))
        self.play(Write(text7))
        self.play(Create(classical_ball))
        self.play(Transform(classical_ball, cloud))
        self.wait(8)
        
        # Clear screen
        self.play(FadeOut(text6), FadeOut(text7), FadeOut(classical_ball))
        
        # (0:40) It's not that we don't *know* where it is; it's that, in a very real sense, it *isn't* at a single, definite place until we look.
        text8 = Text("It's not that we don't *know* where it is; it's that, in a very real sense,", 
                    font_size=30).move_to(UP * 1)
        text9 = Text("it *isn't* at a single, definite place until we look.", 
                    font_size=30).move_to(UP * 0.5)
        
        # Visual: Spread out cloud that hasn't collapsed yet
        quantum_cloud = VGroup()
        for i in range(150):
            x = np.random.normal(0, 1.5)
            y = np.random.normal(0, 0.8)
            opacity = np.exp(-(x**2 + y**2)/4) * 0.6
            dot = Dot(radius=0.03, color=PURPLE, fill_opacity=opacity)
            dot.move_to([x, y - 1, 0])
            quantum_cloud.add(dot)
        
        self.play(Write(text8))
        self.play(Write(text9))
        self.play(Create(quantum_cloud))
        self.wait(8)
        
        # Clear screen
        self.play(FadeOut(text8), FadeOut(text9), FadeOut(quantum_cloud))
        
        # (0:55) This fuzzy cloud is a probability wave, telling us the *likelihood* of finding the particle here, or there.
        text10 = Text("This fuzzy cloud is a probability wave, telling us the *likelihood*", 
                     font_size=30).move_to(UP * 1)
        text11 = Text("of finding the particle here, or there.", 
                     font_size=30).move_to(UP * 0.5)
        
        # Visual: Wave function representation
        axes = Axes(
            x_range=[-4, 4, 1],
            y_range=[0, 1, 0.2],
            x_length=8,
            y_length=3,
            tips=False
        ).move_to(DOWN * 1)
        
        def wave_func(x):
            return 0.8 * np.exp(-x**2/4)
        
        wave = axes.plot(
            wave_func,
            x_range=[-4, 4],
            color=ORANGE,
            stroke_width=4
        )
        
        self.play(Write(text10))
        self.play(Write(text11))
        self.play(Create(axes), Create(wave))
        self.wait(5)
        
        # Clear screen
        self.play(FadeOut(text10), FadeOut(text11), FadeOut(axes), FadeOut(wave))
        
        # (1:05) The act of observation "collapses" this wave, forcing the particle to pick one of those possibilities.
        text12 = Text("The act of observation \"collapses\" this wave,", 
                     font_size=32).move_to(UP * 1)
        text13 = Text("forcing the particle to pick one of those possibilities.", 
                     font_size=32).move_to(UP * 0.5)
        
        # Visual: Wave collapse animation
        spread_wave = VGroup()
        for i in range(100):
            x = np.random.normal(0, 2)
            y = np.random.uniform(-0.5, 0.5)
            dot = Dot(radius=0.02, color=BLUE, fill_opacity=0.5)
            dot.move_to([x, y - 1, 0])
            spread_wave.add(dot)
        
        collapsed_particle = Circle(radius=0.1, color=RED, fill_opacity=1).move_to([1, -1, 0])
        
        self.play(Write(text12))
        self.play(Write(text13))
        self.play(Create(spread_wave))
        self.wait(2)
        self.play(Transform(spread_wave, collapsed_particle))
        self.wait(5)
        
        # Clear screen
        self.play(FadeOut(text12), FadeOut(text13), FadeOut(spread_wave))
        
        # (1:15) This isn't just about measurement error; it's a profound statement about the nature of reality itself.
        text14 = Text("This isn't just about measurement error;", 
                     font_size=32).move_to(UP * 1)
        text15 = Text("it's a profound statement about the nature of reality itself.", 
                     font_size=32).move_to(UP * 0.5)
        
        self.play(Write(text14))
        self.play(Write(text15))
        self.wait(5)
        
        # Quantum mechanics is the mathematical language describing these probabilities, these inherent uncertainties, at the universe's most fundamental level.
        text16 = Text("Quantum mechanics is the mathematical language describing these probabilities,", 
                     font_size=28).move_to(DOWN * 0.5)
        text17 = Text("these inherent uncertainties, at the universe's most fundamental level.", 
                     font_size=28).move_to(DOWN * 1)
        
        # Visual: Mathematical equations and uncertainty representations
        equation1 = MathTex(r"\Psi(x,t)", font_size=48).move_to(LEFT * 3 + DOWN * 2.5)
        equation2 = MathTex(r"|\Psi|^2", font_size=48).move_to(DOWN * 2.5)
        equation3 = MathTex(r"\Delta x \Delta p \geq \frac{\hbar}{2}", font_size=40).move_to(RIGHT * 3 + DOWN * 2.5)
        
        self.play(Write(text16))
        self.play(Write(text17))
        self.play(Write(equation1), Write(equation2), Write(equation3))
        self.wait(8)
        
        # Final fade out
        self.play(FadeOut(text14), FadeOut(text15), FadeOut(text16), FadeOut(text17),
                 FadeOut(equation1), FadeOut(equation2), FadeOut(equation3))
        self.wait(2)