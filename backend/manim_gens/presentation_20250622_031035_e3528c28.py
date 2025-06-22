from manim import *

class AlgebraIntroScript(Scene):
    def construct(self):
        # (0:00) Algebra often begins with a simple question: what value makes this statement true?
        opening_text = Text("Algebra often begins with a simple question:", font_size=36)
        question_text = Text("what value makes this statement true?", font_size=36)
        opening_group = VGroup(opening_text, question_text).arrange(DOWN, buff=0.5)
        
        self.play(Write(opening_text))
        self.wait(0.5)
        self.play(Write(question_text))
        self.wait(1.5)
        
        # Clear for next section
        self.play(FadeOut(opening_group))
        
        # (0:07) Imagine balancing scales: one side has a known weight and an unknown, the other has a total. Algebra helps find that missing amount.
        scales_text = Text("Imagine balancing scales:", font_size=32)
        description_text1 = Text("one side has a known weight and an unknown,", font_size=28)
        description_text2 = Text("the other has a total.", font_size=28)
        algebra_text = Text("Algebra helps find that missing amount.", font_size=28)
        
        scales_group = VGroup(scales_text, description_text1, description_text2, algebra_text).arrange(DOWN, buff=0.4)
        
        # Create visual representation of balance scales
        scale_base = Line(LEFT * 3, RIGHT * 3, color=GRAY)
        scale_pivot = Line(UP * 0.3, DOWN * 0.3, color=GRAY).move_to(ORIGIN)
        left_plate = Rectangle(width=1.5, height=0.2, color=BLUE).move_to(LEFT * 2 + UP * 0.8)
        right_plate = Rectangle(width=1.5, height=0.2, color=BLUE).move_to(RIGHT * 2 + UP * 0.8)
        left_chain = Line(LEFT * 2, LEFT * 2 + UP * 0.8, color=GRAY)
        right_chain = Line(RIGHT * 2, RIGHT * 2 + UP * 0.8, color=GRAY)
        
        # Known weight and unknown on left side
        known_weight = Rectangle(width=0.5, height=0.3, color=GREEN).move_to(LEFT * 2.5 + UP * 1)
        unknown_weight = Text("?", color=RED).move_to(LEFT * 1.5 + UP * 1)
        
        # Total on right side
        total_weight = Rectangle(width=0.8, height=0.4, color=ORANGE).move_to(RIGHT * 2 + UP * 1)
        
        scales_visual = VGroup(scale_base, scale_pivot, left_plate, right_plate, left_chain, right_chain, 
                              known_weight, unknown_weight, total_weight).scale(0.8).to_edge(DOWN)
        
        self.play(Write(scales_text))
        self.wait(0.5)
        self.play(Create(scales_visual))
        self.play(Write(description_text1))
        self.wait(0.5)
        self.play(Write(description_text2))
        self.wait(0.5)
        self.play(Write(algebra_text))
        self.wait(4)
        
        # Clear for next section
        self.play(FadeOut(scales_group), FadeOut(scales_visual))
        
        # (0:20) We replace unknowns with symbols, like 'x', and represent relationships as equations.
        replace_text = Text("We replace unknowns with symbols, like 'x',", font_size=32)
        equations_text = Text("and represent relationships as equations.", font_size=32)
        replace_group = VGroup(replace_text, equations_text).arrange(DOWN, buff=0.5)
        
        # Show example equation
        example_equation = MathTex("3 + x = 8", font_size=48, color=YELLOW)
        
        self.play(Write(replace_text))
        self.wait(0.5)
        self.play(Write(equations_text))
        self.wait(0.5)
        self.play(Write(example_equation.move_to(DOWN * 1)))
        self.wait(4)
        
        # Clear for next section
        self.play(FadeOut(replace_group), FadeOut(example_equation))
        
        # (0:30) Then, by applying inverse operations equally to both sides, we isolate the variable, revealing its hidden value.
        then_text = Text("Then, by applying inverse operations equally to both sides,", font_size=30)
        isolate_text = Text("we isolate the variable, revealing its hidden value.", font_size=30)
        final_group = VGroup(then_text, isolate_text).arrange(DOWN, buff=0.5)
        
        # Show solving process
        step1 = MathTex("3 + x = 8", font_size=40)
        step2 = MathTex("3 + x - 3 = 8 - 3", font_size=40)
        step3 = MathTex("x = 5", font_size=40, color=GREEN)
        
        solving_steps = VGroup(step1, step2, step3).arrange(DOWN, buff=0.8).move_to(DOWN * 1)
        
        self.play(Write(then_text))
        self.wait(0.5)
        self.play(Write(isolate_text))
        self.wait(0.5)
        
        self.play(Write(step1))
        self.wait(1)
        self.play(Transform(step1, step2))
        self.wait(1)
        self.play(Transform(step1, step3))
        self.wait(2)
        
        # Final fade out
        self.play(FadeOut(final_group), FadeOut(step1))
        self.wait(1)