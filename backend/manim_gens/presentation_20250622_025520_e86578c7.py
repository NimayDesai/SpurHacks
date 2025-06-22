from manim import *

class NeuralNetworkGradientDescent(Scene):
    def construct(self):
        # [0:00] A neural network initially makes random guesses. The goal is to systematically adjust its internal parameters to improve accuracy.
        text1 = Text("A neural network initially makes random guesses.", font_size=36)
        text2 = Text("The goal is to systematically adjust its internal", font_size=36)
        text3 = Text("parameters to improve accuracy.", font_size=36)
        
        # Simple neural network visualization
        neurons_input = VGroup(*[Circle(radius=0.3, color=BLUE) for _ in range(3)])
        neurons_hidden = VGroup(*[Circle(radius=0.3, color=GREEN) for _ in range(4)])
        neurons_output = VGroup(*[Circle(radius=0.3, color=RED) for _ in range(2)])
        
        neurons_input.arrange(DOWN, buff=0.5).shift(LEFT * 3)
        neurons_hidden.arrange(DOWN, buff=0.3).shift(LEFT * 0.5)
        neurons_output.arrange(DOWN, buff=0.5).shift(RIGHT * 2)
        
        # Connections
        connections = VGroup()
        for input_neuron in neurons_input:
            for hidden_neuron in neurons_hidden:
                connections.add(Line(input_neuron.get_center(), hidden_neuron.get_center(), stroke_width=1, color=GRAY))
        
        for hidden_neuron in neurons_hidden:
            for output_neuron in neurons_output:
                connections.add(Line(hidden_neuron.get_center(), output_neuron.get_center(), stroke_width=1, color=GRAY))
        
        network = VGroup(neurons_input, neurons_hidden, neurons_output, connections)
        network.scale(0.6).shift(DOWN * 1.5)
        
        text_group1 = VGroup(text1, text2, text3).arrange(DOWN, buff=0.3).shift(UP * 2)
        
        self.play(Write(text_group1))
        self.play(FadeIn(network))
        self.wait(7)
        
        # [0:07] We quantify how wrong it is with a "cost function"—a single number reflecting its error.
        self.play(FadeOut(text_group1), FadeOut(network))
        
        text4 = Text('We quantify how wrong it is with a "cost function"—', font_size=36)
        text5 = Text("a single number reflecting its error.", font_size=36)
        text_group2 = VGroup(text4, text5).arrange(DOWN, buff=0.3).shift(UP * 1)
        
        # Cost function visualization
        cost_label = Text("Cost Function", font_size=32, color=YELLOW)
        cost_value = Text("C = 0.847", font_size=48, color=RED)
        cost_group = VGroup(cost_label, cost_value).arrange(DOWN, buff=0.5).shift(DOWN * 1)
        
        self.play(Write(text_group2))
        self.play(FadeIn(cost_group))
        self.wait(6)
        
        # [0:13] Imagine this cost as a landscape. Learning is like trying to find the lowest point.
        self.play(FadeOut(text_group2), FadeOut(cost_group))
        
        text6 = Text("Imagine this cost as a landscape.", font_size=36)
        text7 = Text("Learning is like trying to find the lowest point.", font_size=36)
        text_group3 = VGroup(text6, text7).arrange(DOWN, buff=0.3).shift(UP * 2.5)
        
        # 3D landscape visualization
        axes = ThreeDAxes(
            x_range=[-3, 3, 1],
            y_range=[-3, 3, 1],
            z_range=[0, 4, 1],
            x_length=6,
            y_length=6,
            z_length=3
        )
        
        def cost_landscape(x, y):
            return 2 * np.exp(-(x**2 + y**2)/2) + 0.5 * (x**2 + y**2)/4
        
        surface = Surface(
            lambda u, v: axes.c2p(u, v, cost_landscape(u, v)),
            u_range=[-2.5, 2.5],
            v_range=[-2.5, 2.5],
            resolution=(20, 20),
            color=BLUE,
            fill_opacity=0.7
        )
        
        # Point on landscape
        point = Dot3D(axes.c2p(1, 1, cost_landscape(1, 1)), color=RED, radius=0.1)
        
        landscape_group = VGroup(axes, surface, point).scale(0.6).shift(DOWN * 0.5)
        
        self.play(Write(text_group3))
        self.play(FadeIn(landscape_group))
        self.wait(7)
        
        # [0:20] The crucial insight is to calculate the *gradient* of this cost. This tells us the direction of steepest ascent for each parameter.
        self.play(FadeOut(text_group3), FadeOut(landscape_group))
        
        text8 = Text("The crucial insight is to calculate the *gradient* of this cost.", font_size=32)
        text9 = Text("This tells us the direction of steepest ascent", font_size=32)
        text10 = Text("for each parameter.", font_size=32)
        text_group4 = VGroup(text8, text9, text10).arrange(DOWN, buff=0.3).shift(UP * 1.5)
        
        # Gradient visualization
        plane = NumberPlane(
            x_range=[-3, 3, 1],
            y_range=[-3, 3, 1],
            background_line_style={"stroke_opacity": 0.3}
        ).scale(0.8)
        
        # Contour lines
        contours = VGroup()
        for level in [0.5, 1.0, 1.5, 2.0]:
            contour = ParametricFunction(
                lambda t: plane.c2p(level * np.cos(t), level * np.sin(t)),
                t_range=[0, 2*PI],
                color=GRAY,
                stroke_width=2
            )
            contours.add(contour)
        
        # Gradient vector
        start_point = plane.c2p(1, 0.5)
        gradient_vector = Arrow(
            start=start_point,
            end=start_point + np.array([1, 0.5, 0]),
            color=RED,
            stroke_width=6,
            tip_length=0.3
        )
        
        gradient_label = Text("∇C", font_size=36, color=RED).next_to(gradient_vector, UP)
        
        gradient_group = VGroup(plane, contours, gradient_vector, gradient_label).shift(DOWN * 1)
        
        self.play(Write(text_group4))
        self.play(FadeIn(gradient_group))
        self.wait(8)
        
        # [0:28] By nudging each parameter slightly *opposite* to its gradient, the network iteratively descends this error landscape, converging towards better predictions.
        self.play(FadeOut(text_group4), FadeOut(gradient_group))
        
        text11 = Text("By nudging each parameter slightly *opposite* to its gradient,", font_size=30)
        text12 = Text("the network iteratively descends this error landscape,", font_size=30)
        text13 = Text("converging towards better predictions.", font_size=30)
        text_group5 = VGroup(text11, text12, text13).arrange(DOWN, buff=0.3).shift(UP * 2)
        
        # Descent visualization
        plane2 = NumberPlane(
            x_range=[-3, 3, 1],
            y_range=[-3, 3, 1],
            background_line_style={"stroke_opacity": 0.3}
        ).scale(0.8)
        
        # Path of descent
        path_points = [
            plane2.c2p(2, 1.5),
            plane2.c2p(1.5, 1),
            plane2.c2p(1, 0.5),
            plane2.c2p(0.5, 0.25),
            plane2.c2p(0, 0)
        ]
        
        path = VMobject()
        path.set_points_as_corners(path_points)
        path.set_color(GREEN)
        path.set_stroke_width(4)
        
        # Moving dot
        moving_dot = Dot(path_points[0], color=YELLOW, radius=0.1)
        
        # Opposite gradient arrows
        opposite_arrows = VGroup()
        for i in range(len(path_points)-1):
            arrow = Arrow(
                start=path_points[i],
                end=path_points[i+1],
                color=BLUE,
                stroke_width=4,
                tip_length=0.2
            )
            opposite_arrows.add(arrow)
        
        descent_group = VGroup(plane2, path, moving_dot, opposite_arrows).shift(DOWN * 1)
        
        self.play(Write(text_group5))
        self.play(FadeIn(descent_group))
        
        # Animate the descent
        self.play(
            MoveAlongPath(moving_dot, path),
            run_time=3
        )
        
        self.wait(2)
        
        # Clear everything at the end
        self.play(FadeOut(text_group5), FadeOut(descent_group))