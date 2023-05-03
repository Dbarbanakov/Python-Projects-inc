import PySimpleGUI as sg
import sys

from .utils import *


def get_loading_screen():
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


layout_window_loading = [
    [sg.Text("LOADING ... ", font=font_window_loading, key="-LOADING-")],
    [
        sg.ProgressBar(
            200,
            orientation="h",
            size=(30, 20),
            key="-LOADING-BAR-",
            bar_color=(color_green, "black"),
        )
    ],
]

window_loading = sg.Window(
    "",
    layout_window_loading,
    element_justification="c",
    modal=True,
    keep_on_top=True,
    alpha_channel=0.5,
)
