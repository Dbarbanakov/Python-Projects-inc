from .utils import *

import sys


def get_loading_screen():
    for i in range(200):
        ev, val = w_loading.read(timeout=10)

        if ev == sg.WIN_CLOSED:
            sys.exit()

        if i in (50, 100, 150):
            w_loading["-LOADING-BAR-"].update(bar_color=(RED, "black"))

            if i == 50:
                sdk.generate_board()
                for row in sdk.board:
                    if 0 in row:
                        sys.exit()

            i += 50

        if i in (75, 125):
            w_loading["-LOADING-BAR-"].update(bar_color=(GREEN, "black"))

        w_loading["-LOADING-"].update(f"LOADING ...  {i/2:02.0f}%")
        w_loading["-LOADING-BAR-"].update(i + 1)
        w_loading.set_alpha(0.5 + 0.5 * (i / 200))

    w_loading.close()


layout_w_loading = [
    [sg.Text("LOADING ... ", font=FONT_LOAD, key="-LOADING-")],
    [
        sg.ProgressBar(
            200,
            orientation="h",
            size=(30, 20),
            key="-LOADING-BAR-",
            bar_color=(GREEN, "black"),
        )
    ],
]

w_loading = sg.Window(
    "",
    layout_w_loading,
    element_justification="c",
    modal=True,
    keep_on_top=True,
    alpha_channel=0.5,
)
