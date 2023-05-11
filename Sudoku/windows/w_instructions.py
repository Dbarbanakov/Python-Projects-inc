from .utils import *

from time import sleep

instructions_file = f"{path.dirname(__file__)}/../files/instructions.txt"

# with open(instructions_file, "r") as lines:
#     instructions = lines.readlines()


def get_w_instructions():
    return sg.Window(
        "Window Title",
        get_layout_w_instructions(),
        font=FONT_SCORES,
        button_color=(RED, "black"),
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


def print_intro(window, string, pause, color=RED):
    for i in range(len(string)):
        window["-MULTILINE-" + sg.WRITE_ONLY_KEY].print(
            f"{string[i]}",
            text_color=(color if string[i] != "-" else RED),
            end="",
        )
        window.refresh()
        sleep(pause)


def print_instructions(window):
    with open(instructions_file, "r") as file:
        lines = file.readlines()

    for x in lines:
        print_intro(window, x, 0.025, color=GREEN)
