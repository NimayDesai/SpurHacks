from manim import *

class CalculusExplanation(Scene):
    def construct(self):
        # Define a simple function for the curves, demonstrating changing rates
        def f_speed(x):
            return x**1.5  # For accelerating car (speed increasing)

        def f_projectile(x):
            return -0.5 * (x - 2)**2 + 3.5  # For projectile (arcing path)

        def f_derivative(x):
            return 0.5 * x**2 + 0.5 * x + 1  # For derivative example

        def f_integral(x):
            return -0.5 * (x - 2)**2 + 4.5 # For integral example

        # --- Segment 1: Constant vs Changing Motion (0:00 - 0:20) ---

        # (0:00) We intuitively understand constant motion.
        constant_motion_text = Text("We intuitively understand constant motion.", font_size=40).to_edge(UP)
        self.play(Write(constant_motion_text), run_time=2) # 0:00 -> 0:02
        self.wait(1) # Current time: 0:03

        # If you travel at a steady speed, say 10 miles per hour, figuring out your distance is simple: just multiply.
        steady_speed_part1 = Text("If you travel at a steady speed, say 10 miles per hour,", font_size=30).next_to(constant_motion_text, DOWN)
        steady_speed_part2 = Text("figuring out your distance is simple: just multiply.", font_size=30).next_to(steady_speed_part1, DOWN)
        distance_formula = Tex("Distance = Speed ", r"$\times$", " Time").scale(0.8).next_to(steady_speed_part2, DOWN, buff=0.5)

        self.play(
            Transform(constant_motion_text, steady_speed_part1),
            Write(steady_speed_part2),
            Write(distance_formula),
            run_time=4
        ) # 0:03 -> 0:07
        self.wait(3) # Current time: 0:10

        # But what if your speed isn't constant? What if it’s continuously changing, like a car accelerating or a projectile arcing through the air?
        changing_speed_text = Text("But what if your speed isn't constant?", font_size=30).to_edge(UP)
        continuous_change_part1 = Text("What if it’s continuously changing, like a car accelerating", font_size=30).next_to(changing_speed_text, DOWN)
        continuous_change_part2 = Text("or a projectile arcing through the air?", font_size=30).next_to(continuous_change_part1, DOWN)

        self.play(
            Transform(constant_motion_text, changing_speed_text), # constant_motion_text now holds changing_speed_text
            FadeOut(steady_speed_part2, distance_formula),
            Write(continuous_change_part1),
            Write(continuous_change_part2),
            run_time=4
        ) # 0:10 -> 0:14

        # Visuals for changing speed (acceleration) and projectile motion
        axes_intro = Axes(
            x_range=[0, 5, 1],
            y_range=[0, 5, 1],
            x_length=6,
            y_length=4,
            axis_config={"color": GRAY},
            tips=False
        ).to_edge(DOWN)
        labels_intro = axes_intro.get_axis_labels(x_label="Time / Distance", y_label="Speed / Height")
        
        speed_curve = axes_intro.get_graph(f_speed, x_range=[0, 4.5], color=YELLOW)
        projectile_path = axes_intro.get_graph(f_projectile, x_range=[0, 4], color=GREEN)

        car_dot = Dot(axes_intro.c2p(0, f_speed(0)), color=RED)
        projectile_dot = Dot(axes_intro.c2p(0, f_projectile(0)), color=BLUE)

        car_label = Text("Car accelerating", font_size=20).next_to(speed_curve, UP, buff=0.2)
        projectile_label = Text("Projectile arcing", font_size=20).next_to(projectile_path, DOWN, buff=0.2)

        self.play(
            Create(axes_intro),
            Write(labels_intro),
            run_time=2
        ) # 0:14 -> 0:16
        self.play(
            Create(speed_curve),
            Create(projectile_path),
            Write(car_label),
            Write(projectile_label),
            MoveAlongPath(car_dot, speed_curve),
            MoveAlongPath(projectile_dot, projectile_path),
            run_time=4
        ) # 0:16 -> 0:20 (Reached 0:20 mark)

        self.remove(car_dot, projectile_dot) # Remove moving dots
        self.wait(0.5) # Slight buffer for next segment start

        # --- Segment 2: Derivatives (0:20 - 1:10) ---

        # (0:20) How do you even describe your speed at a single instant? Not over an hour, but right now?
        question_instant = Text("How do you even describe your speed at a single instant?", font_size=35).to_edge(UP)
        not_hour_text = Text("Not over an hour, but right now?", font_size=35).next_to(question_instant, DOWN)
        
        self.play(
            Transform(constant_motion_text, question_instant), # constant_motion_text now holds question_instant
            FadeOut(continuous_change_part1, continuous_change_part2, car_label, projectile_label),
            Write(not_hour_text),
            run_time=3
        ) # 0:20.5 -> 0:23.5
        self.wait(2.5) # Current time: 0:26

        # Algebra provides no direct pathway.
        algebra_text = Text("Algebra provides no direct pathway.", font_size=35).next_to(not_hour_text, DOWN)
        self.play(Write(algebra_text), run_time=2) # 0:26 -> 0:28
        self.wait(2) # Current time: 0:30

        # Calculus tackles this by zooming in.
        calculus_zoom_text = Text("Calculus tackles this by zooming in.", font_size=35).next_to(algebra_text, DOWN)
        self.play(Write(calculus_zoom_text), run_time=3) # 0:30 -> 0:33
        self.wait(4) # Current time: 0:37

        # Transition to derivative visual
        self.play(
            FadeOut(constant_motion_text, not_hour_text, algebra_text, calculus_zoom_text),
            FadeOut(speed_curve, projectile_path), # Clear previous curves
            run_time=1.5
        ) # 0:37 -> 0:38.5
        
        # New curve for derivative explanation
        derivative_curve_graph = axes_intro.get_graph(f_derivative, x_range=[0.5, 4.5], color=BLUE_A)
        self.play(Transform(axes_intro, axes_intro), # Keep axes, but transform the previous curve into the new one
                  Transform(labels_intro, labels_intro),
                  Create(derivative_curve_graph), run_time=1.5) # 0:38.5 -> 0:40 (Reached 0:40 mark)

        # (0:40) If you magnify any smoothly changing curve enough, it locally appears like a straight line.
        magnify_text = Text("If you magnify any smoothly changing curve enough, it locally appears like a straight line.", font_size=30).to_edge(UP)
        self.play(Write(magnify_text), run_time=3) # 0:40 -> 0:43
        
        point_x_deriv = 2.5
        point_on_graph = Dot(axes_intro.c2p(point_x_deriv, f_derivative(point_x_deriv)), color=RED)
        self.play(FadeIn(point_on_graph), run_time=1) # 0:43 -> 0:44

        self.camera.frame.save_state()
        self.play(
            self.camera.frame.animate.scale(0.2).move_to(point_on_graph),
            run_time=5
        ) # 0:44 -> 0:49
        self.wait(2) # Current time: 0:51

        # The derivative gives us the slope of that tiny line, revealing the instantaneous rate of change – how quickly something is evolving at that precise moment.
        # Calculate tangent slope for visualization
        h = 0.001
        slope = (f_derivative(point_x_deriv + h) - f_derivative(point_x_deriv)) / h
        
        # Create a tangent line visually (extended beyond the zoom)
        tangent_line_start = axes_intro.c2p(point_x_deriv - 1.5, f_derivative(point_x_deriv) - 1.5 * slope)
        tangent_line_end = axes_intro.c2p(point_x_deriv + 1.5, f_derivative(point_x_deriv) + 1.5 * slope)
        tangent_line = Line(tangent_line_start, tangent_line_end, color=YELLOW, stroke_width=5)

        derivative_text_part1 = Text("The derivative gives us the slope of that tiny line,", font_size=30).to_edge(UP)
        derivative_text_part2 = Text("revealing the instantaneous rate of change – how quickly something is evolving at that precise moment.", font_size=30).next_to(derivative_text_part1, DOWN)
        derivative_equation = Tex("$\\frac{dy}{dx}$ or $f'(x)$").scale(1.2).next_to(tangent_line, DOWN, buff=0.7)

        self.play(
            Restore(self.camera.frame), # Zoom out
            Transform(magnify_text, derivative_text_part1), # magnify_text now holds derivative_text_part1
            FadeIn(derivative_text_part2),
            Create(tangent_line),
            run_time=3
        ) # 0:51 -> 0:54
        self.play(Write(derivative_equation), run_time=2) # 0:54 -> 0:56
        self.wait(14) # Current time: 1:10 (Reached 1:10 mark)

        self.play(
            FadeOut(axes_intro, labels_intro, derivative_curve_graph, point_on_graph, tangent_line, 
                    magnify_text, derivative_text_part2, derivative_equation),
            run_time=2
        ) # 1:10 -> 1:12

        # --- Segment 3: Integrals (1:10 - 1:55) ---

        # (1:10) Now, flip the perspective. If you know how fast something is changing at every instant, how do you find the total amount accumulated?
        flip_perspective_text = Text("Now, flip the perspective.", font_size=35).to_edge(UP)
        accumulated_q_part1 = Text("If you know how fast something is changing at every instant,", font_size=30).next_to(flip_perspective_text, DOWN)
        accumulated_q_part2 = Text("how do you find the total amount accumulated?", font_size=30).next_to(accumulated_q_part1, DOWN)

        self.play(Write(flip_perspective_text), run_time=2) # 1:12 -> 1:14
        self.play(Write(accumulated_q_part1), run_time=2) # 1:14 -> 1:16
        self.play(Write(accumulated_q_part2), run_time=3) # 1:16 -> 1:19
        self.wait(6) # Current time: 1:25 (Reached 1:25 mark)

        # (1:25) Imagine breaking the entire process into tiny, tiny slices.
        # Over each slice, the rate is almost constant. Multiply rate by tiny time, then add all these minute contributions together.
        self.play(
            FadeOut(flip_perspective_text, accumulated_q_part1, accumulated_q_part2),
            run_time=1
        ) # 1:25 -> 1:26

        # Re-draw axes and a new curve for integration
        axes_integral = Axes(
            x_range=[0, 5, 1],
            y_range=[0, 5, 1],
            x_length=6,
            y_length=4,
            axis_config={"color": GRAY},
            tips=False
        ).to_edge(DOWN)
        labels_integral = axes_integral.get_axis_labels(x_label="Time", y_label="Rate")
        
        integral_curve_graph = axes_integral.get_graph(f_integral, x_range=[0.5, 4.5], color=ORANGE)

        self.play(Create(axes_integral), Create(labels_integral), Create(integral_curve_graph), run_time=3) # 1:26 -> 1:29

        slices_text = Text("Imagine breaking the entire process into tiny, tiny slices.", font_size=30).to_edge(UP)
        self.play(Write(slices_text), run_time=3) # 1:29 -> 1:32

        # Initial wide slices (Riemann sum)
        dx_wide = 0.8
        rects_wide = axes_integral.get_riemann_rectangles(
            integral_curve_graph, x_range=[0.5, 4.5], dx=dx_wide, color=TEAL_B, fill_opacity=0.7
        )
        self.play(Create(rects_wide), run_time=2) # 1:32 -> 1:34
        self.wait(1) # Current time: 1:35

        slices_explanation_part1 = Text("Over each slice, the rate is almost constant.", font_size=30).next_to(slices_text, DOWN)
        slices_explanation_part2 = Text("Multiply rate by tiny time, then add all these minute contributions together.", font_size=30).next_to(slices_explanation_part1, DOWN)
        
        self.play(
            FadeOut(slices_text),
            Write(slices_explanation_part1),
            Write(slices_explanation_part2),
            run_time=4
        ) # 1:35 -> 1:39
        self.wait(6) # Current time: 1:45 (Reached 1:45 mark)

        # (1:45) As these slices become infinitely thin, that sum becomes perfectly accurate.
        # This is the integral: the process of summing infinitely many infinitesimal pieces to find a total quantity.
        inf_thin_text = Text("As these slices become infinitely thin, that sum becomes perfectly accurate.", font_size=30).to_edge(UP)
        self.play(
            Transform(slices_explanation_part1, inf_thin_text), # slices_explanation_part1 now holds inf_thin_text
            FadeOut(slices_explanation_part2),
            run_time=3
        ) # 1:45 -> 1:48

        # Animate slices becoming thinner and more numerous
        dx_thin = 0.05
        rects_thin = axes_integral.get_riemann_rectangles(
            integral_curve_graph, x_range=[0.5, 4.5], dx=dx_thin, color=TEAL_B, fill_opacity=0.7
        )
        self.play(Transform(rects_wide, rects_thin), run_time=4) # 1:48 -> 1:52

        integral_definition_text = Text("This is the integral: the process of summing infinitely many infinitesimal pieces to find a total quantity.", font_size=30).next_to(inf_thin_text, DOWN)
        integral_equation = Tex("$\\int f(x) dx$").scale(1.5).next_to(axes_integral, UP, buff=0.7)

        self.play(Write(integral_definition_text), run_time=3) # 1:52 -> 1:55 (Reached 1:55 mark)
        self.play(Write(integral_equation), run_time=2) # 1:55 -> 1:57
        self.wait(3) # Current time: 2:00

        self.play(
            FadeOut(axes_integral, labels_integral, integral_curve_graph, rects_wide, 
                    inf_thin_text, integral_definition_text, integral_equation),
            run_time=2
        ) # 2:00 -> 2:02

        # --- Segment 4: Inverse Operations (1:55 - End) ---

        # (1:55) And here's the profound magic: these two ideas, derivatives and integrals, are fundamentally inverse operations, two sides of the same incredible coin, revealing the hidden dynamics of our universe.
        final_text = Text("And here's the profound magic: these two ideas, derivatives and integrals, are fundamentally inverse operations, two sides of the same incredible coin, revealing the hidden dynamics of our universe.", font_size=35).to_edge(UP)
        self.play(Write(final_text), run_time=5) # 2:02 -> 2:07

        deriv_sym = Tex("$\\frac{dy}{dx}$").scale(2.5).shift(LEFT * 3)
        integral_sym = Tex("$\\int f(x) dx$").scale(2.5).shift(RIGHT * 3)

        self.play(
            Write(deriv_sym),
            Write(integral_sym),
            run_time=3
        ) # 2:07 -> 2:10

        # Arrows indicating inverse relationship
        arrow1 = CurvedArrow(deriv_sym.get_right(), integral_sym.get_left(), angle=-TAU/4, color=YELLOW)
        arrow2 = CurvedArrow(integral_sym.get_left(), deriv_sym.get_right(), angle=-TAU/4, color=YELLOW)
        inverse_text_label = Text("Inverse Operations", font_size=30).next_to(arrow1, UP)

        self.play(Create(arrow1), Create(arrow2), Write(inverse_text_label), run_time=3) # 2:10 -> 2:13
        self.wait(7) # Current time: 2:20

        self.play(
            FadeOut(final_text, deriv_sym, integral_sym, arrow1, arrow2, inverse_text_label),
            run_time=2
        ) # 2:20 -> 2:22
        self.wait(1) # Final buffer, total 2:23
