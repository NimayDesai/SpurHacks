from manim import *

# Use a modern, dark theme
config.background_color = DARKER_GRAY
# You can change this to MEDIUM_QUALITY or HIGH_QUALITY for the final render
# config.quality = "medium_quality" 

class QuadraticIntro(Scene):
    def construct(self):
        # --- SCENE 1: The Title and Equation (Approx. 4 seconds) ---
        title = Title("Quadratics").set_color(YELLOW)
        equation = MathTex("f(x) = ax^2 + bx + c", font_size=60).next_to(title, DOWN, buff=0.8)

        self.play(Write(title))
        self.play(FadeIn(equation, shift=UP))
        self.wait(1.5)

        # --- SCENE 2: The Parabola and its Parameters (Approx. 8 seconds) ---
        self.play(FadeOut(title), FadeOut(equation))

        # Create axes
        axes = Axes(
            x_range=[-4, 4, 1],
            y_range=[-4, 8, 1],
            axis_config={"color": BLUE},
            x_length=7,
            y_length=6
        ).add_coordinates()
        
        # ValueTrackers for dynamic parameters a and c
        a_val = ValueTracker(1)
        c_val = ValueTracker(0)

        # The parabola that updates based on the trackers
        graph = always_redraw(
            lambda: axes.plot(
                lambda x: a_val.get_value() * x**2 + c_val.get_value(),
                color=YELLOW,
                x_range=[-4, 4]
            )
        )

        # The equation text that updates
        graph_eq = always_redraw(
            lambda: MathTex(
                f"f(x) = {a_val.get_value():.1f}x^2 + {c_val.get_value():.1f}",
                font_size=48
            ).next_to(axes, UP)
        )
        
        self.play(Create(axes), run_time=1)
        self.play(Create(graph), FadeIn(graph_eq))
        self.wait(0.5)

        # Animate changing 'a' (stretch and flip)
        self.play(a_val.animate.set_value(2), run_time=1.5)
        self.play(a_val.animate.set_value(-1), run_time=1.5)
        
        # Animate changing 'c' (vertical shift)
        self.play(c_val.animate.set_value(3), run_time=1.5)
        self.play(c_val.animate.set_value(-2), run_time=1.5)
        self.wait(0.5)

        # --- SCENE 3: Finding the Roots (Approx. 7 seconds) ---
        self.play(FadeOut(graph), FadeOut(graph_eq), FadeOut(axes))

        # New axes and a parabola with clear roots
        axes_roots = Axes(x_range=[-5, 5, 1], y_range=[-5, 5, 1], axis_config={"color": BLUE}).add_coordinates()
        parabola_roots = axes_roots.plot(lambda x: x**2 - 4, color=YELLOW, x_range=[-3, 3])
        
        # Highlight the roots
        root1 = Dot(axes_roots.c2p(-2, 0), color=RED)
        root2 = Dot(axes_roots.c2p(2, 0), color=RED)
        roots_label = Text("The Roots (Solutions)", font_size=36).to_edge(UP)

        self.play(Create(axes_roots), Create(parabola_roots))
        self.play(Write(roots_label))
        self.play(LaggedStart(FadeIn(root1, scale=2), FadeIn(root2, scale=2), lag_ratio=0.5))
        self.wait(2)

        # --- SCENE 4: Real-World Application (Approx. 8 seconds) ---
        self.play(
            FadeOut(axes_roots),
            FadeOut(parabola_roots),
            FadeOut(root1),
            FadeOut(root2),
            FadeOut(roots_label),
        )
        
        ground = Line(LEFT * 7, RIGHT * 7, color=GRAY).to_edge(DOWN)
        
        # A parabolic path for the projectile
        projectile_path = lambda x: -0.5 * (x-1)**2 + 4.5
        path_graph = axes.plot(projectile_path, x_range=[-2, 4], color=ORANGE)
        
        ball = Dot(color=RED)
        ball.move_to(path_graph.get_start())

        path_trace = TracedPath(ball.get_center, stroke_width=6, stroke_color=ORANGE)
        
        app_label = Text("Describes projectile motion", font_size=36).to_edge(UP)
        
        self.play(Create(ground), Write(app_label))
        self.add(path_trace)
        self.play(MoveAlongPath(ball, path_graph), run_time=4)
        self.wait(1.5)

        # --- SCENE 5: Outro (Approx. 3 seconds) ---
        self.play(
            FadeOut(ground),
            FadeOut(app_label),
            FadeOut(path_trace),
            FadeOut(ball),
        )
        
        final_title = Text("Quadratics", font_size=96, color=YELLOW)
        self.play(Write(final_title))
        self.wait(2)