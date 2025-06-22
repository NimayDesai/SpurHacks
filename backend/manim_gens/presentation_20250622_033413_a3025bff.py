# Manim configuration for LaTeX
import os
import sys

# Add MiKTeX to PATH (adjust path as needed for your system)
if sys.platform.startswith('win'):
    os.environ['PATH'] += r';C:\Program Files\MiKTeX\miktex\bin\x64'
elif sys.platform.startswith('darwin'):  # macOS
    os.environ['PATH'] += ':/usr/local/bin:/opt/homebrew/bin'
    
from manim import *

# Configure LaTeX template
config.tex_template = TexTemplate()
config.tex_template.add_to_preamble(r"\usepackage{amsmath}")
config.tex_template.add_to_preamble(r"\usepackage{amssymb}")
config.tex_template.add_to_preamble(r"\usepackage{mathtools}")
config.tex_template.add_to_preamble(r"\usepackage{physics}")

from manim import *

class LakeIntegrationScene(Scene):
    def construct(self):
        # [0:00] - Opening text
        opening_text = Text("Imagine trying to find the area of a weirdly shaped lake.", font_size=36)
        self.play(Write(opening_text))
        self.wait(5)
        
        # [0:05] - Clear and show lake shape with next text
        self.play(FadeOut(opening_text))
        
        # Create a weird lake shape
        lake_vertices = [
            [-3, 1, 0], [-2, 2, 0], [0, 1.5, 0], [2, 2.5, 0], [3, 1, 0],
            [2.5, 0, 0], [1, -1, 0], [0, -0.5, 0], [-1, -1.5, 0], [-2.5, -0.5, 0]
        ]
        lake = Polygon(*lake_vertices, color=BLUE, fill_opacity=0.7)
        
        text_simple = Text("We can't just use a simple formula.", font_size=36)
        text_simple.to_edge(UP)
        
        self.play(Create(lake), Write(text_simple))
        self.wait(5)
        
        # [0:10] - Clear and show squares concept
        self.play(FadeOut(text_simple))
        
        text_squares = Text("But what if we covered it in tiny squares?", font_size=36)
        text_squares.to_edge(UP)
        
        # Create large squares covering the lake
        squares = VGroup()
        for i in range(-3, 4):
            for j in range(-2, 3):
                square = Square(side_length=0.8, stroke_width=2, color=YELLOW, fill_opacity=0.3)
                square.move_to([i*0.8, j*0.8, 0])
                squares.add(square)
        
        self.play(Write(text_squares))
        self.wait(5)
        
        # [0:15] - Show the squares
        self.play(FadeOut(text_squares))
        
        text_area = Text("The total area of those squares is approximately the lake's area.", font_size=32)
        text_area.to_edge(UP)
        
        self.play(Write(text_area), Create(squares))
        self.wait(5)
        
        # [0:20] - Show smaller squares
        self.play(FadeOut(text_area))
        
        text_smaller = Text("The smaller the squares, the better the approximation.", font_size=36)
        text_smaller.to_edge(UP)
        
        # Create smaller squares
        small_squares = VGroup()
        for i in range(-6, 7):
            for j in range(-4, 5):
                square = Square(side_length=0.4, stroke_width=1, color=YELLOW, fill_opacity=0.3)
                square.move_to([i*0.4, j*0.4, 0])
                small_squares.add(square)
        
        self.play(Write(text_smaller), Transform(squares, small_squares))
        self.wait(5)
        
        # [0:25] - Clear and show integration concept
        self.play(FadeOut(text_smaller), FadeOut(squares), FadeOut(lake))
        
        text_integration = Text("This leads to the core idea of integration:", font_size=36)
        text_integration.to_edge(UP)
        
        text_summing = Text("summing infinitely many infinitesimally small areas.", font_size=32)
        text_summing.next_to(text_integration, DOWN, buff=0.5)
        
        # Show integral symbol and mathematical representation
        integral_symbol = MathTex(r"\int", font_size=72, color=GREEN)
        integral_symbol.move_to(ORIGIN)
        
        self.play(Write(text_integration))
        self.wait(2)
        self.play(Write(text_summing), Create(integral_symbol))
        self.wait(8)
        
        # [0:35] - Final text
        self.play(FadeOut(text_integration), FadeOut(text_summing), FadeOut(integral_symbol))
        
        final_text = Text("It's a powerful way to precisely calculate areas—and volumes—", font_size=32)
        final_text2 = Text("that are far too complex for simple geometry.", font_size=32)
        final_text2.next_to(final_text, DOWN, buff=0.3)
        
        final_group = VGroup(final_text, final_text2)
        final_group.move_to(ORIGIN)
        
        self.play(Write(final_text))
        self.play(Write(final_text2))
        self.wait(3)
        
        self.play(FadeOut(final_group))
