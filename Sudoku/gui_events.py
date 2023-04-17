import PySimpleGUI as sg
from main import *
from layouts import *


def get_sudoku(event):
    global sudoku, is_sudoku_generated, squares

    sudoku = Board()
    sudoku.generate_sudoku(event)
    is_sudoku_generated = True
    squares -= sudoku.initial_positions


def toggle_panel_visibility(boolean, *keys, window=window_main):
    for key in keys:
        window[key].update(visible=boolean)


def get_available_choices(board, row, col):
    available_choices = []
    for i in range(1, 10):
        if sudoku.check_position(board, row, col, i):
            available_choices.append(i)

    return available_choices


def get_event(event):
    global mistakes, squares, timer

    if event == "-TIMEOUT-":
        window_main["-TIMER-"].update(f"{timer}")
        timer += 1

    if event in ("Easy", "Medium", "Hard"):
        get_sudoku(event)

        toggle_panel_visibility(False, "Easy", "Medium", "Hard", "-MAIN-TEXT-")
        window_main.set_title(f"Sudoku@{event}")
        window_main["-PROGRESS-"].update(squares)

        toggle_panel_visibility(True, "-TIMER-", "-PROGRESS-", "-MISTAKES-")

        for coords in sudoku.opened_positions:
            row, col = coords
            window_main[coords].update(
                sudoku.board[row][col], button_color=("white", "black")
            )

    if type(event) == tuple and is_sudoku_generated:
        if event not in sudoku.opened_positions:
            ev, val = sg.Window(
                "Available Numbers:",
                generate_listbox(
                    get_available_choices(sudoku.progress_board, event[0], event[1])
                ),
            ).read(close=True)

            if val[0][0] == sudoku.board[event[0]][event[1]]:
                sudoku.opened_positions.append(event)

                squares -= 1
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
                window_main["-MISTAKES-"].update(f"{mistakes}")
