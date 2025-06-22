from manim import *

class GravityScript(Scene):
    def construct(self):
        # [0:00] Gravity. It's the unseen force that anchors us to the Earth and binds planets to stars.
        gravity_text = Text("Gravity. It's the unseen force that anchors us to the Earth and binds planets to stars.", 
                           font_size=36).scale_to_fit_width(config.frame_width - 1)
        self.play(Write(gravity_text))
        self.wait(9)
        
        # [0:09] But how does it operate?
        self.play(FadeOut(gravity_text))
        operate_text = Text("But how does it operate?", font_size=48)
        self.play(Write(operate_text))
        self.wait(3)
        
        # [0:12] Every object possessing mass exerts an attractive pull on every other mass.
        self.play(FadeOut(operate_text))
        mass_text = Text("Every object possessing mass exerts an attractive pull on every other mass.", 
                        font_size=36).scale_to_fit_width(config.frame_width - 1)
        self.play(Write(mass_text))
        self.wait(8)
        
        # [0:20] This pull strengthens with more mass, and as objects draw closer.
        self.play(FadeOut(mass_text))
        strengthen_text = Text("This pull strengthens with more mass, and as objects draw closer.", 
                             font_size=40).scale_to_fit_width(config.frame_width - 1)
        self.play(Write(strengthen_text))
        self.wait(8)
        
        # [0:28] This fundamental interaction, simple yet profound, dictates everything from an apple's fall to the colossal dance of galaxies.
        self.play(FadeOut(strengthen_text))
        fundamental_text = Text("This fundamental interaction, simple yet profound, dictates everything from an apple's fall to the colossal dance of galaxies.", 
                               font_size=32).scale_to_fit_width(config.frame_width - 1)
        self.play(Write(fundamental_text))
        self.wait(11)
        
        # [0:39] End - clear everything
        self.play(FadeOut(fundamental_text))