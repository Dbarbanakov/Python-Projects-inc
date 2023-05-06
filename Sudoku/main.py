from events import *


get_loading_screen()


while True:
    event, values = window_main.read(timeout=1000)

    if event == sg.WIN_CLOSED:
        break

    else:
        get_event(event)

window_main.close()
