from manim import *

class IdealGasScript(Scene):
    def construct(self):
        # [0:00] Imagine a gas: countless molecules, constantly moving, colliding, and subtly pulling on each other. It's wonderfully complex.
        
        # Create gas molecules as small circles
        molecules = VGroup()
        for i in range(30):
            mol = Circle(radius=0.05, color=BLUE, fill_opacity=0.8)
            mol.move_to([
                np.random.uniform(-5, 5),
                np.random.uniform(-2.5, 2.5),
                0
            ])
            molecules.add(mol)
        
        # Add text
        text1 = Text("Imagine a gas: countless molecules, constantly moving,", font_size=32)
        text2 = Text("colliding, and subtly pulling on each other.", font_size=32)
        text3 = Text("It's wonderfully complex.", font_size=32)
        
        text_group1 = VGroup(text1, text2, text3).arrange(DOWN, buff=0.3)
        text_group1.to_edge(UP, buff=0.5)
        
        # Animate molecules with random motion
        self.play(FadeIn(molecules), Write(text_group1))
        
        # Create random motion for molecules
        for _ in range(3):
            animations = []
            for mol in molecules:
                new_pos = [
                    np.random.uniform(-5, 5),
                    np.random.uniform(-2.5, 2.5),
                    0
                ]
                animations.append(mol.animate.move_to(new_pos))
            self.play(*animations, run_time=1)
        
        self.wait(1)
        
        # [0:09] But what if we simplify? What if we pretend these particles are tiny, point-like, with no size and no forces between them, except for perfect, elastic bounces?
        
        self.play(FadeOut(text_group1), FadeOut(molecules))
        
        text4 = Text("But what if we simplify? What if we pretend these particles", font_size=32)
        text5 = Text("are tiny, point-like, with no size and no forces between them,", font_size=32)
        text6 = Text("except for perfect, elastic bounces?", font_size=32)
        
        text_group2 = VGroup(text4, text5, text6).arrange(DOWN, buff=0.3)
        text_group2.to_edge(UP, buff=0.5)
        
        # Create simplified point particles
        points = VGroup()
        for i in range(20):
            point = Dot(radius=0.03, color=RED)
            point.move_to([
                np.random.uniform(-4, 4),
                np.random.uniform(-2, 2),
                0
            ])
            points.add(point)
        
        # Create a container box
        container = Rectangle(width=8, height=4, color=WHITE, stroke_width=3)
        
        self.play(Write(text_group2), Create(container), FadeIn(points))
        
        # Show elastic bouncing motion
        for _ in range(4):
            animations = []
            for point in points:
                new_pos = [
                    np.random.uniform(-3.8, 3.8),
                    np.random.uniform(-1.8, 1.8),
                    0
                ]
                animations.append(point.animate.move_to(new_pos))
            self.play(*animations, run_time=0.8)
        
        self.wait(2)
        
        # [0:20] This idealized thought experiment gives us the "ideal gas." While not perfectly real, this stripped-down model allows us to elegantly derive relationships between pressure, volume, and temperature, revealing the fundamental mechanics that underpin all gases.
        
        self.play(FadeOut(text_group2), FadeOut(container), FadeOut(points))
        
        text7 = Text('This idealized thought experiment gives us the "ideal gas."', font_size=32)
        text8 = Text("While not perfectly real, this stripped-down model allows us", font_size=32)
        text9 = Text("to elegantly derive relationships between pressure, volume,", font_size=32)
        text10 = Text("and temperature, revealing the fundamental mechanics", font_size=32)
        text11 = Text("that underpin all gases.", font_size=32)
        
        text_group3 = VGroup(text7, text8, text9, text10, text11).arrange(DOWN, buff=0.3)
        text_group3.move_to(ORIGIN)
        
        # Show ideal gas law equation
        equation = MathTex("PV = nRT", font_size=60, color=YELLOW)
        equation.to_edge(DOWN, buff=1)
        
        self.play(Write(text_group3))
        self.wait(1)
        self.play(Write(equation))
        self.wait(3)
        
        # Clear everything at the end
        self.play(FadeOut(text_group3), FadeOut(equation))