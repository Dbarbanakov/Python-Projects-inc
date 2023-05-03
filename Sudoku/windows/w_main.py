import PySimpleGUI as sg
from .utils import *


def get_health_bar(name, max, colors):
    """Used for both Player's and Board's health bars."""
    return sg.ProgressBar(
        max,
        orientation="h",
        key=f"-HEALTH-{name}-",
        bar_color=colors,
        visible=False,
        size=(15, 20),
    )


layout_main = [
    [
        sg.vbottom(
            [
                sg.Image(
                    f"{os.path.dirname(__file__)}/../files/images/avatar_player.png",
                    key="-AVATAR-PLAYER-",
                    visible=False,
                ),
                sg.Column(
                    [
                        [sg.T("Player", key="-USER-")],
                        [get_health_bar("PLAYER", 10, (color_red, color_green))],
                    ]
                ),
                sg.Text(
                    "0", key="-TIMER-", visible=False, size=(6), justification="center"
                ),
                sg.Column(
                    [
                        [sg.Push(), sg.T("Board")],
                        [get_health_bar("SUDOKU", 81, (color_green, color_red))],
                    ]
                ),
                sg.Image(
                    f"{os.path.dirname(__file__)}/../files/images/avatar_board.png",
                    key="-AVATAR-SUDOKU-",
                    visible=False,
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
            [
                [
                    sg.B(
                        " ",
                        size=(4, 2),
                        key=(i, j),
                        pad=(0, 0),
                        border_width=2,
                        font=font_window_high_scores,
                    )
                    for j in range(9)
                ]
                for i in range(9)
            ],
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
                            f"{os.path.dirname(__file__)}/../files/images/star.png",
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
]

window_main = sg.Window(
    "Sudoku",
    layout_main,
    element_justification="c",
    font=font_window_main,
    return_keyboard_events=True,
    use_default_focus=False,
)
