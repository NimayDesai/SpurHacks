from manim import *

class CalculusIntro(Scene):
    def construct(self):
        # (0:00) Imagine trying to understand how things change, not just on average, but precisely, moment by moment.
        text1 = Text("Imagine trying to understand how things change,\nnot just on average, but precisely, moment by moment.", 
                    font_size=36, color=WHITE)
        text1.move_to(ORIGIN)
        
        self.play(Write(text1))
        self.wait(8)
        
        # (0:08) Calculus provides a powerful lens: one part lets us zoom in infinitely close to find the *instantaneous* rate of change, like your speed right now.
        self.play(FadeOut(text1))
        
        text2 = Text("Calculus provides a powerful lens: one part lets us zoom in\ninfinitely close to find the instantaneous rate of change,\nlike your speed right now.", 
                    font_size=36, color=WHITE)
        text2.move_to(ORIGIN)
        
        self.play(Write(text2))
        self.wait(12)
        
        # (0:20) The other asks the inverse: if we know these tiny rates, what was the *total accumulation* over time?
        self.play(FadeOut(text2))
        
        text3 = Text("The other asks the inverse: if we know these tiny rates,\nwhat was the total accumulation over time?", 
                    font_size=36, color=WHITE)
        text3.move_to(ORIGIN)
        
        self.play(Write(text3))
        self.wait(10)
        
        # (0:30) It's about connecting the small, local changes to the vast, global outcomes.
        self.play(FadeOut(text3))
        
        text4 = Text("It's about connecting the small, local changes\nto the vast, global outcomes.", 
                    font_size=36, color=WHITE)
        text4.move_to(ORIGIN)
        
        self.play(Write(text4))
        self.wait(5)
        
        self.play(FadeOut(text4))