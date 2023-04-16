import PySimpleGUI as sg
from Sudoku import *


MAX_ROWS = MAX_COLS = 9
is_sudoku_generated = False
difficulty = ""

sg.theme("DarkBlack")

squares = 81
mistakes = 0
timer = 0


def get_sudoku(event):
    global sudoku
    global is_sudoku_generated
    global squares

    sudoku = Board()
    sudoku.generate_sudoku(event)
    is_sudoku_generated = True
    squares -= sudoku.initial_positions


# menu_def
# high scores
# game modes - complete solution and partial as it is.
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


def get_event(event):
    global mistakes, squares, timer

    # Acts as a timer.
    if event == "-TIMEOUT-":
        window_main["-TIMER-"].update("{}".format(timer))
        timer += 1

    # Event = Easy,Medium or Hard.
    if event in ("Easy", "Medium", "Hard"):
        # Generates the Sudoku with the selected difficulty.
        get_sudoku(event)

        # Hides difficulty panels.
        toggle_panel_visibility(
            window_main, False, "Easy", "Medium", "Hard", "-MAIN-TEXT-"
        )

        # Updates the Window.
        window_main["-PROGRESS-TEXT-"].update("{}".format(event[0]))
        window_main["-PROGRESS-"].update(squares)
        # Shows Progress bar together with the current difficulty and the amount of mistakes done.
        toggle_panel_visibility(
            window_main, True, "-TIMER-", "-PROGRESS-", "-PROGRESS-TEXT-", "-MISTAKES-"
        )

        # Updates the Sudoku board with the numbers at their random positions generated based on the selected difficulty.
        for x in sudoku.opened_positions:
            row, col = x
            window_main[x].update(
                sudoku.board[row][col], button_color=("white", "black")
            )
    # Event - Selecting a slot to open on the board.
    if type(event) == tuple and is_sudoku_generated:
        # Upon click, if the selected box is not opened - create a window and read its contents.
        # Window contains of an element(Listbox) which has values.
        # Values are equal to the numbers which are suitable for that position,
        # Considering the numbers in the already opened slots.
        if event not in sudoku.opened_positions:
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

            # Checks whether the selected number from the Listbox is equal to the one from the generated solution.
            if values_nums[0][0] == sudoku.board[event[0]][event[1]]:
                # If so, appends its position to the already opened positions.
                sudoku.opened_positions.append(event)

                # Updates squares and the main window with its value.
                squares -= 1
                window_main["-PROGRESS-"].update(squares)

                # Updates the color and shows the number on the board.
                window_main[event].update(
                    sudoku.board[event[0]][event[1]], button_color=("white", "black")
                )
                sudoku.progress_board[event[0]][event[1]] = sudoku.board[event[0]][
                    event[1]
                ]

            else:
                # If the selected number from the Listbox is not the same as the one from the solution,
                # pops a warning and updates mistakes together with the main window.
                sg.popup_no_wait("This is not the right number.", "Mistakes += 1.")
                mistakes += 1
                window_main["-MISTAKES-"].update("{}".format(mistakes))


layout_main = [
    [
        [
            sg.T(
                "{}".format(mistakes),
                key="-MISTAKES-",
                visible=False,
            ),
            sg.ProgressBar(
                81,
                orientation="h",
                key="-PROGRESS-",
                bar_color=("green", "red"),
                expand_y=True,
                visible=False,
            ),
            sg.T("{}".format(timer), key="-TIMER-", visible=False),
            sg.T("", key="-PROGRESS-TEXT-", visible=False),
            sg.T("Choose a difficulty - ", key="-MAIN-TEXT-"),
            sg.B("Easy"),
            sg.B("Medium"),
            sg.B("Hard"),
        ]
    ],
    [
        [[generate_button(i, j) for j in range(MAX_COLS)] for i in range(MAX_ROWS)],
    ],
    # [sg.B("-SAVE-")],
    [sg.B("Exit")],
]


window_main = sg.Window("Sudoku", layout_main, element_justification="c")

while True:
    event, values = window_main.read(timeout=1000, timeout_key="-TIMEOUT-")

    # if event == "-SAVE-":
    # window_main.save_to_disk("high_scores.txt")
    if event in (sg.WIN_CLOSED, "Exit"):
        break
    else:
        get_event(event)


window_main.close()
