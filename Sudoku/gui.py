import PySimpleGUI as sg
from layouts import *
from gui_events import *

# menu_def
# high scores
# game modes
# get_solution - timeout


while True:
    event, values = window_main.read(timeout=1000, timeout_key="-TIMEOUT-")
    if event in (sg.WIN_CLOSED, "Exit"):
        break
    else:
        get_event(event)


window_main.close()
