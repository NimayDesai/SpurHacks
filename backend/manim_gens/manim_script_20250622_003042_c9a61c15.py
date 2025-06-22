from manim import *

class QuantumMechanicsScript(Scene):
    def construct(self):
        # (0:00) We intuitively imagine the world as collections of tiny balls.
        text1 = Text("We intuitively imagine the world as collections of tiny balls.", font_size=36)
        text1.move_to(UP * 2)
        self.play(Write(text1))
        
        # Visual: tiny balls/marbles
        balls = VGroup(*[Circle(radius=0.1, color=BLUE, fill_opacity=0.8) for _ in range(12)])
        balls.arrange_in_grid(3, 4, buff=0.3)
        balls.move_to(DOWN * 0.5)
        self.play(Create(balls))
        
        # A marble, even shrunk down billions of times, still has a clear location, a definite speed.
        text2 = Text("A marble, even shrunk down billions of times, still has a clear location, a definite speed.", font_size=32)
        text2.move_to(DOWN * 2.5)
        self.play(Write(text2))
        
        # That's classical physics.
        text3 = Text("That's classical physics.", font_size=32)
        text3.move_to(DOWN * 3.2)
        self.play(Write(text3))
        
        self.wait(3)
        self.play(FadeOut(text1, text2, text3, balls))
        
        # (0:15) But when we zoom in, truly zoom, to the realm of electrons and photons, this simple picture dissolves.
        text4 = Text("But when we zoom in, truly zoom, to the realm of electrons and photons,", font_size=36)
        text4.move_to(UP * 1)
        text5 = Text("this simple picture dissolves.", font_size=36)
        text5.move_to(UP * 0.3)
        self.play(Write(text4))
        self.play(Write(text5))
        
        self.wait(10)
        self.play(FadeOut(text4, text5))
        
        # (0:25) Instead of a tiny ball at a specific spot, quantum mechanics suggests these fundamental particles exist as a spread-out "cloud" of possibilities.
        text6 = Text("Instead of a tiny ball at a specific spot, quantum mechanics suggests", font_size=32)
        text6.move_to(UP * 1.5)
        text7 = Text("these fundamental particles exist as a spread-out \"cloud\" of possibilities.", font_size=32)
        text7.move_to(UP * 1)
        self.play(Write(text6))
        self.play(Write(text7))
        
        # Visual: probability cloud
        cloud = Circle(radius=1.5, color=YELLOW, fill_opacity=0.3, stroke_opacity=0.5)
        cloud.move_to(DOWN * 0.5)
        self.play(Create(cloud))
        
        self.wait(15)
        self.play(FadeOut(text6, text7, cloud))
        
        # (0:40) It's not that we don't *know* where it is; it's that, in a very real sense, it *isn't* at a single, definite place until we look.
        text8 = Text("It's not that we don't *know* where it is; it's that, in a very real sense,", font_size=32)
        text8.move_to(UP * 1)
        text9 = Text("it *isn't* at a single, definite place until we look.", font_size=32)
        text9.move_to(UP * 0.5)
        self.play(Write(text8))
        self.play(Write(text9))
        
        self.wait(15)
        self.play(FadeOut(text8, text9))
        
        # (0:55) This fuzzy cloud is a probability wave, telling us the *likelihood* of finding the particle here, or there.
        text10 = Text("This fuzzy cloud is a probability wave, telling us the *likelihood*", font_size=32)
        text10.move_to(UP * 1)
        text11 = Text("of finding the particle here, or there.", font_size=32)
        text11.move_to(UP * 0.5)
        self.play(Write(text10))
        self.play(Write(text11))
        
        # Visual: probability wave
        plane = NumberPlane(x_range=[-4, 4], y_range=[-2, 2], background_line_style={"stroke_opacity": 0.3})
        plane.scale(0.7)
        plane.move_to(DOWN * 1)
        
        wave_func = lambda x: 0.8 * np.exp(-0.3 * x**2) * np.cos(2 * x)
        wave = plane.plot(wave_func, x_range=[-4, 4], color=YELLOW, stroke_width=4)
        
        self.play(Create(plane))
        self.play(Create(wave))
        
        self.wait(10)
        self.play(FadeOut(text10, text11, plane, wave))
        
        # (1:05) The act of observation "collapses" this wave, forcing the particle to pick one of those possibilities.
        text12 = Text("The act of observation \"collapses\" this wave, forcing the particle", font_size=32)
        text12.move_to(UP * 1)
        text13 = Text("to pick one of those possibilities.", font_size=32)
        text13.move_to(UP * 0.5)
        self.play(Write(text12))
        self.play(Write(text13))
        
        self.wait(10)
        self.play(FadeOut(text12, text13))
        
        # (1:15) This isn't just about measurement error; it's a profound statement about the nature of reality itself.
        text14 = Text("This isn't just about measurement error; it's a profound statement", font_size=32)
        text14.move_to(UP * 1)
        text15 = Text("about the nature of reality itself.", font_size=32)
        text15.move_to(UP * 0.5)
        self.play(Write(text14))
        self.play(Write(text15))
        
        # Quantum mechanics is the mathematical language describing these probabilities, these inherent uncertainties, at the universe's most fundamental level.
        text16 = Text("Quantum mechanics is the mathematical language describing these probabilities,", font_size=28)
        text16.move_to(DOWN * 0.5)
        text17 = Text("these inherent uncertainties, at the universe's most fundamental level.", font_size=28)
        text17.move_to(DOWN * 1)
        self.play(Write(text16))
        self.play(Write(text17))
        
        self.wait(5)