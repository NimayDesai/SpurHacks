from manim import *

class VectorTransformationScene(Scene):
    def construct(self):
        # [0:00] Think of vectors not as static lists of numbers, but as dynamic arrows stretching from the origin.
        text1 = Text("Think of vectors not as static lists of numbers, but as dynamic arrows stretching from the origin.", 
                    font_size=36).scale(0.8)
        text1.move_to(UP * 2)
        
        # Create coordinate plane
        plane = NumberPlane(
            x_range=[-4, 4, 1],
            y_range=[-3, 3, 1],
            background_line_style={
                "stroke_color": BLUE_D,
                "stroke_width": 1,
                "stroke_opacity": 0.6
            }
        ).scale(0.7)
        
        # Create vector arrows from origin
        vector1 = Arrow(start=ORIGIN, end=[2, 1.5, 0], color=RED, buff=0, stroke_width=6)
        vector2 = Arrow(start=ORIGIN, end=[-1.5, 2, 0], color=GREEN, buff=0, stroke_width=6)
        vector3 = Arrow(start=ORIGIN, end=[1, -2, 0], color=YELLOW, buff=0, stroke_width=6)
        
        self.play(Write(text1))
        self.wait(0.5)
        self.play(Create(plane))
        self.play(Create(vector1), Create(vector2), Create(vector3))
        self.wait(2)
        
        # [0:08] Adding them is simply following one arrow's path after another.
        self.play(FadeOut(text1))
        text2 = Text("Adding them is simply following one arrow's path after another.", 
                    font_size=36).scale(0.8)
        text2.move_to(UP * 2.5)
        
        # Show vector addition
        vector_a = Arrow(start=ORIGIN, end=[2, 1, 0], color=RED, buff=0, stroke_width=6)
        vector_b = Arrow(start=[2, 1, 0], end=[2 + 1.5, 1 + 1.5, 0], color=GREEN, buff=0, stroke_width=6)
        vector_sum = Arrow(start=ORIGIN, end=[3.5, 2.5, 0], color=BLUE, buff=0, stroke_width=8)
        
        self.play(FadeOut(vector1, vector2, vector3))
        self.play(Write(text2))
        self.play(Create(vector_a))
        self.play(Create(vector_b))
        self.play(Create(vector_sum))
        self.wait(2)
        
        # [0:14] Multiplying by a scalar just stretches or shrinks these arrows.
        self.play(FadeOut(text2), FadeOut(vector_a, vector_b, vector_sum))
        text3 = Text("Multiplying by a scalar just stretches or shrinks these arrows.", 
                    font_size=36).scale(0.8)
        text3.move_to(UP * 2.5)
        
        # Show scalar multiplication
        original_vector = Arrow(start=ORIGIN, end=[2, 1.5, 0], color=RED, buff=0, stroke_width=6)
        scaled_vector_half = Arrow(start=ORIGIN, end=[1, 0.75, 0], color=ORANGE, buff=0, stroke_width=6)
        scaled_vector_double = Arrow(start=ORIGIN, end=[4, 3, 0], color=PURPLE, buff=0, stroke_width=6)
        
        self.play(Write(text3))
        self.play(Create(original_vector))
        self.play(Transform(original_vector.copy(), scaled_vector_half))
        self.wait(0.5)
        self.play(Transform(original_vector.copy(), scaled_vector_double))
        self.wait(2)
        
        # [0:20] Linear algebra truly blossoms when we consider how entire spaces can be systematically *transformed*.
        self.play(FadeOut(text3), FadeOut(original_vector, scaled_vector_half, scaled_vector_double))
        text4 = Text("Linear algebra truly blossoms when we consider how entire spaces can be systematically ", 
                    font_size=36).scale(0.8)
        text4_transform = Text("transformed", font_size=36, slant=ITALIC).scale(0.8)
        text4_period = Text(".", font_size=36).scale(0.8)
        
        text4_group = VGroup(text4, text4_transform, text4_period).arrange(RIGHT, buff=0.1)
        text4_group.move_to(UP * 2.5)
        
        # Show grid transformation
        grid = NumberPlane(
            x_range=[-3, 3, 0.5],
            y_range=[-2, 2, 0.5],
            background_line_style={
                "stroke_color": BLUE_D,
                "stroke_width": 1,
                "stroke_opacity": 0.4
            }
        ).scale(0.8)
        
        self.play(Write(text4_group))
        self.play(Create(grid))
        
        # Apply transformation to show space transformation
        self.play(grid.animate.apply_matrix([[1.5, 0.5], [0.3, 1.2]]))
        self.wait(4)
        
        # [0:30] A matrix, then, isn't just a grid of numbers; it's a concise description of one such transformation, guiding every point in space to a new destination.
        self.play(FadeOut(text4_group), FadeOut(grid), FadeOut(plane))
        text5 = Text("A matrix, then, isn't just a grid of numbers; it's a concise description of one such transformation, guiding every point in space to a new destination.", 
                    font_size=32).scale(0.8)
        text5.move_to(UP * 1.5)
        
        # Show matrix
        matrix = Matrix([["1.5", "0.5"], ["0.3", "1.2"]], bracket_h_buff=0.1, bracket_v_buff=0.1)
        matrix.scale(1.2)
        matrix.move_to(DOWN * 0.5)
        
        self.play(Write(text5))
        self.play(Write(matrix))
        self.wait(3)
        
        # Final cleanup
        self.play(FadeOut(text5), FadeOut(matrix))
        self.wait(1)