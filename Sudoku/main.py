import PySimpleGUI as sg

from events import *


get_loading_screen()


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
