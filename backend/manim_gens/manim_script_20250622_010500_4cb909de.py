from manim import *

class QuantumMechanicsScript(Scene):
    def construct(self):
        # (0:00) We typically envision particles as tiny, distinct objects with exact locations.
        text1 = Text("We typically envision particles as tiny, distinct objects with exact locations.", 
                    font_size=32).scale(0.8)
        
        # Visual: Small circles representing particles at fixed positions
        particles = VGroup()
        positions = [LEFT*3, LEFT*1, RIGHT*1, RIGHT*3]
        for pos in positions:
            particle = Circle(radius=0.1, color=BLUE, fill_opacity=1)
            particle.move_to(pos + UP*0.5)
            particles.add(particle)
        
        self.play(Write(text1))
        self.play(Create(particles))
        self.wait(8)
        self.play(FadeOut(text1), FadeOut(particles))
        
        # (0:08) But at the universe's smallest scales, this intuition fails.
        text2 = Text("But at the universe's smallest scales, this intuition fails.", 
                    font_size=36).scale(0.9)
        self.play(Write(text2))
        self.wait(6)
        self.play(FadeOut(text2))
        
        # (0:14) Quantum mechanics reveals a world where energy and momentum come in discrete packets – "quanta."
        text3 = Text("Quantum mechanics reveals a world where energy and momentum\ncome in discrete packets – \"quanta.\"", 
                    font_size=32).scale(0.8)
        
        # Visual: Discrete energy packets
        packets = VGroup()
        for i in range(5):
            packet = Rectangle(width=0.8, height=0.5, color=YELLOW, fill_opacity=0.7)
            packet.move_to(LEFT*4 + RIGHT*2*i + DOWN*1)
            energy_label = Text("E", font_size=20, color=WHITE)
            energy_label.move_to(packet.get_center())
            packet_group = VGroup(packet, energy_label)
            packets.add(packet_group)
        
        self.play(Write(text3))
        self.play(Create(packets))
        self.wait(11)
        self.play(FadeOut(text3), FadeOut(packets))
        
        # (0:25) A particle's position isn't fixed, but a probability distribution.
        text4 = Text("A particle's position isn't fixed, but a probability distribution.", 
                    font_size=36).scale(0.9)
        
        # Visual: Probability distribution curve
        axes = Axes(
            x_range=[-3, 3, 1],
            y_range=[0, 1, 0.2],
            x_length=6,
            y_length=3,
            axis_config={"color": WHITE}
        ).scale(0.8).shift(DOWN*1)
        
        def prob_func(x):
            return 0.8 * np.exp(-x**2/2)
        
        prob_curve = axes.plot(
            prob_func,
            x_range=[-3, 3],
            color=RED,
            stroke_width=4
        )
        
        self.play(Write(text4))
        self.play(Create(axes), Create(prob_curve))
        self.wait(9)
        self.play(FadeOut(text4), FadeOut(axes), FadeOut(prob_curve))
        
        # (0:34) It's a mathematical framework describing nature's strange, probabilistic dance, offering astonishingly precise predictions despite its counter-intuitive essence.
        text5 = Text("It's a mathematical framework describing nature's strange,\nprobabilistic dance, offering astonishingly precise predictions\ndespite its counter-intuitive essence.", 
                    font_size=30).scale(0.8)
        
        # Visual: Mathematical equations and wave-like motion
        equation = MathTex(r"\Psi(x,t) = Ae^{i(kx-\omega t)}", font_size=40)
        equation.move_to(DOWN*1.5)
        
        # Wave animation
        wave_axes = Axes(
            x_range=[-4, 4, 1],
            y_range=[-1, 1, 0.5],
            x_length=8,
            y_length=2,
            axis_config={"color": WHITE}
        ).scale(0.6).shift(UP*1)
        
        def wave_func(x, t):
            return 0.5 * np.sin(2*x - 3*t)
        
        wave = always_redraw(lambda: wave_axes.plot(
            lambda x: wave_func(x, self.renderer.time),
            x_range=[-4, 4],
            color=BLUE,
            stroke_width=3
        ))
        
        self.play(Write(text5))
        self.play(Create(wave_axes), Write(equation))
        self.add(wave)
        self.wait(16)
        self.play(FadeOut(text5), FadeOut(wave_axes), FadeOut(equation), FadeOut(wave))
        
        self.wait(1)