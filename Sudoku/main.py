import PySimpleGUI as sg
from events import *

# high scores
# keyboard controls

for i in range(100):
    if i == 50:
        sudoku.generate_board()

    sg.one_line_progress_meter(
        "My Meter",
        i + 1,
        100,
        "key",
        "Optional message",
        orientation="h",
        no_button=True,
        no_titlebar=True,
    )

while True:
    event, values = window_main.read(timeout=1000, timeout_key="-TIMEOUT-")
    if event in (sg.WIN_CLOSED, "Exit"):
        break
    else:
        get_event(event)


window_main.close()
