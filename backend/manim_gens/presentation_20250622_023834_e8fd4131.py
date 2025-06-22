from manim import *

class CalculusIntroduction(Scene):
    def construct(self):
        # (0:00) At its heart, calculus is the mathematics of change.
        title_text = Text("At its heart, calculus is the mathematics of change.", font_size=36)
        self.play(Write(title_text))
        self.wait(3)
        
        # Consider a journey: how fast are you moving at this very instant?
        self.play(FadeOut(title_text))
        journey_text = Text("Consider a journey: how fast are you moving at this very instant?", font_size=32)
        self.play(Write(journey_text))
        self.wait(2)
        
        # That's the essence of the derivative, revealing an instantaneous rate.
        self.play(FadeOut(journey_text))
        derivative_text = Text("That's the essence of the derivative, revealing an instantaneous rate.", font_size=32)
        self.play(Write(derivative_text))
        self.wait(3)
        
        # (0:18) But what if you knew your speed at every tiny moment?
        self.play(FadeOut(derivative_text))
        speed_question = Text("But what if you knew your speed at every tiny moment?", font_size=32)
        self.play(Write(speed_question))
        self.wait(3)
        
        # Could you then determine the total distance covered?
        distance_question = Text("Could you then determine the total distance covered?", font_size=32)
        self.play(Write(distance_question))
        distance_question.next_to(speed_question, DOWN, buff=0.5)
        self.wait(9)
        
        # (0:30) This act of summing infinitely many tiny changes to find a total accumulation is integration.
        self.play(FadeOut(speed_question), FadeOut(distance_question))
        integration_text = Text("This act of summing infinitely many tiny changes\nto find a total accumulation is integration.", font_size=32)
        self.play(Write(integration_text))
        self.wait(12)
        
        # (0:42) These two ideas—unveiling the rate of change and reconstructing the total from those rates—are the twin pillars of calculus
        self.play(FadeOut(integration_text))
        pillars_text = Text("These two ideas—unveiling the rate of change and reconstructing\nthe total from those rates—are the twin pillars of calculus,", font_size=30)
        self.play(Write(pillars_text))
        self.wait(3)
        
        # powerful tools for describing our dynamic world.
        tools_text = Text("powerful tools for describing our dynamic world.", font_size=30)
        tools_text.next_to(pillars_text, DOWN, buff=0.5)
        self.play(Write(tools_text))
        self.wait(3)
        
        self.play(FadeOut(pillars_text), FadeOut(tools_text))