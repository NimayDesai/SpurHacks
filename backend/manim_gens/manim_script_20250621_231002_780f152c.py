from manim import *

class CalculusScene(Scene):
    def construct(self):
        # What is calculus? At its heart, it's about understanding change. [0:05]
        text1 = Text("What is calculus? At its heart, it's about understanding change.")
        self.play(Write(text1))
        self.wait(5)
        self.play(FadeOut(text1))

        # Imagine zooming in on a curve. What happens as you magnify more and more? It starts to look straighter and straighter, doesn't it? That's the idea behind the derivative – finding the instantaneous rate of change, the slope of that infinitely zoomed-in line. [0:15]
        text2 = Text("Imagine zooming in on a curve. What happens as you magnify more and more? It starts to look straighter and straighter, doesn't it? That's the idea behind the derivative – finding the instantaneous rate of change, the slope of that infinitely zoomed-in line.")
        curve = FunctionGraph(lambda x: x**2, x_range=[-2,2], color=BLUE)
        self.play(Create(curve),Write(text2))
        self.wait(10)
        self.play(FadeOut(curve), FadeOut(text2))


        # It's about answering questions like: how fast is something changing *right now*? The integral, on the other hand, is about accumulation. It's about adding up infinitely many tiny slices to find the area under a curve, or the total change over time. [0:25]
        text3 = Text("It's about answering questions like: how fast is something changing *right now*? The integral, on the other hand, is about accumulation. It's about adding up infinitely many tiny slices to find the area under a curve, or the total change over time.")
        self.play(Write(text3))
        self.wait(10)
        self.play(FadeOut(text3))

        # So, derivatives dissect change, integrals assemble it. [0:30]
        text4 = Text("So, derivatives dissect change, integrals assemble it.")
        self.play(Write(text4))
        self.wait(5)
        self.play(FadeOut(text4))

        # They're inverse operations, like multiplication and division, but operating on the continuous world of curves and motion. [0:35]
        text5 = Text("They're inverse operations, like multiplication and division, but operating on the continuous world of curves and motion.")
        self.play(Write(text5))
        self.wait(5)
        self.play(FadeOut(text5))

        # Together, they form the language of change, letting us model and understand the dynamic processes that shape our universe.
        text6 = Text("Together, they form the language of change, letting us model and understand the dynamic processes that shape our universe.")
        self.play(Write(text6))
        self.wait(5)
        self.play(FadeOut(text6))
