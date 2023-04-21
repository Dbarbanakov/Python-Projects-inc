import PySimpleGUI as sg
from solution import *
from layouts import *

sudoku = None


def main():
    global sudoku
    sudoku = Board()
    sudoku.get_solution(5)


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
    global hp_player, hp_sudoku, timer

    if event == "-TIMEOUT-":
        window_main["-TIMER-"].update(f"{timer}")
        timer += 1

    if timer == 100:
        ev, val = window_modal.read()
        if ev:
            window_main["-STARS-"].update(ev)
            window_modal.close()

    if event in ("Easy", "Medium", "Hard"):
        sudoku.generate_sudoku(event)

        hp_sudoku -= len(sudoku.opened_positions)

        window_main.ding()
        window_main["-HEALTH-SUDOKU-"].update(hp_sudoku)
        window_main["FRAME-BUTTONS-"].update(f"{event}")

        toggle_panel_visibility(False, "-FRAME-DIFFICULTY-")

        toggle_panel_visibility(
            True, "-HEALTH-PLAYER-", "-TIMER-", "-HEALTH-SUDOKU-", "FRAME-BUTTONS-"
        )

        for coords in sudoku.opened_positions:
            row, col = coords
            window_main[coords].update(
                sudoku.board[row][col], button_color=("white", "black")
            )

    if type(event) == tuple and sudoku:
        if event not in sudoku.opened_positions:
            ev, val = sg.Window(
                "Available Numbers:",
                generate_listbox(
                    get_available_choices(sudoku.progress_board, event[0], event[1])
                ),
            ).read(close=True)

            if val[0][0] == sudoku.board[event[0]][event[1]]:
                sudoku.opened_positions.append(event)

                hp_sudoku -= 1
                window_main["-HEALTH-SUDOKU-"].update(hp_sudoku)

                window_main[event].update(
                    sudoku.board[event[0]][event[1]], button_color=("white", "black")
                )
                sudoku.progress_board[event[0]][event[1]] = sudoku.board[event[0]][
                    event[1]
                ]

            else:
                sg.popup_no_wait("This is not the right number.", "Health -= 1.")
                hp_player += 1
                window_main["-HEALTH-PLAYER-"].update(f"{hp_player}")
