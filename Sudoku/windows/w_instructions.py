from .utils import *

from time import sleep

instructions_file = f"{path.dirname(__file__)}/../files/instructions.txt"

with open(instructions_file, "r") as lines:
    instructions = lines.readlines()


def get_w_instructions():
    return sg.Window(
        "Window Title",
        get_layout_w_instructions(),
        font=FONT_WINDOW_HIGH_SCORES,
        button_color=(COLOR_RED, "black"),
        return_keyboard_events=True,
        finalize=True,
        disable_close=True,
        keep_on_top=True,
    )


def get_layout_w_instructions():
    return [
        [
            sg.Multiline(
                key="-MULTILINE-" + sg.WRITE_ONLY_KEY,
                size=(65, 25),
                background_color="black",
                disabled=True,
            )
        ],
    ]


def print_intro(window, string, pause, color=COLOR_RED):
    for i in range(len(string)):
        window["-MULTILINE-" + sg.WRITE_ONLY_KEY].print(
            f"{string[i]}",
            text_color=(color if string[i] != "-" else COLOR_RED),
            end="",
        )
        window.refresh()
        sleep(pause)


def print_instructions(window, pause=0.025, file=instructions):
    for x in file:
        print_intro(window, x, pause, color=COLOR_GREEN)
