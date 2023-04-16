import PySimpleGUI as sg
from Sudoku import *


def get_sudoku(event):
    global sudoku
    global is_sudoku_generated
    global squares

    sudoku = Board()
    sudoku.generate_sudoku(event)
    is_sudoku_generated = True
    squares -= sudoku.initial_positions


# menu_def
# fix progress_board - print_partial_board
# high scores
# game modes - complete solution and partial as it is.
# timer
# get_solution - timeout


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


def toggle_panel_visibility(window, boolean, *keys):
    for key in keys:
        window[key].update(visible=boolean)


def get_available_choices(board, row, col):
    available_choices = []
    for i in range(1, 10):
        if sudoku.check_position(board, row, col, i):
            available_choices.append(i)

    return available_choices


MAX_ROWS = MAX_COLS = 9
is_sudoku_generated = False
difficulty = ""

sg.theme("DarkBlack")

squares = 81
mistakes = 0

layout_main = [
    [
        [
            sg.T("", key="-PROGRESS-TEXT-", visible=False),
            sg.T("{}".format(mistakes), key="-MISTAKES-", visible=False),
            sg.ProgressBar(
                81,
                orientation="h",
                key="-PROGRESS-",
                bar_color=("green", "red"),
                expand_y=True,
                visible=False,
            ),
            sg.T("Choose a difficulty - ", key="-MAIN-TEXT-"),
            sg.B("Easy"),
            sg.B("Medium"),
            sg.B("Hard"),
        ]
    ],
    [
        [[generate_button(i, j) for j in range(MAX_COLS)] for i in range(MAX_ROWS)],
    ],
    [sg.B("Exit")],
    # [
    # sg.T("Squares left - {}".format(squares), key="-SQUARES-"),
    # ],
]


window_main = sg.Window("Sudoku", layout_main, element_justification="c")

while True:
    event, values = window_main.read()

    if event in (sg.WIN_CLOSED, "Exit"):
        break

    if event in ("Easy", "Medium", "Hard"):
        toggle_panel_visibility(
            window_main, False, "Easy", "Medium", "Hard", "-MAIN-TEXT-"
        )
        toggle_panel_visibility(
            window_main, True, "-PROGRESS-", "-PROGRESS-TEXT-", "-MISTAKES-"
        )
        # window_main["-MAIN-TEXT-"].update("Current Difficulty - {}".format(event))
        window_main["-PROGRESS-TEXT-"].update("{}".format(event[0]))

        get_sudoku(event)
        # window_main["-SQUARES-"].update(f"Squares left - {squares}")
        window_main["-PROGRESS-"].update(squares)

        for x in sudoku.random_positions:
            row, col = x
            window_main[x].update(
                sudoku.board[row][col], button_color=("white", "black")
            )

    if type(event) == tuple and is_sudoku_generated:
        if event not in sudoku.random_positions:
            event_nums, values_nums = sg.Window(
                "Available Numbers:",
                [
                    [
                        [
                            sg.Listbox(
                                values=get_available_choices(
                                    sudoku.progress_board, event[0], event[1]
                                ),
                                size=(20, 10),
                                enable_events=True,
                            )
                        ],
                    ]
                ],
            ).read(close=True)
            if values_nums[0][0] == sudoku.board[event[0]][event[1]]:
                sudoku.random_positions.append(event)

                squares -= 1
                # window_main["-SQUARES-"].update(f"Squares left - {squares}")
                window_main["-PROGRESS-"].update(squares)

                window_main[event].update(
                    sudoku.board[event[0]][event[1]], button_color=("white", "black")
                )
                sudoku.progress_board[event[0]][event[1]] = sudoku.board[event[0]][
                    event[1]
                ]

            else:
                sg.popup_no_wait("This is not the right number.", "Mistakes += 1.")
                mistakes += 1
                window_main["-MISTAKES-"].update("{}".format(mistakes))


window_main.close()
