from manim import *
import numpy as np

class CalculusIntroduction(Scene):
    def construct(self):
        # Set up a consistent text style for narration
        narration_text_config = {"font_size": 30, "color": WHITE}

        # --- [0:00] Section: Introduction to change and the problem statement ---
        narration_p1 = Text(
            "The world around us is rarely static. Things grow, they decay, they move, they accelerate.",
            **narration_text_config
        ).to_edge(UP)

        narration_q1 = Text(
            "But how do we precisely describe change when it's not a simple, constant rate?",
            **narration_text_config
        ).next_to(narration_p1, DOWN, buff=0.4)

        narration_q2 = Text(
            "How do we measure the speed of a car *at a single instant*",
            **narration_text_config
        ).next_to(narration_q1, DOWN, buff=0.4)

        narration_q2_cont = Text(
            "when its velocity is continuously shifting?",
            **narration_text_config
        ).next_to(narration_q2, DOWN, buff=0.2)

        initial_line = Line(LEFT * 2, RIGHT * 2, color=BLUE, stroke_width=4)
        grow_line = Line(LEFT * 3, RIGHT * 3, color=BLUE, stroke_width=4)
        decay_line = Line(LEFT * 1, RIGHT * 1, color=BLUE, stroke_width=4)

        dot_moving = Dot(LEFT * 4, color=RED)
        # Use ParametricFunction instead of FunctionGraph for a standalone path
        path_curve = ParametricFunction(
            lambda t: np.array([t, 0.5 * np.sin(2 * t) + 0.1 * t, 0]),
            t_range=[-4, 4],
            color=GREEN
        )

        self.play(FadeIn(narration_p1), run_time=2)
        self.play(Create(initial_line), run_time=1)
        self.play(Transform(initial_line, grow_line), run_time=1)
        self.play(Transform(initial_line, decay_line), run_time=1)
        self.play(FadeOut(initial_line))

        self.play(
            FadeIn(narration_q1),
            Create(path_curve),
            FadeIn(dot_moving),
            run_time=2
        )
        self.play(MoveAlongPath(dot_moving, path_curve), rate_func=lambda t: t**2, run_time=4)
        self.play(MoveAlongPath(dot_moving, path_curve.reverse_points()), rate_func=lambda t: 1 - (1-t)**2, run_time=4)

        self.play(
            FadeIn(narration_q2), FadeIn(narration_q2_cont),
            run_time=2
        )
        self.wait(1)

        self.play(
            FadeOut(narration_p1), FadeOut(narration_q1),
            FadeOut(narration_q2), FadeOut(narration_q2_cont),
            FadeOut(dot_moving), FadeOut(path_curve),
            run_time=1.5
        )
        self.wait(0.5)

        # --- [0:18] Section: Derivatives - Instantaneous Rate of Change ---
        narration_deriv_p1 = Text(
            "Calculus begins by giving us the tools for this. Imagine zooming in on a curve,",
            **narration_text_config
        ).to_edge(UP)
        narration_deriv_p2 = Text(
            "representing some changing quantity. As you zoom closer, any tiny segment of that curve",
            **narration_text_config
        ).next_to(narration_deriv_p1, DOWN, buff=0.4)
        narration_deriv_p3 = Text(
            "appears to straighten out, revealing a clear slope. This slope, at that single point,",
            **narration_text_config
        ).next_to(narration_deriv_p2, DOWN, buff=0.4)
        narration_deriv_p4 = Text(
            "is what we call a derivative – the instantaneous rate of change.",
            **narration_text_config
        ).next_to(narration_deriv_p3, DOWN, buff=0.2)

        self.play(FadeIn(narration_deriv_p1), run_time=1.5)

        plane = NumberPlane(
            x_range=[-5, 5, 1], y_range=[-3, 3, 1], x_length=10, y_length=6,
            axis_config={"color": GREY_A}, background_line_style={"stroke_opacity": 0.5}
        ).to_edge(DOWN)
        curve_func = lambda x: 0.5 * x**2 - 0.2 * x**3 + 0.5 * np.sin(x)
        # Use plane.plot for graphing on the plane
        curve = plane.plot(
            curve_func,
            x_range=[-4.5, 4.5],
            color=YELLOW,
            stroke_width=4
        )
        dot_on_curve = Dot(plane.coords_to_point(1.5, curve_func(1.5)), color=RED, radius=0.1)

        self.play(Create(plane), Create(curve), FadeIn(dot_on_curve), run_time=2.5)
        self.play(FadeIn(narration_deriv_p2), run_time=2)

        zoom_x = 1.5
        zoom_y = curve_func(zoom_x)
        zoomed_plane = NumberPlane(
            x_range=[zoom_x-0.5, zoom_x+0.5, 0.1], y_range=[zoom_y-0.3, zoom_y+0.3, 0.1],
            x_length=10, y_length=6, axis_config={"color": GREY_A}, background_line_style={"stroke_opacity": 0.5}
        ).to_edge(DOWN)
        zoomed_curve = zoomed_plane.plot(
            curve_func,
            x_range=[zoom_x-0.5, zoom_x+0.5],
            color=YELLOW,
            stroke_width=4
        )
        zoomed_dot = Dot(zoomed_plane.coords_to_point(zoom_x, zoom_y), color=RED, radius=0.1)

        self.play(
            Transform(plane, zoomed_plane), Transform(curve, zoomed_curve), Transform(dot_on_curve, zoomed_dot),
            run_time=3.5
        )
        self.play(FadeIn(narration_deriv_p3), run_time=2.5)

        h = 1e-4
        m = (curve_func(zoom_x + h) - curve_func(zoom_x)) / h
        x1, x2 = zoom_x - 1.5, zoom_x + 1.5
        y1 = zoom_y + m * (x1 - zoom_x)
        y2 = zoom_y + m * (x2 - zoom_x)
        tangent = Line(
            zoomed_plane.coords_to_point(x1, y1),
            zoomed_plane.coords_to_point(x2, y2),
            color=GREEN_A, stroke_width=5
        )
        label = Text("Derivative (Instantaneous Rate of Change)", font_size=28, color=GREEN_A).to_corner(UL).shift(RIGHT*2)

        self.play(Create(tangent), run_time=2)
        self.play(FadeIn(narration_deriv_p4), run_time=2.5)
        self.play(FadeIn(label), run_time=1.5)
        self.wait(2)

        self.play(
            FadeOut(narration_deriv_p1), FadeOut(narration_deriv_p2), FadeOut(narration_deriv_p3),
            FadeOut(narration_deriv_p4), FadeOut(plane), FadeOut(curve), FadeOut(dot_on_curve),
            FadeOut(tangent), FadeOut(label), run_time=1.5
        )
        self.wait(0.5)

        # --- [0:45] Section: Integrals - Total Accumulated Amount ---
        narration_i1 = Text(
            "Now, flip the problem: If we know how something is changing at every moment,",
            **narration_text_config
        ).to_edge(UP)
        narration_i2 = Text(
            "how do we find the total amount accumulated? If we know a car's instantaneous speed,",
            **narration_text_config
        ).next_to(narration_i1, DOWN, buff=0.4)
        narration_i3 = Text(
            "how far did it travel? We can sum up countless tiny 'rate times time' products,",
            **narration_text_config
        ).next_to(narration_i2, DOWN, buff=0.4)
        narration_i4 = Text(
            "the area under the rate curve. This process of summing infinitesimal pieces is the integral.",
            **narration_text_config
        ).next_to(narration_i3, DOWN, buff=0.2)

        self.play(FadeIn(narration_i1), run_time=2)
        integral_plane = NumberPlane(x_range=[0,6,1], y_range=[0,4,1], x_length=8, y_length=5,
                                     axis_config={"color": GREY_A}, background_line_style={"stroke_opacity":0.5}).to_edge(DOWN)
        f_int = lambda x: -0.15*x**2 + 1.2*x + 0.5
        curve_int = integral_plane.plot(f_int, x_range=[0.1,5.8], color=BLUE_A, stroke_width=4)
        self.play(Create(integral_plane), Create(curve_int), run_time=2.5)
        self.play(FadeIn(narration_i2), run_time=2)
        self.play(FadeIn(narration_i3), run_time=2.5)

        rects = integral_plane.get_riemann_rectangles(curve_int, x_range=[0.1,5.8], dx=0.4, color=BLUE, fill_opacity=0.4, stroke_width=0.5)
        self.play(Create(rects), run_time=3)
        self.wait(1)
        self.play(FadeIn(narration_i4), run_time=2.5)

        area = integral_plane.get_area(curve_int, x_range=[0.1,5.8], color=BLUE_B, opacity=0.7)
        label_i = Text("Integral (Total Accumulated Amount)", font_size=28, color=BLUE_B).to_corner(UL).shift(RIGHT*2)
        self.play(Transform(rects, area), FadeIn(label_i), run_time=2.5)
        self.wait(3)
        self.play(
            FadeOut(narration_i1), FadeOut(narration_i2), FadeOut(narration_i3), FadeOut(narration_i4),
            FadeOut(integral_plane), FadeOut(curve_int), FadeOut(rects), FadeOut(label_i), run_time=1.5
        )
        self.wait(0.5)

        # Duality and applications section follows the same pattern using plane.plot or ParametricFunction for visuals.
