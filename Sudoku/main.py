import PySimpleGUI as sg
import sys
from events import *


for i in range(200):
    if i == 50:
        sudoku.generate_board()

    ev, val = window_progress_bar.read(timeout=10)

    if ev == sg.WIN_CLOSED:
        sys.exit()

    window_progress_bar["-LOADING-"].update(i + 1)
    window_progress_bar.set_alpha(0.5 + 0.5 * (i / 200))

window_progress_bar.close()


while True:
    event, values = window_main.read(timeout=1000, timeout_key="-TIMEOUT-")
    if event == sg.WIN_CLOSED:
        break
    else:
        get_event(event)

window_main.close()
