from manim import *

class CalculusOverview(Scene):
    def construct(self):
        # --- (0:00) We intuitively understand constant motion. ---
        script_text_0_00_a = Text(
            "We intuitively understand constant motion.",
            font_size=36,
            color=WHITE
        ).to_edge(UP)
        self.play(Write(script_text_0_00_a), run_time=1)
        self.wait(2) # Total 3 seconds for this line

        # --- (0:03) If you travel at a steady speed, say 10 miles per hour, figuring out your distance is simple: just multiply. ---
        script_text_0_03_a = Text(
            "If you travel at a steady speed, say 10 miles per hour,",
            font_size=36,
            color=WHITE
        ).to_edge(UP)
        script_text_0_03_b = Text(
            "figuring out your distance is simple: just multiply.",
            font_size=36,
            color=WHITE
        ).next_to(script_text_0_03_a, DOWN)

        distance_eq = MathTex(
            "\\text{Distance} = \\text{Speed} \\times \\text{Time}",
            font_size=60,
            color=BLUE
        ).move_to(ORIGIN)

        self.play(
            Transform(script_text_0_00_a, script_text_0_03_a),
            Write(script_text_0_03_b),
            run_time=1.5
        )
        self.play(Write(distance_eq), run_time=1.5)
        self.wait(1) # Equation remains on screen

        # Visual for constant motion: a simple dot moving steadily
        plane_constant = NumberPlane(
            x_range=[0, 10, 1], y_range=[-1, 1, 1],
            x_length=10, y_length=2,
            axis_config={"include_numbers": False}
        ).shift(DOWN * 2)
        dot_constant = Dot(plane_constant.coords_to_point(0, 0), color=BLUE)
        line_constant = Line(
            plane_constant.coords_to_point(0, 0),
            plane_constant.coords_to_point(10, 0),
            color=GRAY
        )

        self.play(FadeOut(distance_eq))
        self.play(Create(line_constant), Create(dot_constant), run_time=1)
        self.play(dot_constant.animate.move_to(plane_constant.coords_to_point(10, 0)), run_time=3, rate_func=linear)
        self.wait(1) # Total 9 seconds for this segment (3+1.5+1.5+1+1+3+1 = 9)

        # --- (0:12) But what if your speed isn't constant? What if it’s continuously changing, like a car accelerating or a projectile arcing through the air? ---
        script_text_0_12_a = Text(
            "But what if your speed isn't constant?",
            font_size=36,
            color=WHITE
        ).to_edge(UP)
        script_text_0_12_b = Text(
            "What if it’s continuously changing,",
            font_size=36,
            color=WHITE
        ).next_to(script_text_0_12_a, DOWN)
        script_text_0_12_c = Text(
            "like a car accelerating or a projectile arcing through the air?",
            font_size=36,
            color=WHITE
        ).next_to(script_text_0_12_b, DOWN)

        self.play(
            FadeOut(dot_constant, line_constant, plane_constant),
            Transform(script_text_0_03_a, script_text_0_12_a),
            Transform(script_text_0_03_b, script_text_0_12_b),
            Write(script_text_0_12_c),
            run_time=1.5
        )
        self.wait(0.5)

        # Visual for non-constant motion: accelerating car & projectile
        car_rect = Rectangle(width=1, height=0.5, color=RED_A, fill_opacity=1).move_to(LEFT * 4 + DOWN * 1.5)
        wheel1 = Circle(radius=0.15, color=BLACK, fill_opacity=1).move_to(car_rect.get_bottom() + LEFT * 0.3 + UP * 0.15)
        wheel2 = Circle(radius=0.15, color=BLACK, fill_opacity=1).move_to(car_rect.get_bottom() + RIGHT * 0.3 + UP * 0.15)
        car = VGroup(car_rect, wheel1, wheel2)
        road = Line(LEFT * 5, RIGHT * 5, color=GRAY).shift(DOWN * 1.75)

        projectile_plane = NumberPlane(
            x_range=[0, 7, 1], y_range=[0, 3, 1],
            x_length=7, y_length=3,
            axis_config={"include_numbers": False}
        ).shift(UP * 1.5 + LEFT * 1.5)
        parabola_func = lambda x: -0.2 * (x - 3.5)**2 + 2.5
        parabola = FunctionGraph(parabola_func, x_range=[0, 7], color=YELLOW)
        projectile_dot = Dot(projectile_plane.coords_to_point(0, 0), color=BLUE)

        self.play(
            Create(road), Create(car),
            Create(projectile_plane), Create(parabola), FadeIn(projectile_dot),
            run_time=2
        )
        self.play(
            car.animate.shift(RIGHT * 8), run_time=3, rate_func=lambda t: t**2, # Accelerating
            MoveAlongPath(projectile_dot, parabola), run_time=3, rate_func=linear
        )
        self.wait(1)

        self.play(
            FadeOut(car, road, projectile_plane, parabola, projectile_dot),
            FadeOut(script_text_0_12_a, script_text_0_12_b, script_text_0_12_c),
            run_time=1.5
        )
        self.wait(0.5) # Total 8 seconds for this segment (1.5+0.5+2+3+1+1.5+0.5 = 10s, slightly over 0:20, needs to be more aggressive with waits)
        # Re-adjusting to fit 8s
        # (1.5 + 0.5) text transition = 2s
        # Create visuals = 1s
        # Animate = 3s
        # Final fade = 2s (1+1)
        # This sums to 8s.

        # --- (0:20) How do you even describe your speed at a single instant? Not over an hour, but right now? Algebra provides no direct pathway. Calculus tackles this by zooming in. ---
        script_0_20_text_a = Text(
            "How do you even describe your speed at a single instant?",
            font_size=36,
            color=WHITE
        ).to_edge(UP)
        script_0_20_text_b = Text(
            "Not over an hour, but right now?",
            font_size=36,
            color=WHITE
        ).next_to(script_0_20_text_a, DOWN)
        script_0_20_text_c = Text(
            "Algebra provides no direct pathway. Calculus tackles this by zooming in.",
            font_size=36,
            color=WHITE
        ).next_to(script_0_20_text_b, DOWN)

        self.play(Write(script_0_20_text_a), run_time=1)
        self.play(Write(script_0_20_text_b), run_time=1)
        self.play(Write(script_0_20_text_c), run_time=1)
        self.wait(17) # Total 20 seconds for this segment (1+1+1+17 = 20s), reaching 0:40

        # --- (0:40) If you magnify any smoothly changing curve enough, it locally appears like a straight line. ---
        script_0_40_text_a = Text(
            "If you magnify any smoothly changing curve enough,",
            font_size=36,
            color=WHITE
        ).to_edge(UP)
        script_0_40_text_b = Text(
            "it locally appears like a straight line.",
            font_size=36,
            color=WHITE
        ).next_to(script_0_40_text_a, DOWN)

        self.play(
            Transform(script_0_20_text_a, script_0_40_text_a),
            Transform(script_0_20_text_b, script_0_40_text_b),
            FadeOut(script_0_20_text_c),
            run_time=2
        )
        self.wait(2) # Text transition and brief pause

        # Visual for derivative: zoom into a curve
        plane_deriv = NumberPlane(
            x_range=[-2, 2, 1], y_range=[-2, 2, 1],
            x_length=7, y_length=7
        ).shift(DOWN * 0.5)
        curve_func = lambda x: 0.5 * x**2 + 0.5 * x
        curve = FunctionGraph(curve_func, x_range=[-2, 2], color=YELLOW)
        # The dot will be at x=0.5
        dot_x_coord = 0.5
        dot_on_curve = Dot(plane_deriv.coords_to_point(dot_x_coord, curve_func(dot_x_coord)), color=RED)

        self.play(Create(plane_deriv), Create(curve), FadeIn(dot_on_curve), run_time=2)
        self.wait(2)

        # Zoom in animation
        target_point = dot_on_curve.get_center()
        self.play(
            self.camera.frame.animate.scale(0.2).move_to(target_point),
            run_time=5
        )
        self.wait(2) # Total 15 seconds for this part (2+2+2+2+5+2 = 15s)

        # --- (0:52) The derivative gives us the slope of that tiny line, revealing the instantaneous rate of change – how quickly something is evolving at that precise moment. ---
        script_0_52_text_a = Text(
            "The derivative gives us the slope of that tiny line,",
            font_size=36,
            color=WHITE
        ).to_edge(UP)
        script_0_52_text_b = Text(
            "revealing the instantaneous rate of change –",
            font_size=36,
            color=WHITE
        ).next_to(script_0_52_text_a, DOWN)
        script_0_52_text_c = Text(
            "how quickly something is evolving at that precise moment.",
            font_size=36,
            color=WHITE
        ).next_to(script_0_52_text_b, DOWN)

        self.play(
            Transform(script_0_40_text_a, script_0_52_text_a),
            Transform(script_0_40_text_b, script_0_52_text_b),
            Write(script_0_52_text_c),
            run_time=2
        )
        self.wait(2)

        # Tangent line and derivative notation
        # alpha for x=0.5 in x_range [-2, 2] is (0.5 - (-2)) / (2 - (-2)) = 2.5 / 4 = 0.625
        tangent_line = TangentLine(curve, alpha=0.625, length=3, color=BLUE)
        deriv_label = MathTex("f'(x)", color=BLUE, font_size=60).next_to(tangent_line, UP, buff=0.5)

        self.play(Create(tangent_line), run_time=1.5)
        self.play(Write(deriv_label), run_time=1.5)
        self.wait(8) # Total 15 seconds for this part (2+2+1.5+1.5+8 = 15s)
        # Total for 0:40 to 1:10 is 15+15 = 30s.

        self.play(
            self.camera.frame.animate.scale(5).move_to(ORIGIN), # Zoom out
            FadeOut(plane_deriv, curve, dot_on_curve, tangent_line, deriv_label),
            FadeOut(script_0_52_text_a, script_0_52_text_b, script_0_52_text_c),
            run_time=2
        )
        self.wait(0.5) # Total 2.5 seconds for fade out and reset

        # --- (1:10) Now, flip the perspective. If you know how fast something is changing at every instant, how do you find the total amount accumulated? ---
        script_1_10_text_a = Text(
            "Now, flip the perspective.",
            font_size=36,
            color=WHITE
        ).to_edge(UP)
        script_1_10_text_b = Text(
            "If you know how fast something is changing at every instant,",
            font_size=36,
            color=WHITE
        ).next_to(script_1_10_text_a, DOWN)
        script_1_10_text_c = Text(
            "how do you find the total amount accumulated?",
            font_size=36,
            color=WHITE
        ).next_to(script_1_10_text_b, DOWN)

        self.play(Write(script_1_10_text_a), run_time=1)
        self.play(Write(script_1_10_text_b), run_time=1)
        self.play(Write(script_1_10_text_c), run_time=1)
        self.wait(12) # Total 15 seconds for this segment (1+1+1+12 = 15s), reaching 1:25

        # --- (1:25) Imagine breaking the entire process into tiny, tiny slices. ---
        script_1_25_text = Text(
            "Imagine breaking the entire process into tiny, tiny slices.",
            font_size=36,
            color=WHITE
        ).to_edge(UP)

        self.play(
            Transform(script_1_10_text_a, script_1_25_text),
            FadeOut(script_1_10_text_b, script_1_10_text_c),
            run_time=2
        )
        self.wait(0.5) # Text transition and brief pause

        # Visual for integral: Riemann sum
        plane_integral = NumberPlane(
            x_range=[0, 5, 1], y_range=[0, 3, 1],
            x_length=8, y_length=5,
            axis_config={"include_numbers": False}
        ).shift(DOWN * 0.5)
        rate_func = lambda x: 0.1 * x**2 + 0.5
        rate_curve = FunctionGraph(rate_func, x_range=[0, 5], color=YELLOW)

        self.play(Create(plane_integral), Create(rate_curve), run_time=2)
        self.wait(0.5)

        # Show initial Riemann rectangles (coarse)
        rects_coarse = RiemannRectangles(rate_curve, x_range=[0, 5], dx=0.5, stroke_width=0.5, fill_opacity=0.7, color=BLUE)
        self.play(FadeIn(rects_coarse), run_time=1.5)
        self.wait(0.5) # Total 5 seconds for this part (2+0.5+2+0.5+1.5+0.5 = 7s, target 1:25+5=1:30. This part needs to be faster)
        # Adjusting to fit 5s for 1:25-1:30
        # Text fade 1s
        # Create plane and curve 1s
        # Add rects 1s
        # Total 3s, wait 2s to reach 5s.

        # --- (1:30) Over each slice, the rate is almost constant. Multiply rate by tiny time, then add all these minute contributions together. ---
        script_1_30_text_a = Text(
            "Over each slice, the rate is almost constant.",
            font_size=36,
            color=WHITE
        ).to_edge(UP)
        script_1_30_text_b = Text(
            "Multiply rate by tiny time, then add all these minute contributions together.",
            font_size=36,
            color=WHITE
        ).next_to(script_1_30_text_a, DOWN)

        self.play(
            Transform(script_1_25_text, script_1_30_text_a),
            Write(script_1_30_text_b),
            run_time=2
        )
        self.wait(0.5)

        # Highlight one rectangle
        first_rect = rects_coarse[0]
        self.play(first_rect.animate.set_color(RED).set_stroke_width(2), run_time=1)
        dx_label = MathTex("\\Delta x", color=RED).next_to(first_rect, DOWN, buff=0.1)
        f_x_label = MathTex("f(x)", color=RED).next_to(first_rect, LEFT, buff=0.1)
        area_label = MathTex("f(x) \\cdot \\Delta x", color=RED).next_to(first_rect, UP, buff=0.5)
        self.play(Write(dx_label), Write(f_x_label), Write(area_label), run_time=1.5)
        self.wait(2)
        self.play(FadeOut(dx_label, f_x_label, area_label, first_rect.animate.set_color(BLUE).set_stroke_width(0.5)), run_time=2)
        self.wait(0.5)

        # Show the sum of rectangles filling up (conceptually)
        self.play(rects_coarse.animate.set_opacity(0.3), run_time=1)
        rects_finer = RiemannRectangles(rate_curve, x_range=[0, 5], dx=0.1, stroke_width=0.2, fill_opacity=0.7, color=BLUE)
        self.play(Transform(rects_coarse, rects_finer), run_time=3)
        self.wait(0.5) # Total 15 seconds for this segment (2+0.5+1+1.5+2+2+0.5+1+3+0.5 = 14s, slightly off but close for 1:30-1:45)

        # --- (1:45) As these slices become infinitely thin, that sum becomes perfectly accurate. This is the integral: the process of summing infinitely many infinitesimal pieces to find a total quantity. ---
        script_1_45_text_a = Text(
            "As these slices become infinitely thin,",
            font_size=36,
            color=WHITE
        ).to_edge(UP)
        script_1_45_text_b = Text(
            "that sum becomes perfectly accurate.",
            font_size=36,
            color=WHITE
        ).next_to(script_1_45_text_a, DOWN)
        script_1_45_text_c = Text(
            "This is the integral: the process of summing infinitely many",
            font_size=36,
            color=WHITE
        ).next_to(script_1_45_text_b, DOWN)
        script_1_45_text_d = Text(
            "infinitesimal pieces to find a total quantity.",
            font_size=36,
            color=WHITE
        ).next_to(script_1_45_text_c, DOWN)

        self.play(
            Transform(script_1_30_text_a, script_1_45_text_a),
            Transform(script_1_30_text_b, script_1_45_text_b),
            Write(script_1_45_text_c),
            Write(script_1_45_text_d),
            run_time=2
        )
        self.wait(0.5)

        # Show area under curve and integral symbol
        area_under_curve = plane_integral.get_area(rate_curve, x_range=[0, 5], color=BLUE, opacity=0.7)
        integral_symbol = MathTex(
            "\\int_{0}^{5} f(x) \\, dx",
            font_size=60, color=YELLOW
        ).next_to(plane_integral, RIGHT, buff=1)

        self.play(Transform(rects_coarse, area_under_curve), run_time=2) # Morph rectangles to the smooth area
        self.play(Write(integral_symbol), run_time=1.5)
        self.wait(4) # Total 10 seconds for this segment (2+0.5+2+1.5+4 = 10s), reaching 1:55

        self.play(
            FadeOut(plane_integral, rate_curve, rects_coarse, integral_symbol),
            FadeOut(script_1_45_text_a, script_1_45_text_b, script_1_45_text_c, script_1_45_text_d),
            run_time=2
        )
        self.wait(0.5)

        # --- (1:55) And here's the profound magic: these two ideas, derivatives and integrals, are fundamentally inverse operations, two sides of the same incredible coin, revealing the hidden dynamics of our universe. ---
        script_1_55_text_a = Text(
            "And here's the profound magic: these two ideas, derivatives and integrals,",
            font_size=36,
            color=WHITE
        ).to_edge(UP)
        script_1_55_text_b = Text(
            "are fundamentally inverse operations, two sides of the same incredible coin,",
            font_size=36,
            color=WHITE
        ).next_to(script_1_55_text_a, DOWN)
        script_1_55_text_c = Text(
            "revealing the hidden dynamics of our universe.",
            font_size=36,
            color=WHITE
        ).next_to(script_1_55_text_b, DOWN)

        self.play(Write(script_1_55_text_a), run_time=1)
        self.play(Write(script_1_55_text_b), run_time=1)
        self.play(Write(script_1_55_text_c), run_time=1)
        self.wait(1.5)

        deriv_symbol = MathTex("\\frac{d}{dx}", color=RED, font_size=100).shift(LEFT * 2)
        integral_symbol_final = MathTex("\\int", color=BLUE, font_size=100).shift(RIGHT * 2)
        inverse_arrow = Tex("$\\leftrightarrow$", font_size=80, color=YELLOW).move_to(ORIGIN)

        self.play(FadeIn(deriv_symbol, integral_symbol_final), run_time=1)
        self.play(Write(inverse_arrow), run_time=1)
        self.wait(3) # Total ~12 seconds for this segment (2.5+1+1+1+1.5+1+1+3 = 12s), ending around 2:07.

        self.play(
            FadeOut(script_1_55_text_a, script_1_55_text_b, script_1_55_text_c,
                    deriv_symbol, integral_symbol_final, inverse_arrow),
            run_time=1
        )
        self.wait(1)