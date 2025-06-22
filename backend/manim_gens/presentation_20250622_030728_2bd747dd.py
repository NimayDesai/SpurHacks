from manim import *

class AlgebraScale(Scene):
    def construct(self):
        # [0:00] Imagine a perfectly balanced scale, where each side must always weigh the same.
        text1 = Text("Imagine a perfectly balanced scale, where each side\nmust always weigh the same.", font_size=36)
        text1.move_to(UP * 2)
        
        # Create a balanced scale visual
        fulcrum = Triangle(color=GRAY, fill_opacity=1).scale(0.5)
        fulcrum.rotate(PI)
        
        beam = Rectangle(width=6, height=0.2, color=BROWN, fill_opacity=1)
        beam.move_to(fulcrum.get_top() + UP * 0.1)
        
        left_pan = Circle(radius=0.8, color=GOLD, fill_opacity=0.8)
        left_pan.move_to(beam.get_left() + DOWN * 1.2)
        
        right_pan = Circle(radius=0.8, color=GOLD, fill_opacity=0.8)
        right_pan.move_to(beam.get_right() + DOWN * 1.2)
        
        left_chain = Line(beam.get_left(), left_pan.get_top(), color=GRAY)
        right_chain = Line(beam.get_right(), right_pan.get_top(), color=GRAY)
        
        scale = VGroup(fulcrum, beam, left_pan, right_pan, left_chain, right_chain)
        scale.move_to(DOWN * 0.5)
        
        self.play(Write(text1))
        self.wait(1)
        self.play(Create(scale))
        self.wait(4)
        
        # [0:06] Algebra is essentially working with these scales. We use letters, like 'x', not just as unknowns, but as flexible placeholders for quantities we want to understand.
        self.play(FadeOut(text1), FadeOut(scale))
        
        text2 = Text("Algebra is essentially working with these scales.\nWe use letters, like 'x', not just as unknowns,\nbut as flexible placeholders for quantities\nwe want to understand.", font_size=32)
        text2.move_to(UP * 1.5)
        
        # Show algebraic equation on a scale
        equation_scale = VGroup(fulcrum, beam, left_pan, right_pan, left_chain, right_chain).copy()
        equation_scale.scale(0.7)
        equation_scale.move_to(DOWN * 1)
        
        x_term = MathTex("x + 3", font_size=48, color=BLUE)
        x_term.move_to(left_pan.get_center() + DOWN * 1)
        
        number_term = MathTex("7", font_size=48, color=RED)
        number_term.move_to(right_pan.get_center() + DOWN * 1)
        
        self.play(Write(text2))
        self.wait(2)
        self.play(Create(equation_scale))
        self.play(Write(x_term), Write(number_term))
        self.wait(8)
        
        # [0:18] The magic lies in manipulating these relationships: if you add something to one side, you must add it to the other to keep the balance.
        self.play(FadeOut(text2))
        
        text3 = Text("The magic lies in manipulating these relationships:\nif you add something to one side, you must add it\nto the other to keep the balance.", font_size=32)
        text3.move_to(UP * 2.5)
        
        self.play(Write(text3))
        self.wait(2)
        
        # Show manipulation
        subtract_3 = MathTex("-3", font_size=36, color=GREEN)
        subtract_3_left = subtract_3.copy().move_to(left_pan.get_center() + DOWN * 1.8)
        subtract_3_right = subtract_3.copy().move_to(right_pan.get_center() + DOWN * 1.8)
        
        self.play(Write(subtract_3_left), Write(subtract_3_right))
        self.wait(2)
        
        # Show result
        x_result = MathTex("x", font_size=48, color=BLUE)
        x_result.move_to(left_pan.get_center() + DOWN * 1)
        
        result_4 = MathTex("4", font_size=48, color=RED)
        result_4.move_to(right_pan.get_center() + DOWN * 1)
        
        self.play(Transform(x_term, x_result), Transform(number_term, result_4))
        self.play(FadeOut(subtract_3_left), FadeOut(subtract_3_right))
        self.wait(6)
        
        # [0:28] This simple idea lets us uncover hidden values and generalize patterns far beyond mere numbers.
        self.play(FadeOut(text3), FadeOut(equation_scale), FadeOut(x_term), FadeOut(number_term))
        
        text4 = Text("This simple idea lets us uncover hidden values\nand generalize patterns far beyond mere numbers.", font_size=36)
        text4.move_to(UP * 1)
        
        # Show pattern generalization
        pattern_examples = VGroup(
            MathTex("2x + 1 = 9", font_size=32),
            MathTex("3y - 5 = 16", font_size=32),
            MathTex("a^2 + b^2 = c^2", font_size=32),
            MathTex("f(x) = mx + b", font_size=32)
        )
        pattern_examples.arrange(DOWN, buff=0.8)
        pattern_examples.move_to(DOWN * 0.5)
        
        self.play(Write(text4))
        self.wait(2)
        self.play(Write(pattern_examples))
        self.wait(8)
        
        # [0:38] It's a language for describing how quantities interact.
        self.play(FadeOut(text4), FadeOut(pattern_examples))
        
        text5 = Text("It's a language for describing how quantities interact.", font_size=40)
        text5.move_to(ORIGIN)
        
        self.play(Write(text5))
        self.wait(4)
        
        self.play(FadeOut(text5))