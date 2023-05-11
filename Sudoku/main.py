from events import *

get_loading_screen()


while True:
    event, values = w_main.read(timeout=1000)

    if event:
        w_main["-TIMER-"].update(get_chronometer())

    if event == sg.WIN_CLOSED:
        break

    else:
        get_event(event)

w_main.close()
