import PySimpleGUI as sg
from windows import *
from events_utils import *

hp_sudoku = 81
hp_player = 0
timer = 0
user = "Player"


def get_event(event):
    global hp_player, hp_sudoku, timer, user

    # Focus

    element = window_main.find_element_with_focus()

    if element:
        if event == "Return:36":
            element.click()

        if event == "Tab:23":
            change_prev_focus_color(element)

        if type(element.Key) == tuple:
            row, col = element.Key

            if event == "Right:114":
                col += 1 * (col < 8)
            elif event == "Left:113":
                col -= 1 * (col > 0)
            elif event == "Down:116":
                row += 1 * (row < 8)
            elif event == "Up:111":
                row -= 1 * (row > 0)

            change_color(element, "black", "white")

            coords = (row, col)
            window_main[coords].set_focus()

        change_color(window_main.find_element_with_focus(), color_green, color_red)
        window_main.refresh()

    # Focus

    if type(event) == tuple:
        solution_number = sudoku.board[event[0]][event[1]]

        if event not in sudoku.opened_positions:
            ev, val = window_choices(event)
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

    if event in ("Easy", "Medium", "Hard"):
        window_main["-FRAME-BUTTONS-"].update(event)

        window_main.set_alpha(0.5)

        sudoku.apply_difficulty(event)
        hp_sudoku -= len(sudoku.opened_positions)
        window_main["-HEALTH-SUDOKU-"].update(hp_sudoku)

        user = get_user_window()
        window_main["-USER-"].update(user)
        window_main.set_alpha(1)

        toggle_panel_visibility(False, window_main, "-FRAME-DIFFICULTY-")

        toggle_panel_visibility(
            True,
            window_main,
            "-EMOJI-SUDOKU-",
            "-HEALTH-PLAYER-",
            "-TIMER-",
            "-HEALTH-SUDOKU-",
            "-EMOJI-PLAYER-",
            "-FRAME-BUTTONS-",
        )

        for coords in sudoku.opened_positions:
            row, col = coords
            window_main[coords].update(
                sudoku.board[row][col], button_color=("white", "black")
            )

    if event == "-RATE-":
        window_rate = window_rating()
        window_main.set_alpha(0.5)

        ev, val = window_rate.read()

        if ev in (0, 1, 2, 3, 4):
            toggle_panel_visibility(False, window_main, "-RATE-")
            toggle_panel_visibility(
                True,
                window_main,
                "-THANKS-",
                "-FRAME-STARS-",
            )

            stars = get_stars(val)

            for i in range(stars):
                toggle_panel_visibility(True, window_main, f"star{i+1}")

        window_main.set_alpha(1)

        window_rate.close()

        sg.SystemTray.notify(
            f"{'@'*5}{' '*5}{'@'*5}",
            f"{' '*5}{'#'*5}" * 3,
            display_duration_in_ms=750,
            fade_in_duration=500,
            location=(800, 500),
        )

    if event == "-HIGH-SCORES-":
        window_main.set_alpha(0.5)

        format_score()

        get_high_scores_window()
        window_main.set_alpha(1)

    if event == "Save":
        score = get_score(timer, hp_player)
        write_score(score, user)

    if hp_sudoku == 0:
        score = write_score(timer, hp_player, user)
        write_score(score)
        hp_sudoku -= 1
