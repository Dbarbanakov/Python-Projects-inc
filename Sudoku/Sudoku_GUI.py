import PySimpleGUI as sg
from Sudoku import *


def get_sudoku(event):
    global is_sudoku_generated
    global sudoku
    sudoku = Board()
    sudoku.generate_sudoku(event)
    is_sudoku_generated = True


def generate_button(i, j):
    return sg.B(button_text=" ", size=(4, 2), key=(i, j), pad=(0, 0))


MAX_ROWS = MAX_COLS = 9
is_sudoku_generated = False
available_choices = [1, 2, 3, 4, 5, 6, 7, 8, 9]
difficulty = ""
# self.progress_board

sg.theme("DarkBlack")
squares = 81


layout_main = [
    [sg.T("Choose a difficulty - "), sg.B("Easy"), sg.B("Medium"), sg.B("Hard")],
    [[generate_button(i, j) for j in range(MAX_COLS)] for i in range(MAX_ROWS)],
    [sg.T("Squares left - {}".format(squares))],
    [sg.B("Exit")],
]


window_main = sg.Window("Choose a difficulty", layout_main)

while True:
    event, values = window_main.read()
    print(event, values)
    if event in (sg.WIN_CLOSED, "Exit"):
        break
    if event in ("Easy", "Medium", "Hard"):
        get_sudoku(event)
        print(sudoku.random_positions)
        for x in sudoku.random_positions:
            row, col = x
            window_main[x].update(
                sudoku.board[row][col], button_color=("white", "black")
            )
        # self.random_positions
    if type(event) == tuple and is_sudoku_generated:
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
            print("equal")
            window_main[event].update(
                sudoku.board[event[0]][event[1]], button_color=("white", "black")
            )
        else:
            sg.popup_no_wait("This is not the right number.")


window_main.close()
