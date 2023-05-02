import PySimpleGUI as sg
from .uts import *

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
