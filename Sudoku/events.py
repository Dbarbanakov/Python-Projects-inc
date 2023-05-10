from windows import *
from events_utils import *

import sys


def get_event(event):
    global hp_player, hp_sudoku, consequences

    # Focus Logic starts

    element = window_main.find_element_with_focus()

    if element:
        if event == "Return:36":
            element.click()

        if event == "Tab:23":
            prev_element = element.get_previous_focus()

            change_button_color(prev_element)

            if prev_element.Key == "-INSTRUCTIONS-":
                change_button_color(prev_element, color2=color_yellow)

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

            change_button_color(element)

            coords = (row, col)
            window_main[coords].set_focus()

        change_button_color(
            window_main.find_element_with_focus(), color_green, color_red
        )
        window_main.refresh()

    # Focus Logic ends

    if type(event) == tuple:
        row, col = event

        solution_number = sudoku.board[row][col]

        if event not in sudoku.opened_positions:
            nums = [
                x
                for x in range(1, 10)
                if sudoku.check_position(sudoku.progress_board, row, col, x)
            ]

            window_available_numbers = get_window_available_numbers(nums)

            is_ele_clicked = {num: False for num in nums}

            tabs = 0

            while True:
                ev, val = window_available_numbers.read()

                # Keyboard Focus

                focus_ele = window_available_numbers.find_element_with_focus()

                if focus_ele:
                    prev_focus_ele = focus_ele.get_previous_focus()

                    if ev == "Return:36":
                        focus_ele.click()

                if ev in ("q:24", sg.WIN_CLOSED):
                    break

                if ev == ("Tab:23"):
                    change_button_color(focus_ele, color2=color_red)

                    if tabs == 0:
                        tabs += 1
                        continue

                    color = (
                        color_yellow
                        if is_ele_clicked[prev_focus_ele.Key]
                        else color_blue
                    )

                    change_button_color(prev_focus_ele, color2=color)

                # Keyboard Focus

                if (
                    type(ev) is str
                    and ev[0].isdecimal()
                    and int(ev[0]) in nums
                    or type(ev) is int
                    and ev in nums
                ):
                    ev = int(ev[0]) if type(ev) is str else ev

                    if ev == solution_number:
                        sudoku.opened_positions.append(event)

                        window_main[event].update(
                            solution_number, button_color=("white", "black")
                        )

                        sudoku.progress_board[row][col] = solution_number

                        hp_sudoku -= 1
                        window_main["-HEALTH-BOARD-"].update(hp_sudoku)

                        consequences += 1
                        window_main["-CONSEQUENCES-"].update(
                            f"Consequence - {consequences}"
                        )

                        update_score(consequences)

                        hp_player += consequences
                        update_health_bar(window_main, hp_player)

                        break

                    else:
                        window_available_numbers[ev].update(button_color=color_yellow)
                        is_ele_clicked[ev] = True

                        hp_player -= 1
                        update_health_bar(window_main, hp_player)

                        consequences = 0
                        window_main["-CONSEQUENCES-"].update(
                            f"Consequence - {consequences}"
                        )

            window_available_numbers.close()

    if event in ("Easy", "Medium", "Hard"):
        window_main.finalize()
        window_main[event].block_focus()
        window_main["-FRAME-BUTTONS-"].update(event)
        window_main["-HEALTH-PLAYER-"].update(hp_player)

        window_main.set_alpha(0.5)

        sudoku.apply_difficulty(event)
        hp_sudoku -= len(sudoku.opened_positions)
        window_main["-HEALTH-BOARD-"].update(hp_sudoku)

        user = get_window_user_login()
        window_main["-USER-"].update(user)

        for coords in sudoku.opened_positions:
            row, col = coords
            window_main[coords].update(
                sudoku.board[row][col], button_color=("white", "black")
            )

        window_main.set_alpha(1)

        toggle_element_visibility(False, window_main, "-FRAME-DIFFICULTY-")

        toggle_element_visibility(
            True,
            window_main,
            "-AVATAR-BOARD-",
            "-HEALTH-PLAYER-",
            "-TIMER-",
            "-HEALTH-BOARD-",
            "-AVATAR-PLAYER-",
            "-FRAME-BUTTONS-",
            "-CONSEQUENCES-",
            "-SCORE-",
        )

    if event == "-INSTRUCTIONS-":
        window_main.set_alpha(0.5)

        window_instructions = get_window_instructions()

        str_print(
            window_instructions,
            " " * 7 + "Use Q to exit or Press Space to continue ... \n\n\n",
            0.05,
        )

        was_space_pressed = False

        while True:
            ev, val = window_instructions.read()

            if ev in (sg.WIN_CLOSED, "q:24"):
                break

            if ev == "space:65" and not was_space_pressed:
                window_instructions.DisableClose = False
                print_instructions(window_instructions)

                was_space_pressed = True

        window_instructions.close()
        window_main.set_alpha(1)

    if event == "-RATE-":
        window_main.set_alpha(0.5)

        window_rating = get_window_rating()
        ev, val = window_rating.read(close=True)

        if ev in (0, 1, 2, 3, 4):
            toggle_element_visibility(False, window_main, "-RATE-")
            toggle_element_visibility(
                True,
                window_main,
                "-THANKS-",
                "-FRAME-STARS-",
            )

            stars = ev + 1

            for i in range(stars):
                toggle_element_visibility(True, window_main, f"star{i}")

        window_main.set_alpha(1)

    if event == "-HIGH-SCORES-":
        window_main.set_alpha(0.5)

        get_window_high_scores().read(close=True)

        window_main.set_alpha(1)

    if hp_sudoku == 0:
        window_main.set_alpha(0.5)

        username = window_main["-USER-"].get()

        score = int(window_main["-SCORE-"].get().split()[-1])
        append_score(score, username)
        write_score()

        hp_sudoku -= 1

        window_high_scores = get_window_high_scores()
        ev, val = window_high_scores.read(close=True)

        if ev == "-ENDGAME-":
            window_high_scores.close()
            sys.exit()
