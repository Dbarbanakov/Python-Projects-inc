import PySimpleGUI as sg
from windows import *
from events_utils import *
from scores import *

hp_sudoku = 81
hp_player = 0
timer = 0
user = "Player"


def get_event(event):
    global hp_player, hp_sudoku, timer, user

    if hp_sudoku == 0:
        score = write_score(timer, hp_player, user)
        write_score(score)
        hp_sudoku -= 1

    if event == "-TIMEOUT-":
        window_main["-TIMER-"].update(f"{timer}")
        timer += 1

    if event in ("Easy", "Medium", "Hard"):
        window_main["-FRAME-BUTTONS-"].update(event)

        sudoku.apply_difficulty(event)
        hp_sudoku -= len(sudoku.opened_positions)
        window_main["-HEALTH-SUDOKU-"].update(hp_sudoku)

        user = get_user_window()
        window_main["-USER-"].update(user)

        toggle_panel_visibility(False, window_main, "-FRAME-DIFFICULTY-")

        toggle_panel_visibility(
            True,
            window_main,
            "-HEALTH-PLAYER-",
            "-TIMER-",
            "-HEALTH-SUDOKU-",
            "-FRAME-BUTTONS-",
            "-RATE-",
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
                hp_player += 1
                window_main["-HEALTH-PLAYER-"].update(f"{hp_player}")

    if event == "Save":
        score = get_score(timer, hp_player)
        write_score(score, user)

    if event == "-RATE-":
        toggle_panel_visibility(False, window_main, "-RATE-")
        ev, val = window_modal.read()
        if ev:
            stars = get_stars(val)

            for i in range(stars):
                toggle_panel_visibility(True, window_main, f"star{i+1}")

            window_modal.close()

    if event == "-HIGH-SCORES-":
        format_score()
        sg.Window(
            "High Scores",
            frame_layout_high_scores(),
            font=("FreeSerif", 12, "bold"),
            element_justification="c",
            no_titlebar=True,
            margins=(1, 1),
        ).read(close=True)
