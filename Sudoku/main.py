import PySimpleGUI as sg
import sys

from events import *
from windows.w_loading import *


for i in range(200):
    ev, val = window_loading.read(timeout=10)

    if ev == sg.WIN_CLOSED:
        sys.exit()

    if i in (50, 100, 150):
        window_loading["-LOADING-BAR-"].update(bar_color=(color_red, "black"))

        if i == 50:
            sudoku.generate_board()

        i += 50

    if i in (75, 125):
        window_loading["-LOADING-BAR-"].update(bar_color=(color_green, "black"))

    window_loading["-LOADING-"].update(f"LOADING ...  {i/2:02.0f}%")
    window_loading["-LOADING-BAR-"].update(i + 1)
    window_loading.set_alpha(0.5 + 0.5 * (i / 200))


window_loading.close()

# sg.show_debugger_window(location=(10, 10))
current_time = 0
start_time = int(round(time.time() * 100))

while True:
    event, values = window_main.read(timeout=1000)

    current_time = int(round(time.time() * 100)) - start_time
    timer = current_time / 100

    window_main["-TIMER-"].update(
        "{:0d}:{:02d}".format((current_time // 100) // 60, (current_time // 100) % 60)
    )

    if event == sg.WIN_CLOSED:
        break

    else:
        get_event(event, timer)

window_main.close()
