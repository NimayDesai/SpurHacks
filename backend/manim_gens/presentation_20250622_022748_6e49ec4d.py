from manim import *

class PhotosynthesisScene(Scene):
    def construct(self):
        # [0:00] Plants seem to conjure food from thin air and sunlight. But how?
        text_00 = Text("Plants seem to conjure food from thin air and sunlight. But how?", 
                      font_size=36).scale_to_fit_width(config.frame_width * 0.9)
        self.play(Write(text_00))
        self.wait(5)
        
        # [0:05] It's an elegant energy dance within their cells.
        self.play(FadeOut(text_00))
        text_05 = Text("It's an elegant energy dance within their cells.", 
                      font_size=36).scale_to_fit_width(config.frame_width * 0.9)
        self.play(Write(text_05))
        self.wait(5)
        
        # [0:10] Tiny internal machinery captures photons – little packets of light energy.
        self.play(FadeOut(text_05))
        text_10 = Text("Tiny internal machinery captures photons – little packets of light energy.", 
                      font_size=36).scale_to_fit_width(config.frame_width * 0.9)
        
        # Visual: Show photons as small circles with light rays
        photons = VGroup()
        for i in range(8):
            photon = Circle(radius=0.1, color=YELLOW, fill_opacity=0.8)
            photon.move_to([np.random.uniform(-3, 3), np.random.uniform(-2, 2), 0])
            photons.add(photon)
        
        light_rays = VGroup()
        for i in range(6):
            ray = Line(start=[np.random.uniform(-4, 4), 3, 0], 
                      end=[np.random.uniform(-4, 4), -3, 0], 
                      color=YELLOW, stroke_width=2)
            light_rays.add(ray)
        
        self.play(Write(text_10))
        self.play(Create(light_rays), Create(photons))
        self.wait(8)
        
        # [0:18] This energy then powers a chemical construction site.
        self.play(FadeOut(text_10), FadeOut(light_rays), FadeOut(photons))
        text_18 = Text("This energy then powers a chemical construction site.", 
                      font_size=36).scale_to_fit_width(config.frame_width * 0.9)
        
        # Visual: Show construction site with geometric shapes
        construction_base = Rectangle(width=4, height=2, color=BLUE, fill_opacity=0.3)
        construction_elements = VGroup()
        for i in range(5):
            element = Square(side_length=0.3, color=GREEN, fill_opacity=0.6)
            element.move_to([np.random.uniform(-1.5, 1.5), np.random.uniform(-0.8, 0.8), 0])
            construction_elements.add(element)
        
        self.play(Write(text_18))
        self.play(Create(construction_base), Create(construction_elements))
        self.wait(6)
        
        # [0:24] Water molecules are split, and carbon dioxide atoms are meticulously rearranged, building new sugar molecules.
        self.play(FadeOut(text_18), FadeOut(construction_base), FadeOut(construction_elements))
        text_24 = Text("Water molecules are split, and carbon dioxide atoms are\nmeticulously rearranged, building new sugar molecules.", 
                      font_size=32).scale_to_fit_width(config.frame_width * 0.9)
        
        # Visual: Show molecular representations
        # Water molecules (H2O)
        water_molecules = VGroup()
        for i in range(3):
            h2o = VGroup()
            o_atom = Circle(radius=0.2, color=RED, fill_opacity=0.8)
            h_atom1 = Circle(radius=0.1, color=WHITE, fill_opacity=0.8).next_to(o_atom, LEFT, buff=0.1)
            h_atom2 = Circle(radius=0.1, color=WHITE, fill_opacity=0.8).next_to(o_atom, RIGHT, buff=0.1)
            h2o.add(o_atom, h_atom1, h_atom2)
            h2o.move_to([-3 + i * 1.5, 1, 0])
            water_molecules.add(h2o)
        
        # CO2 molecules
        co2_molecules = VGroup()
        for i in range(3):
            co2 = VGroup()
            c_atom = Circle(radius=0.2, color=GRAY, fill_opacity=0.8)
            o_atom1 = Circle(radius=0.15, color=RED, fill_opacity=0.8).next_to(c_atom, LEFT, buff=0.1)
            o_atom2 = Circle(radius=0.15, color=RED, fill_opacity=0.8).next_to(c_atom, RIGHT, buff=0.1)
            co2.add(c_atom, o_atom1, o_atom2)
            co2.move_to([-3 + i * 1.5, -1, 0])
            co2_molecules.add(co2)
        
        # Sugar molecule (simplified representation)
        sugar_molecule = VGroup()
        for i in range(6):
            atom = Circle(radius=0.15, color=GREEN, fill_opacity=0.8)
            angle = i * PI / 3
            atom.move_to([0.8 * np.cos(angle) + 2, 0.8 * np.sin(angle), 0])
            sugar_molecule.add(atom)
        
        self.play(Write(text_24))
        self.play(Create(water_molecules), Create(co2_molecules))
        self.wait(3)
        self.play(Create(sugar_molecule))
        self.wait(7)
        
        # [0:34] Essentially, light energy transforms simple ingredients into the complex fuel for life.
        self.play(FadeOut(text_24), FadeOut(water_molecules), FadeOut(co2_molecules), FadeOut(sugar_molecule))
        text_34 = Text("Essentially, light energy transforms simple ingredients\ninto the complex fuel for life.", 
                      font_size=36).scale_to_fit_width(config.frame_width * 0.9)
        
        # Visual: Show transformation process
        light_energy = Text("Light Energy", color=YELLOW).move_to([-3, 2, 0])
        simple_ingredients = Text("Simple Ingredients", color=BLUE).move_to([-3, 0, 0])
        arrow = Arrow(start=[-1, 1, 0], end=[1, 1, 0], color=WHITE)
        complex_fuel = Text("Complex Fuel", color=GREEN).move_to([3, 1, 0])
        
        self.play(Write(text_34))
        self.play(Write(light_energy), Write(simple_ingredients))
        self.play(Create(arrow))
        self.play(Write(complex_fuel))
        self.wait(3)
        
        # Final fadeout
        self.play(FadeOut(text_34), FadeOut(light_energy), FadeOut(simple_ingredients), 
                 FadeOut(arrow), FadeOut(complex_fuel))