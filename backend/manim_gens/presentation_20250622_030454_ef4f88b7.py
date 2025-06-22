from manim import *

class AlgebraIntro(Scene):
    def construct(self):
        # [0:00] Arithmetic works with known numbers to find an answer. But what if a number is unknown?
        arithmetic_text = Text("Arithmetic works with known numbers to find an answer.", font_size=36)
        arithmetic_text.move_to(UP * 1.5)
        
        # Visual: simple arithmetic example
        example1 = MathTex("5 + 3 = 8", font_size=48)
        example1.move_to(DOWN * 0.5)
        
        self.play(Write(arithmetic_text))
        self.play(Write(example1))
        self.wait(2)
        
        unknown_text = Text("But what if a number is unknown?", font_size=36)
        unknown_text.move_to(DOWN * 1.5)
        
        self.play(Write(unknown_text))
        self.wait(5)
        
        # [0:07] Algebra begins by asking: 'three plus *what* equals eight?' We use symbols, like 'x', for these hidden values.
        self.play(FadeOut(arithmetic_text), FadeOut(example1), FadeOut(unknown_text))
        
        algebra_text = Text("Algebra begins by asking:", font_size=36)
        algebra_text.move_to(UP * 2)
        
        question_text = Text("'three plus *what* equals eight?'", font_size=36)
        question_text.move_to(UP * 0.5)
        
        # Visual: algebraic equation
        equation = MathTex("3 + ? = 8", font_size=48)
        equation.move_to(DOWN * 0.5)
        
        self.play(Write(algebra_text))
        self.play(Write(question_text))
        self.play(Write(equation))
        self.wait(2)
        
        symbols_text = Text("We use symbols, like 'x', for these hidden values.", font_size=36)
        symbols_text.move_to(DOWN * 2)
        
        # Transform the equation to use x
        equation_x = MathTex("3 + x = 8", font_size=48)
        equation_x.move_to(DOWN * 0.5)
        
        self.play(Write(symbols_text))
        self.play(Transform(equation, equation_x))
        self.wait(6)
        
        # [0:15] The core insight is balance: an equation is like a perfectly balanced scale.
        self.play(FadeOut(algebra_text), FadeOut(question_text), FadeOut(equation), FadeOut(symbols_text))
        
        balance_text = Text("The core insight is balance:", font_size=36)
        balance_text.move_to(UP * 2)
        
        scale_text = Text("an equation is like a perfectly balanced scale.", font_size=36)
        scale_text.move_to(UP * 0.5)
        
        # Visual: balance scale
        # Create a simple balance scale representation
        fulcrum = Triangle(color=GRAY, fill_opacity=1).scale(0.3)
        fulcrum.move_to(DOWN * 0.5)
        
        left_plate = Rectangle(width=1.5, height=0.2, color=BROWN, fill_opacity=1)
        left_plate.move_to(LEFT * 2 + DOWN * 0.2)
        
        right_plate = Rectangle(width=1.5, height=0.2, color=BROWN, fill_opacity=1)
        right_plate.move_to(RIGHT * 2 + DOWN * 0.2)
        
        left_support = Line(fulcrum.get_top(), left_plate.get_bottom(), color=GRAY)
        right_support = Line(fulcrum.get_top(), right_plate.get_bottom(), color=GRAY)
        
        # Add equation parts on the scale
        left_side = MathTex("3 + x", font_size=32)
        left_side.move_to(LEFT * 2 + UP * 0.2)
        
        right_side = MathTex("8", font_size=32)
        right_side.move_to(RIGHT * 2 + UP * 0.2)
        
        scale_group = VGroup(fulcrum, left_plate, right_plate, left_support, right_support)
        
        self.play(Write(balance_text))
        self.play(Write(scale_text))
        self.play(Create(scale_group))
        self.play(Write(left_side), Write(right_side))
        self.wait(4)
        
        # [0:21] Whatever you do to one side, you must do to the other. This simple rule lets us systematically isolate and unveil any unknown, extending arithmetic's power to solve vast new problems.
        self.play(FadeOut(balance_text), FadeOut(scale_text), FadeOut(scale_group), FadeOut(left_side), FadeOut(right_side))
        
        rule_text1 = Text("Whatever you do to one side,", font_size=36)
        rule_text1.move_to(UP * 2)
        
        rule_text2 = Text("you must do to the other.", font_size=36)
        rule_text2.move_to(UP * 1)
        
        # Visual: equation transformation
        original_eq = MathTex("3 + x = 8", font_size=40)
        original_eq.move_to(UP * 0.2)
        
        # Show subtracting 3 from both sides
        subtract_text = Text("Subtract 3 from both sides:", font_size=28)
        subtract_text.move_to(DOWN * 0.5)
        
        transformed_eq = MathTex("x = 5", font_size=40)
        transformed_eq.move_to(DOWN * 1.2)
        
        self.play(Write(rule_text1))
        self.play(Write(rule_text2))
        self.play(Write(original_eq))
        self.wait(2)
        
        self.play(Write(subtract_text))
        self.play(Write(transformed_eq))
        self.wait(2)
        
        conclusion_text1 = Text("This simple rule lets us systematically isolate", font_size=32)
        conclusion_text1.move_to(DOWN * 2.2)
        
        conclusion_text2 = Text("and unveil any unknown, extending arithmetic's", font_size=32)
        conclusion_text2.move_to(DOWN * 2.8)
        
        conclusion_text3 = Text("power to solve vast new problems.", font_size=32)
        conclusion_text3.move_to(DOWN * 3.4)
        
        self.play(Write(conclusion_text1))
        self.play(Write(conclusion_text2))
        self.play(Write(conclusion_text3))
        self.wait(3)
        
        # Clear all elements at the end
        self.play(FadeOut(*self.mobjects))