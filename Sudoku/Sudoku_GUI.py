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


def generate_button(i, j):
    return sg.B(button_text=" ", size=(4, 2), key=(i, j), pad=(0, 0))


def toggle_panel_visibility(window, boolean, *keys):
    for key in keys:
        window[key].update(visible=boolean)


MAX_ROWS = MAX_COLS = 9
is_sudoku_generated = False
available_choices = [1, 2, 3, 4, 5, 6, 7, 8, 9]
difficulty = ""

sg.theme("DarkBlack")

squares = 81


layout_main = [
    [
        [
            sg.T("Choose a difficulty - ", key="-MAIN-TEXT-"),
            sg.B("Easy"),
            sg.B("Medium"),
            sg.B("Hard"),
        ]
    ],
    [[generate_button(i, j) for j in range(MAX_COLS)] for i in range(MAX_ROWS)],
    [sg.T("Squares left - {}".format(squares), key="-SQUARES-")],
    [sg.B("Exit")],
]


window_main = sg.Window("Choose a difficulty", layout_main)

while True:
    event, values = window_main.read()

    if event in (sg.WIN_CLOSED, "Exit"):
        break

    if event in ("Easy", "Medium", "Hard"):
        toggle_panel_visibility(window_main, False, "Easy", "Medium", "Hard")
        window_main["-MAIN-TEXT-"].update("Current Difficulty - {}".format(event))

        get_sudoku(event)
        window_main["-SQUARES-"].update(f"Squares left - {squares}")

        # print(sudoku.progress_board)
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
                                values=available_choices,
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
                window_main["-SQUARES-"].update(f"Squares left - {squares}")

                window_main[event].update(
                    sudoku.board[event[0]][event[1]], button_color=("white", "black")
                )
            else:
                sg.popup_no_wait("This is not the right number.")


window_main.close()
