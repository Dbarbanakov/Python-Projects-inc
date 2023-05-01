import PySimpleGUI as sg
from layouts_utils import *

sg.theme("DarkBlack")


layout_window_main = [
    [
        sg.vbottom(
            [
                sg.Image(
                    sg.PYTHON_COLORED_HEARTS_BASE64,
                    key="-EMOJI-PLAYER-",
                    visible=False,
                    subsample=2,
                ),
                sg.Column(
                    [
                        [sg.T("Player", key="-USER-")],
                        [get_health_bar("PLAYER", 10, (color_red, color_green))],
                    ]
                ),
                sg.Text(
                    "0", key="-TIMER-", visible=False, size=(2), justification="center"
                ),
                sg.Column(
                    [
                        [sg.Push(), sg.T("Board")],
                        [get_health_bar("SUDOKU", 81, (color_green, color_red))],
                    ]
                ),
                sg.Image(
                    sg.PYTHON_COLORED_HEARTS_BASE64,
                    key="-EMOJI-SUDOKU-",
                    visible=False,
                    subsample=2,
                ),
            ]
        ),
    ],
    [
        sg.Frame(
            "Choose a difficulty.",
            [
                [
                    sg.B("Easy"),
                    sg.B("Medium"),
                    sg.B("Hard"),
                ]
            ],
            key="-FRAME-DIFFICULTY-",
            title_location="n",
        ),
        sg.Frame(
            "",
            [[get_button(i, j) for j in range(9)] for i in range(9)],
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
            sg.Frame(
                "",
                [
                    [
                        sg.Image(
                            f"{os.path.dirname(__file__)}/files/images/star.png",
                            key=f"star{x}",
                            visible=False,
                        )
                        for x in range(5)
                    ]
                ],
                key="-FRAME-STARS-",
                visible=False,
            )
        ),
        sg.Push(),
        sg.B("High Scores", key="-HIGH-SCORES-"),
    ],
    # [sg.B("Save")],
]

layout_window_rating = (
    [
        sg.Frame(
            "Stars",
            [
                [
                    sg.Radio(
                        f"{i+1}",
                        "-RADIO-STARS-",
                        font=font_window_loading,
                        text_color=color_green,
                        enable_events=True,
                    )
                    for i in range(5)
                ]
            ],
            key="-FRAME-RADIO-",
            title_location="n",
        ),
    ],
)

layout_window_loading = [
    [sg.Text("LOADING ... ", font=font_window_loading, key="-LOADING-")],
    [
        sg.ProgressBar(
            200,
            orientation="h",
            size=(30, 20),
            key="-LOADING-BAR-",
            bar_color=(color_green, "black"),
        )
    ],
]
