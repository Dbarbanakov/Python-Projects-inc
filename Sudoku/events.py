from windows import *
from events_utils import *

import sys


def get_event(event):
    global HP_PLAYER, HP_BOARD, COMBO

    # Focus Logic starts

    focus = w_main.find_element_with_focus()

    if focus:
        if event == "Return:36":
            focus.click()

        if event == "Tab:23":
            prev_focus = focus.get_previous_focus()

            prev_focus.update(
                button_color="black"
                if prev_focus.get_text() in range(1, 10)
                else "white"
            )

        if type(focus.Key) == tuple:
            row, col = focus.Key

            if event == "Right:114":
                col += 1 * (col < 8)
            elif event == "Left:113":
                col -= 1 * (col > 0)
            elif event == "Down:116":
                row += 1 * (row < 8)
            elif event == "Up:111":
                row -= 1 * (row > 0)

            focus.update(
                button_color="black" if focus.get_text() in range(1, 10) else "white"
            )

            w_main[(row, col)].set_focus()

        focus = w_main.find_element_with_focus()
        focus.update(button_color=GREEN if focus.get_text() in range(1, 10) else RED)
        w_main.refresh()

    # Focus Logic ends

    if type(event) == tuple:
        row, col = event

        solution_number = sudoku.board[row][col]

        if event not in sudoku.opened_coords:
            nums = [
                x
                for x in range(1, 10)
                if sudoku.check_position(sudoku.progress_board, row, col, x)
            ]

            w_choices = get_w_choices(nums)

            clicked = {num: False for num in nums}

            tabs = 0

            # w_choices - open

            while True:
                ev, val = w_choices.read()

                if ev in ("q:24", sg.WIN_CLOSED):
                    break

                # Focus - w_choices

                focus = w_choices.find_element_with_focus()

                if focus and ev == "Return:36":
                    focus.click()

                if ev == ("Tab:23"):
                    focus.update(button_color=RED)

                    prev_focus = focus.get_previous_focus()

                    if tabs == 0:
                        tabs += 1
                        continue

                    prev_focus.update(
                        button_color=YELLOW if clicked[prev_focus.Key] else BLUE
                    )

                # Focus - w_choices

                if ev in nums or ev[0].isdecimal() and int(ev[0]) in nums:
                    num = int(ev[0]) if type(ev) is str else ev

                    if num == solution_number:
                        sudoku.opened_coords.append(event)
                        sudoku.progress_board[row][col] = solution_number

                        w_main[event].update(
                            solution_number, button_color=("white", "black")
                        )

                        HP_BOARD -= 1
                        COMBO += 1
                        HP_PLAYER += COMBO

                        w_main["-COMBO-"].update(f"Combo - {COMBO}")

                        colors = get_hp_bar_colors(HP_PLAYER)
                        w_main["-HP-PLAYER-"].update(HP_PLAYER % 10, bar_color=colors)

                        w_main["-HP-BOARD-"].update(HP_BOARD)

                        w_main["-SCORE-"].update(f"Score - {get_score() + 10 + COMBO}")

                        break

                    else:
                        COMBO = 0
                        HP_PLAYER -= 1

                        w_choices[num].update(button_color=YELLOW)
                        clicked[num] = True

                        w_main["-COMBO-"].update(f"Combo - {COMBO}")

                        colors = get_hp_bar_colors(HP_PLAYER)
                        w_main["-HP-PLAYER-"].update(HP_PLAYER % 10, bar_color=colors)

            w_choices.close()

    if event in ("Easy", "Medium", "Hard"):
        w_main.finalize()
        w_main[event].block_focus()
        w_main["-FRAME-BUTTONS-"].update(event)
        w_main["-HP-PLAYER-"].update(HP_PLAYER)

        w_main.set_alpha(0.5)

        sudoku.apply_difficulty(event)
        HP_BOARD -= len(sudoku.opened_coords)
        w_main["-HP-BOARD-"].update(HP_BOARD)

        user = get_w_user_login()
        w_main["-USER-"].update(user)

        for coord in sudoku.opened_coords:
            row, col = coord
            w_main[coord].update(
                sudoku.board[row][col], button_color=("white", "black")
            )

        w_main.set_alpha(1)

        # Hides -FRAME-DIFFICULTY-, shows rest.
        toggle_element_visibility(
            "-FRAME-DIFFICULTY-",
            "-AVATAR-BOARD-",
            "-HP-PLAYER-",
            "-TIMER-",
            "-HP-BOARD-",
            "-AVATAR-PLAYER-",
            "-FRAME-BUTTONS-",
            "-COMBO-",
            "-SCORE-",
        )

    if event == "-INSTRUCTIONS-":
        w_main.set_alpha(0.5)

        w_instructions = get_w_instructions()

        print_intro(
            w_instructions,
            " " * 7 + "Use Q to exit or Press Space to continue ... \n\n\n",
            0.05,
        )

        was_space_pressed = False

        while True:
            ev, val = w_instructions.read()

            if ev in (sg.WIN_CLOSED, "q:24"):
                break

            if ev == "space:65" and not was_space_pressed:
                was_space_pressed = True
                w_instructions.DisableClose = False

                print_instructions(w_instructions)

        w_instructions.close()
        w_main.set_alpha(1)

    if event == "-RATE-":
        w_main.set_alpha(0.5)

        w_rating = get_w_rating()
        ev, val = w_rating.read(close=True)
        if ev in range(5):
            # Hides -RATE-, shows rest.
            toggle_element_visibility(
                "-RATE-",
                "-THANKS-",
                "-FRAME-STARS-",
            )

            for i in range(ev + 1):
                # Shows a star for each iteration.
                toggle_element_visibility(f"{i}")

        w_main.set_alpha(1)

    if event == "-HIGH-SCORES-":
        w_main.set_alpha(0.5)

        get_w_high_scores().read(close=True)

        w_main.set_alpha(1)

    if HP_BOARD == 0:
        w_main.set_alpha(0.5)

        HP_BOARD -= 1

        username = w_main["-USER-"].get()
        score = get_score()

        append_score(score, username)
        write_score()

        w_high_scores = get_w_high_scores()
        ev, val = w_high_scores.read(close=True)

        if ev == "-ENDGAME-":
            w_high_scores.close()
            sys.exit()
