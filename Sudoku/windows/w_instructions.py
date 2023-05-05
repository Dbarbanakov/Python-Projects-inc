from .utils import *

from time import sleep

instructions_file = f"{path.dirname(__file__)}/../files/instructions.txt"

with open(instructions_file, "r") as lines:
    instructions = lines.readlines()


def get_window_instructions():
    return sg.Window(
        "Window Title",
        get_layout_instructions(),
        font=font_window_high_scores,
        button_color=(color_red, "black"),
        return_keyboard_events=True,
        finalize=True,
    )


def get_layout_instructions():
    return [
        [
            sg.MLine(
                key="-ML1-" + sg.WRITE_ONLY_KEY,
                size=(100, 20),
                background_color="black",
                disabled=True,
            )
        ],
    ]


def str_print(window, s, pause, finish=""):
    for i in range(len(s)):
        window["-ML1-" + sg.WRITE_ONLY_KEY].print(
            f"{s[i]}", text_color="red", end=finish
        )
        window.refresh()
        sleep(pause)
