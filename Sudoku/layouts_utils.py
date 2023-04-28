import PySimpleGUI as sg
import os
from scores import *

color_red = "#FF3300"
color_green = "#00b300"

font_loading = ("Ani", 12, "bold")
font_main_window = ("Purisa", 12, "bold")
font_login_scores = ("FreeMono", 12, "bold")


def health_bar(name, max, colors):
    return sg.ProgressBar(
        max,
        orientation="h",
        key=f"-HEALTH-{name}-",
        bar_color=colors,
        expand_y=True,
        visible=False,
        size=(21),
    )


def generate_button(i, j, text=" "):
    return sg.B(
        text,
        size=(4, 2),
        key=(i, j),
        pad=(0, 0),
        border_width=2,
        font=("Helvetica", 10, "bold"),
        auto_size_button=False,
    )


def generate_options(options):
    buttons = []
    for i in range(len(options)):
        buttons.append(
            sg.B(
                " ",
                key=options[i],
                image_source=f"{os.path.dirname(__file__)}/files/images/{options[i]}.png",
            )
        )
    return buttons


def generate_frame_with_buttons(options):
    return [[sg.Frame(" ----- ", [generate_options(options)], title_location="s")]]


def frame_layout_stars(number=5):
    frame = []
    for i in range(number):
        frame.append(
            sg.Image(
                f"{os.path.dirname(__file__)}/files/images/star.png",
                key=f"star{i+1}",
                visible=False,
            )
        )
    return frame


def frame_layout_stars_radio(radios=5):
    frame = []
    for i in range(radios):
        frame.append(
            sg.Radio(
                f"{i+1}",
                "-RADIO-STARS-",
                font=font_loading,
                text_color=color_green,
                # circle_color=color_red,
                enable_events=True,
            )
        )
    return frame


def frame_layout_high_scores():
    text = (
        "     User",
        " -- Score -- ",
        "       Date",
    )

    return [
        [
            sg.Frame(
                "@ High Scores @",
                [
                    [
                        sg.T(
                            f"{x}",
                            size=12,
                            text_color=color_green,
                        )
                        for x in text
                    ],
                    [col_high_scores()],
                ],
                title_location="n",
                pad=20,
                title_color=color_red,
            )
        ],
        [
            sg.B("Agreed"),
        ],
    ]


def col_high_scores():
    return sg.Column(
        [[sg.T(col.strip(), size=12) for col in row.split()] for row in read_score()],
        element_justification="left",
    )
