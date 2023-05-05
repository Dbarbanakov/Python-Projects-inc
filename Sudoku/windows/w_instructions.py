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
        disable_close=True,
        keep_on_top=True,
    )


def get_layout_instructions():
    return [
        [
            sg.MLine(
                key="-ML1-" + sg.WRITE_ONLY_KEY,
                size=(65, 25),
                background_color="black",
                disabled=True,
            )
        ],
    ]


def str_print(window, s, pause, color=color_red):
    for i in range(len(s)):
        window["-ML1-" + sg.WRITE_ONLY_KEY].print(f"{s[i]}", text_color=color, end="")
        window.refresh()
        sleep(pause)


def print_file(file, window, pause):
    for x in file:
        str_print(window, x, pause, color=color_green)
