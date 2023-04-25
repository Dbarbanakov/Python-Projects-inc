import PySimpleGUI as sg
from layouts_utils import *

sg.theme("DarkBlack")


layout_main = [
    [
        [
            sg.T("Player", key="-USER-"),
            sg.T("VS"),
            sg.T("Sudoku"),
        ],
        [
            health_bar("PLAYER", 10, ("red", "green")),
            sg.T("VS", key="-TIMER-", visible=False),
            health_bar("SUDOKU", 81, ("green", "red")),
        ],
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
            [[generate_button(i, j) for j in range(9)] for i in range(9)],
            key="-FRAME-BUTTONS-",
            title_location="n",
            visible=False,
        ),
    ],
    [sg.B("Save")],
    [
        sg.Frame(
            " ",
            [frame_layout_stars()],
            key="-FRAME-STARS-",
        ),
    ],
    [sg.B("High Scores", key="-HIGH-SCORES-")],
    [sg.B("Exit")],
]

layout_modal = [
    [
        sg.Frame(
            "Stars",
            [frame_layout_stars_radio()],
            key="-FRAME-RADIO-",
            title_location="n",
        ),
    ],
]

window_main = sg.Window(
    "Sudoku",
    layout_main,
    element_justification="c",
)

window_modal = sg.Window(
    " ",
    layout_modal,
    element_justification="c",
    modal=True,
    disable_close=True,
)
