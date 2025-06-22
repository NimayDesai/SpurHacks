from manim import *

class QuantumMechanicsScript(Scene):
    def construct(self):
        # (0:00) We typically envision particles as tiny, distinct objects with exact locations.
        text1 = Text("We typically envision particles as tiny, distinct objects with exact locations.", 
                    font_size=36).scale(0.8)
        
        # Visual: tiny distinct particles at exact locations
        particles = VGroup()
        for i in range(6):
            particle = Dot(radius=0.08, color=BLUE)
            particle.move_to([i*1.5 - 3.75, 0, 0])
            particles.add(particle)
        
        self.play(Write(text1))
        self.wait(2)
        self.play(FadeIn(particles))
        self.wait(6)
        self.play(FadeOut(text1), FadeOut(particles))
        
        # (0:08) But at the universe's smallest scales, this intuition fails.
        text2 = Text("But at the universe's smallest scales, this intuition fails.", 
                    font_size=36).scale(0.8)
        self.play(Write(text2))
        self.wait(6)
        self.play(FadeOut(text2))
        
        # (0:14) Quantum mechanics reveals a world where energy and momentum come in discrete packets – "quanta."
        text3 = Text("Quantum mechanics reveals a world where energy and momentum\ncome in discrete packets – \"quanta.\"", 
                    font_size=36).scale(0.8)
        
        # Visual: discrete energy packets
        quanta = VGroup()
        for i in range(5):
            quantum = Rectangle(width=0.6, height=0.8, color=YELLOW, fill_opacity=0.7)
            quantum.move_to([i*1.2 - 2.4, -1.5, 0])
            label = Text("E", font_size=24).move_to(quantum.get_center())
            quanta.add(VGroup(quantum, label))
        
        self.play(Write(text3))
        self.wait(3)
        self.play(FadeIn(quanta))
        self.wait(8)
        self.play(FadeOut(text3), FadeOut(quanta))
        
        # (0:25) A particle's position isn't fixed, but a probability distribution.
        text4 = Text("A particle's position isn't fixed, but a probability distribution.", 
                    font_size=36).scale(0.8)
        
        # Visual: probability distribution curve
        axes = Axes(
            x_range=[-3, 3, 1],
            y_range=[0, 2, 0.5],
            x_length=6,
            y_length=3,
            axis_config={"color": WHITE}
        ).scale(0.7).shift(DOWN*1.2)
        
        def prob_func(x):
            return 1.5 * np.exp(-x**2/2)
        
        prob_curve = axes.plot(
            prob_func,
            x_range=[-3, 3],
            color=RED,
            stroke_width=4
        )
        
        self.play(Write(text4))
        self.wait(2)
        self.play(Create(axes), Create(prob_curve))
        self.wait(7)
        self.play(FadeOut(text4), FadeOut(axes), FadeOut(prob_curve))
        
        # (0:34) It's a mathematical framework describing nature's strange, probabilistic dance, offering astonishingly precise predictions despite its counter-intuitive essence.
        text5 = Text("It's a mathematical framework describing nature's strange,\nprobabilistic dance, offering astonishingly precise predictions\ndespite its counter-intuitive essence.", 
                    font_size=36).scale(0.8)
        
        # Visual: mathematical equations and wave-like motion
        equation = MathTex(r"\Psi(x,t) = A e^{i(kx - \omega t)}", font_size=48)
        equation.shift(DOWN*1.5)
        
        wave_func = lambda x: 0.5 * np.sin(2*x)
        wave_axes = Axes(
            x_range=[-PI, PI, PI/2],
            y_range=[-1, 1, 0.5],
            x_length=6,
            y_length=2,
            axis_config={"color": WHITE}
        ).scale(0.8).shift(UP*1.5)
        
        wave = wave_axes.plot(
            wave_func,
            x_range=[-PI, PI],
            color=GREEN,
            stroke_width=3
        )
        
        self.play(Write(text5))
        self.wait(4)
        self.play(Create(wave_axes), Create(wave))
        self.wait(2)
        self.play(Write(equation))
        self.wait(10)
        self.play(FadeOut(text5), FadeOut(equation), FadeOut(wave_axes), FadeOut(wave))
        
        # (0:50) Final wait
        self.wait(2)