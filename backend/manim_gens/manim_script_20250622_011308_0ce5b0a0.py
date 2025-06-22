from manim import *

class CalculusIntroduction(Scene):
    def construct(self):
        # [0:00] What *is* calculus, fundamentally?
        title_text = Text("What *is* calculus, fundamentally?", font_size=48)
        self.play(Write(title_text))
        self.wait(2)
        
        # It's the language for things that change, that aren't constant.
        change_text = Text("It's the language for things that change, that aren't constant.", font_size=36)
        change_text.next_to(title_text, DOWN, buff=1)
        self.play(Write(change_text))
        self.wait(2)
        
        # For centuries, our math excelled at straight lines and steady rates.
        straight_text = Text("For centuries, our math excelled at straight lines and steady rates.", font_size=36)
        straight_text.next_to(change_text, DOWN, buff=0.5)
        self.play(Write(straight_text))
        
        # Show straight line
        line = Line(LEFT * 3, RIGHT * 3, color=BLUE, stroke_width=4)
        line.next_to(straight_text, DOWN, buff=1)
        self.play(Create(line))
        self.wait(3)
        
        # [0:15] Clear and transition
        self.play(FadeOut(title_text, change_text, straight_text, line))
        
        # But how do you measure speed at a single instant when the pace is always shifting?
        speed_text = Text("But how do you measure speed at a single instant\nwhen the pace is always shifting?", font_size=40)
        self.play(Write(speed_text))
        self.wait(3)
        
        # Calculus lets us ask: what does a curve *look like* if we zoom in infinitely close?
        curve_question = Text("Calculus lets us ask: what does a curve *look like*\nif we zoom in infinitely close?", font_size=36)
        curve_question.next_to(speed_text, DOWN, buff=1)
        self.play(Write(curve_question))
        
        # Show a curve
        plane = NumberPlane(x_range=[-3, 3], y_range=[-2, 2], x_length=6, y_length=4)
        plane.scale(0.8)
        plane.next_to(curve_question, DOWN, buff=0.5)
        
        def curve_func(x):
            return 0.3 * x**3 - 0.5 * x**2 + 0.2 * x + 0.5
            
        curve = plane.plot(
            curve_func,
            x_range=[-2.5, 2.5],
            color=YELLOW,
            stroke_width=4
        )
        
        self.play(Create(plane), Create(curve))
        self.wait(5)
        
        # [0:35] Clear and transition
        self.play(FadeOut(speed_text, curve_question, plane, curve))
        
        # And then, how do we sum up an infinite number of these tiny, changing pieces to find a total?
        sum_text = Text("And then, how do we sum up an infinite number\nof these tiny, changing pieces to find a total?", font_size=40)
        self.play(Write(sum_text))
        
        # Show rectangles under a curve to illustrate summation
        plane2 = NumberPlane(x_range=[-2, 4], y_range=[-1, 3], x_length=6, y_length=4)
        plane2.scale(0.7)
        plane2.next_to(sum_text, DOWN, buff=0.5)
        
        def simple_curve(x):
            return 0.5 * x**2 + 0.5
            
        curve2 = plane2.plot(
            simple_curve,
            x_range=[0, 3],
            color=RED,
            stroke_width=4
        )
        
        # Create rectangles under the curve
        rectangles = VGroup()
        n_rects = 8
        dx = 3 / n_rects
        for i in range(n_rects):
            x = i * dx
            height = simple_curve(x)
            rect = Rectangle(
                width=dx * plane2.x_axis.unit_size,
                height=height * plane2.y_axis.unit_size,
                fill_opacity=0.3,
                fill_color=BLUE,
                stroke_width=1
            )
            rect.move_to(plane2.c2p(x + dx/2, height/2))
            rectangles.add(rect)
        
        self.play(Create(plane2), Create(curve2))
        self.play(Create(rectangles))
        self.wait(5)
        
        # [0:50] Clear and transition
        self.play(FadeOut(sum_text, plane2, curve2, rectangles))
        
        # It's seeing the world as continuous motion, and finding its precise measure.
        final_text = Text("It's seeing the world as continuous motion,\nand finding its precise measure.", font_size=44)
        self.play(Write(final_text))
        self.wait(4)
        
        # Final clear
        self.play(FadeOut(final_text))