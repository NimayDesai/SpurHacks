from manim import *

class CalculusScene(Scene):
    def construct(self):
        # What is calculus? At its heart, it's the study of continuous change. [0:08]
        title = Text("What is calculus?", font_size=36)
        subtitle = Text("At its heart, it's the study of continuous change.", font_size=24)
        self.play(Write(title), run_time=1)
        self.play(Write(subtitle), run_time=2)
        self.wait(5)


        # Imagine a car speeding up – how do we precisely describe its velocity at any instant? That's where calculus comes in. It provides tools to dissect this seemingly simple question. [0:15]
        car_text = Text("Imagine a car speeding up – how do we precisely describe its velocity at any instant?", font_size=24)
        calculus_intro = Text("That's where calculus comes in. It provides tools to dissect this seemingly simple question.", font_size=24)
        self.play(FadeOut(title), FadeOut(subtitle))
        self.play(Write(car_text), run_time=3)
        self.play(Write(calculus_intro), run_time=3)
        self.wait(4)

        # We might start by thinking about average speed over an interval, but what about the *instantaneous* speed? Calculus allows us to zoom in infinitely, revealing the slope of the curve representing the car's position over time— its instantaneous velocity. [0:28]
        average_speed = Text("We might start by thinking about average speed over an interval, but what about the *instantaneous* speed?", font_size=24)
        zoom_in = Text("Calculus allows us to zoom in infinitely, revealing the slope of the curve representing the car's position over time— its instantaneous velocity.", font_size=24)
        self.play(FadeOut(car_text), FadeOut(calculus_intro))
        self.play(Write(average_speed), run_time=3)
        self.play(Write(zoom_in), run_time=5)
        self.wait(3)


        # This idea, of zooming in on curves until they appear straight, is fundamental. And this "slope" at a point is just one of the two core ideas: the derivative. [0:40]
        zoom_explanation = Text("This idea, of zooming in on curves until they appear straight, is fundamental.", font_size=24)
        derivative_intro = Text('And this "slope" at a point is just one of the two core ideas: the derivative.', font_size=24)
        self.play(FadeOut(average_speed), FadeOut(zoom_in))
        self.play(Write(zoom_explanation), run_time=3)
        self.play(Write(derivative_intro), run_time=3)
        self.wait(3)

        # The inverse? Finding the area under the curve, giving us the integral. It sounds abstract, but it's deeply intertwined with our world—from predicting planetary motion to designing efficient bridges. [0:52]
        integral_intro = Text("The inverse? Finding the area under the curve, giving us the integral.", font_size=24)
        applications = Text("It sounds abstract, but it's deeply intertwined with our world—from predicting planetary motion to designing efficient bridges.", font_size=24)
        self.play(FadeOut(zoom_explanation), FadeOut(derivative_intro))
        self.play(Write(integral_intro), run_time=3)
        self.play(Write(applications), run_time=5)
        self.wait(3)

        # Calculus doesn't just give us answers; it gives us a way of thinking about continuous change itself.
        conclusion = Text("Calculus doesn't just give us answers; it gives us a way of thinking about continuous change itself.", font_size=24)
        self.play(FadeOut(integral_intro), FadeOut(applications))
        self.play(Write(conclusion), run_time=3)
        self.wait(3)

