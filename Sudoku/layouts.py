import PySimpleGUI as sg
from layouts_utils import *

sg.theme("DarkBlack")


layout_main = [
    [
        [sg.Image(sg.PYTHON_COLORED_HEARTS_BASE64, key="-EMOJI-INITIAL-")],
        [
            sg.T("Player", key="-USER-"),
            sg.T("  VS  "),
            sg.T("Board"),
        ],
        [
            health_bar("PLAYER", 10, (color_red, color_green)),
            sg.T("", key="-TIMER-", visible=False, size=(2)),
            health_bar("SUDOKU", 81, (color_green, color_red)),
        ],
    ],
    [
        sg.Frame(
            "Choose a difficulty.",
            [
                [
                    sg.B("Easy"),
                    sg.B("Medium"),
                    sg.B("Hard", enable_events=True),
                ]
            ],
            key="-FRAME-DIFFICULTY-",
            title_location="n",
        ),
        sg.Frame(
            "",
            [[generate_button(i, j) for j in range(9)] for i in range(9)],
            key="-FRAME-BUTTONS-",
            title_location="n",
            visible=False,
        ),
    ],
    [
        sg.T(
            "Thanks for the appreciation!",
            text_color=color_red,
            key="-THANKS-",
            visible=False,
        )
    ],
    [
        sg.B("Rate me", key="-RATE-"),
        sg.Push(),
        sg.pin(
            sg.Frame("", [frame_layout_stars()], key="-FRAME-STARS-", visible=False)
        ),
        sg.Push(),
        sg.B("High Scores", key="-HIGH-SCORES-"),
    ],
    # [sg.B("Save")],
]


def layout_rating():
    return [
        [
            sg.Frame(
                "Stars",
                [frame_layout_stars_radio()],
                key="-FRAME-RADIO-",
                title_location="n",
            ),
        ],
    ]


layout_progress_bar = [
    [sg.Text("LOADING ... ", font=font_loading)],
    [
        sg.ProgressBar(
            200,
            orientation="h",
            size=(30, 20),
            key="-LOADING-",
            bar_color=(color_red, "black"),
        )
    ],
]
