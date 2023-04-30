import PySimpleGUI as sg
import sys, psutil
from events import *


for i in range(200):
    if i == 50:
        sudoku.generate_board()
    if i > 100 and i % 25 == 0:
        i += 50
    ev, val = window_loading.read(timeout=10)

    if ev == sg.WIN_CLOSED:
        sys.exit()

    cpu_percent = psutil.cpu_percent(interval=0.02)

    window_loading["text"].update(f"LOADING ...  {cpu_percent:02.0f}%")

    window_loading["-LOADING-"].update(i + 1)
    window_loading.set_alpha(0.5 + 0.5 * (i / 200))

window_loading.close()

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
