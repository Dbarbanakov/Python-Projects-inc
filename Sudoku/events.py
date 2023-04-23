import PySimpleGUI as sg
from layouts import *
from events_utils import *


hp_sudoku = 81
hp_player = 0
timer = 0


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
        sudoku.apply_difficulty(event)
        hp_sudoku -= len(sudoku.opened_positions)

        window_main.ding()
        window_main["-HEALTH-SUDOKU-"].update(hp_sudoku)
        window_main["-FRAME-BUTTONS-"].update(f"{event}")

        toggle_panel_visibility(False, window_main, "-FRAME-DIFFICULTY-")

        toggle_panel_visibility(
            True,
            window_main,
            "-HEALTH-PLAYER-",
            "-TIMER-",
            "-HEALTH-SUDOKU-",
            "-FRAME-BUTTONS-",
        )

        for coords in sudoku.opened_positions:
            row, col = coords
            window_main[coords].update(
                sudoku.board[row][col], button_color=("white", "black")
            )

    if type(event) == tuple and sudoku:
        solution_number = sudoku.board[event[0]][event[1]]

        if event not in sudoku.opened_positions:
            ev, val = sg.Window(
                "Available Numbers:",
                generate_frame_with_buttons(
                    get_available_choices(sudoku.progress_board, event[0], event[1])
                ),
                no_titlebar=True,
            ).read(close=True)

            if int(ev) == solution_number:
                sudoku.opened_positions.append(event)

                hp_sudoku -= 1
                window_main["-HEALTH-SUDOKU-"].update(hp_sudoku)

                window_main[event].update(
                    solution_number, button_color=("white", "black")
                )
                sudoku.progress_board[event[0]][event[1]] = solution_number

            else:
                sg.popup_no_wait("This is not the right number.", "Health -= 1.")
                hp_player += 1
                window_main["-HEALTH-PLAYER-"].update(f"{hp_player}")
