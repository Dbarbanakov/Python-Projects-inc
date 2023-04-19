import PySimpleGUI as sg
from layouts import *
from events import *

from multiprocessing import Process
import time

# high scores
# game modes
# get_solution - timeout
# bug - input - enter

# loading - processess

# random number generation


for i in range(500):
    if i == 1:
        start = time.time()
        main()
        print(f"finished - {time.time() - start}")

    sg.one_line_progress_meter(
        "My Meter",
        i + 1,
        500,
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
