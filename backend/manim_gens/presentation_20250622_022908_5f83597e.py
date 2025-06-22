from manim import *

class PlantEnergyScene(Scene):
    def construct(self):
        # [0:00] How do plants capture energy from the sun?
        title_text = Text("How do plants capture energy from the sun?", font_size=48)
        self.play(Write(title_text))
        self.wait(4)
        
        # [0:04] It's not just absorbing warmth; it's an intricate process of *conversion*.
        self.play(FadeOut(title_text))
        conversion_text = Text("It's not just absorbing warmth; it's an intricate\nprocess of conversion.", font_size=36)
        conversion_word = Text("conversion", font_size=36, color=YELLOW).move_to(conversion_text.get_center() + DOWN * 0.3)
        conversion_group = VGroup(conversion_text, conversion_word)
        self.play(Write(conversion_text))
        self.play(Transform(conversion_text[-10:], conversion_word))
        self.wait(1)
        
        # [0:09] Light energy arrives, empowering the plant to take simple carbon dioxide and water molecules.
        self.play(FadeOut(conversion_text))
        light_text = Text("Light energy arrives, empowering the plant to take\nsimple carbon dioxide and water molecules.", font_size=36)
        
        # Visual elements for light, CO2, and H2O
        sun = Circle(radius=0.5, color=YELLOW, fill_opacity=0.8).shift(UP * 2 + LEFT * 4)
        light_rays = VGroup(*[Line(sun.get_center(), sun.get_center() + 2 * np.array([np.cos(angle), np.sin(angle), 0]), color=YELLOW) 
                             for angle in np.linspace(0, 2*np.pi, 8)])
        
        co2_molecule = VGroup(
            Circle(radius=0.2, color=GRAY, fill_opacity=0.8),
            Circle(radius=0.15, color=RED, fill_opacity=0.8).shift(LEFT * 0.4),
            Circle(radius=0.15, color=RED, fill_opacity=0.8).shift(RIGHT * 0.4)
        ).shift(DOWN * 1 + LEFT * 2)
        
        h2o_molecule = VGroup(
            Circle(radius=0.2, color=RED, fill_opacity=0.8),
            Circle(radius=0.1, color=WHITE, fill_opacity=0.8).shift(UP * 0.3 + LEFT * 0.2),
            Circle(radius=0.1, color=WHITE, fill_opacity=0.8).shift(UP * 0.3 + RIGHT * 0.2)
        ).shift(DOWN * 1 + RIGHT * 2)
        
        self.play(Write(light_text))
        self.play(FadeIn(sun), FadeIn(light_rays), FadeIn(co2_molecule), FadeIn(h2o_molecule))
        self.wait(2)
        
        # [0:15] This energy then gets elegantly woven into the chemical bonds of glucose, a sugar molecule.
        self.play(FadeOut(light_text), FadeOut(sun), FadeOut(light_rays), FadeOut(co2_molecule), FadeOut(h2o_molecule))
        glucose_text = Text("This energy then gets elegantly woven into the\nchemical bonds of glucose, a sugar molecule.", font_size=36)
        
        # Glucose molecule representation
        glucose_molecule = VGroup(
            *[Circle(radius=0.15, color=BLUE, fill_opacity=0.8).shift(0.8 * np.array([np.cos(i * np.pi/3), np.sin(i * np.pi/3), 0])) 
              for i in range(6)]
        )
        bonds = VGroup(
            *[Line(glucose_molecule[i].get_center(), glucose_molecule[(i+1)%6].get_center(), color=WHITE) 
              for i in range(6)]
        )
        glucose_group = VGroup(glucose_molecule, bonds)
        
        self.play(Write(glucose_text))
        self.play(FadeIn(glucose_group))
        self.wait(2)
        
        # [0:21] In essence, light becomes stored chemical potential.
        self.play(FadeOut(glucose_text), FadeOut(glucose_group))
        potential_text = Text("In essence, light becomes stored chemical potential.", font_size=36)
        
        # Energy transformation visual
        light_energy = Text("Light Energy", color=YELLOW).shift(LEFT * 3)
        arrow = Arrow(LEFT * 1.5, RIGHT * 1.5, color=WHITE)
        chemical_energy = Text("Chemical Potential", color=GREEN).shift(RIGHT * 3)
        
        self.play(Write(potential_text))
        self.play(FadeIn(light_energy), FadeIn(arrow), FadeIn(chemical_energy))
        self.wait(1)
        
        # [0:25] Oxygen is simply what's left over.
        self.play(FadeOut(potential_text), FadeOut(light_energy), FadeOut(arrow), FadeOut(chemical_energy))
        oxygen_text = Text("Oxygen is simply what's left over.", font_size=36)
        
        # Oxygen molecule
        o2_molecule = VGroup(
            Circle(radius=0.2, color=RED, fill_opacity=0.8).shift(LEFT * 0.3),
            Circle(radius=0.2, color=RED, fill_opacity=0.8).shift(RIGHT * 0.3),
            Line(LEFT * 0.1, RIGHT * 0.1, color=WHITE)
        )
        
        self.play(Write(oxygen_text))
        self.play(FadeIn(o2_molecule))
        self.wait(2)
        
        # Final cleanup
        self.play(FadeOut(oxygen_text), FadeOut(o2_molecule))