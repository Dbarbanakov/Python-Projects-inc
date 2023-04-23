import PySimpleGUI as sg
from layouts_utils import *

sg.theme("DarkBlack")


layout_main = [
    [
        [
            sg.T("Player"),
            sg.T("VS"),
            sg.T("Sudoku"),
        ],
        [
            sg.ProgressBar(
                10,
                orientation="h",
                key="-HEALTH-PLAYER-",
                bar_color=("red", "green"),
                expand_y=True,
                visible=False,
                size=(21),
            ),
            sg.T("VS", key="-TIMER-", visible=False),
            sg.ProgressBar(
                81,
                orientation="h",
                key="-HEALTH-SUDOKU-",
                bar_color=("green", "red"),
                expand_y=True,
                visible=False,
                size=(21),
            ),
        ],
    ],
    [
        sg.Frame(
            "Choose a difficulty.",
            [
                [
                    sg.B("Easy", bind_return_key=True),
                    sg.B("Medium", bind_return_key=True),
                    sg.B("Hard", bind_return_key=True),
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
    [sg.T("", key="-STARS-")],
    # [sg.B("Save", image_source="nums.png")],
    [sg.B("Exit")],
]

layout_modal = [
    [
        sg.Frame(
            "Stars",
            [
                [
                    sg.Radio("*", "stars", key="1 STAR", enable_events=True),
                    sg.Radio("**", "stars", key="2 STARS", enable_events=True),
                    sg.Radio("***", "stars", key="3 STARS", enable_events=True),
                ]
            ],
        )
    ]
]

window_main = sg.Window(
    "Sudoku",
    layout_main,
    element_justification="c",
)

window_modal = sg.Window(
    "Rate me.",
    layout_modal,
    modal=True,
    element_justification="c",
    return_keyboard_events=True,
    disable_close=True,
)
