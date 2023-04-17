import PySimpleGUI as sg

sg.theme("DarkBlack")

is_sudoku_generated = False
difficulty = ""

squares = 81
mistakes = 0
timer = 0


def generate_button(i, j):
    return sg.B(
        button_text=" ",
        size=(4, 2),
        key=(i, j),
        pad=(0, 0),
        border_width=2,
        font=("Helvetica", 10, "bold"),
        auto_size_button=False,
    )


def generate_listbox(numbers):
    return (
        [
            [
                sg.Listbox(
                    values=numbers,
                    size=(20, 10),
                    enable_events=True,
                )
            ],
        ],
    )


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
        sg.T("Choose a difficulty - ", key="-MAIN-TEXT-"),
        sg.B("Easy", bind_return_key=True),
        sg.B("Medium", bind_return_key=True),
        sg.B("Hard", bind_return_key=True),
        sg.Frame(
            "",
            [[generate_button(i, j) for j in range(9)] for i in range(9)],
            key="-BUTTON-FRAME-",
            visible=False,
            title_location="n",
        ),
    ],
    [
        [generate_button(11, 11) for i in range(5)],
    ],
    [sg.B("Save")],
    [sg.B("Exit")],
]


window_main = sg.Window("Sudoku", layout_main, element_justification="c")
