import PySimpleGUI as sg
from events import *

# keyboard controls


for i in range(200):
    if i == 50:
        sudoku.generate_board()

    window_progress_bar.read(timeout=10)
    window_progress_bar["-LOADING-"].update(i + 1)
    window_progress_bar.set_alpha(0.5 + 0.5 * (i / 200))

window_progress_bar.close()


while True:
    event, values = window_main.read(timeout=1000, timeout_key="-TIMEOUT-")
    if event in (sg.WIN_CLOSED, "Exit"):
        break
    else:
        get_event(event)


window_main.close()
