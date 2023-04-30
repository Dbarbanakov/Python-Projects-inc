import PySimpleGUI as sg
import sys
from events import *


for i in range(60):
    if i == 50:
        sudoku.generate_board()

    ev, val = window_progress_bar.read(timeout=10)

    if ev == sg.WIN_CLOSED:
        sys.exit()

    window_progress_bar["-LOADING-"].update(i + 1)
    window_progress_bar.set_alpha(0.5 + 0.5 * (i / 200))

window_progress_bar.close()

# sg.show_debugger_window(location=(10, 10))

while True:
    event, values = window_main.read(timeout=1000)

    if event == sg.TIMEOUT_KEY:
        window_main["-TIMER-"].update(f"{timer}")
        timer += 1

    if event == sg.WIN_CLOSED:
        break

    else:
        get_event(event)

window_main.close()
