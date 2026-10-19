# 3b1b-style explainer: How to optimize on-device slot filling on a phone.
# Render with:  manim -pql 4_video_explainer.py MobileSlotFillingOptimization
from manim import *


class MobileSlotFillingOptimization(Scene):
    def construct(self):
        # Scene 1: title
        title = Text("Make on-device slot filling fast", font_size=40)
        subtitle = Text("small model · cached prompt · short output", font_size=24, color=GREY_B)
        subtitle.next_to(title, DOWN, buff=0.4)
        self.play(Write(title))
        self.play(FadeIn(subtitle, shift=UP * 0.2))
        self.wait(1.5)
        self.play(FadeOut(title), FadeOut(subtitle))

        # Scene 2: three costs of one turn
        costs = VGroup(
            Text("1. Read the prompt (prefill)", font_size=30),
            Text("2. Write the output (decode)", font_size=30),
            Text("3. Load the model (startup)", font_size=30),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.7)
        self.play(LaggedStart(*[FadeIn(c, shift=RIGHT * 0.3) for c in costs], lag_ratio=0.4))
        self.wait(1)
        self.play(FadeOut(costs))

        # Scene 3: fixed prefix is cached, only new tokens are read
        prefix = RoundedRectangle(width=5, height=1, corner_radius=0.1, color=BLUE, fill_opacity=0.5)
        prefix_lbl = Text("fixed prefix", font_size=26).move_to(prefix)
        user = RoundedRectangle(width=2.6, height=1, corner_radius=0.1, color=GREEN, fill_opacity=0.5)
        user.next_to(prefix, RIGHT, buff=0.2)
        user_lbl = Text("user words", font_size=26).move_to(user)
        row = VGroup(prefix, prefix_lbl, user, user_lbl).move_to(ORIGIN)
        self.play(Create(prefix), Write(prefix_lbl), Create(user), Write(user_lbl))
        self.wait(0.5)

        cache_tag = Text("cache_prompt: reuse", font_size=26, color=YELLOW).next_to(prefix, DOWN, buff=0.5)
        self.play(prefix.animate.set_fill(GREY, opacity=0.6), Write(cache_tag))
        self.play(user.animate.set_fill(GREEN, opacity=0.9))
        self.wait(1.5)
        self.play(FadeOut(row), FadeOut(cache_tag))

        # Scene 4: output is capped and stops at the closing brace
        json_text = Text('{"from":"北京","to":"上海","date":"2026-10-20","seat":null}', font_size=28)
        cap = Line(LEFT * 3.2, RIGHT * 3.2, color=RED).next_to(json_text, DOWN, buff=0.3)
        cap_lbl = Text("n_predict = 64, temperature = 0", font_size=24, color=RED).next_to(cap, DOWN, buff=0.2)
        self.play(Write(json_text))
        self.play(Create(cap), Write(cap_lbl))
        self.wait(1.5)
        self.play(FadeOut(json_text), FadeOut(cap), FadeOut(cap_lbl))

        # Scene 5: the lever stack
        levers = VGroup(
            Text("Smaller model: 0.5B–1.5B, Q4_K_M", font_size=28),
            Text("Short prompt, fixed prefix first", font_size=28),
            Text("Small context: 512–1024", font_size=28),
            Text("Server started once, kept warm", font_size=28),
            Text("Threads matched to fast cores", font_size=28),
            Text("Dates and numbers handled by code", font_size=28),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.35)
        self.play(LaggedStart(*[FadeIn(l, shift=RIGHT * 0.2) for l in levers], lag_ratio=0.25))
        self.wait(1.5)
        self.play(FadeOut(levers))

        # Scene 6: measure, change one thing, check accuracy
        loop = VGroup(
            Text("Measure", font_size=32),
            Text("Change ONE lever", font_size=32),
            Text("Check accuracy", font_size=32),
        ).arrange(RIGHT, buff=1.2)
        arrows = VGroup(
            Arrow(loop[0].get_right(), loop[1].get_left(), buff=0.2),
            Arrow(loop[1].get_right(), loop[2].get_left(), buff=0.2),
        )
        back = CurvedArrow(loop[2].get_bottom() + DOWN * 0.3, loop[0].get_bottom() + DOWN * 0.3, angle=-TAU / 4)
        self.play(Write(loop), Create(arrows))
        self.play(Create(back))
        self.wait(1)
        self.play(FadeOut(loop), FadeOut(arrows), FadeOut(back))

        # Ending
        end = Text("Measure. Change one thing. Keep what passes.", font_size=32, color=YELLOW)
        self.play(Write(end))
        self.wait(2)
