from .utils import *

from time import sleep

instructions_file = f"{path.dirname(__file__)}/../files/instructions.txt"


def get_w_instructions():
    return sg.Window(
        "Window Title",
        get_layout_w_instructions(),
        font=singleton.font_scores,
        button_color=(singleton.red, "black"),
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


def print_line(window, string, pause, color=singleton.red):
    """Prints a line(string) letter by letter with a delay(pause)."""
    for i in range(len(string)):
        window["-MULTILINE-" + sg.WRITE_ONLY_KEY].print(
            f"{string[i]}",
            text_color=(color if string[i] != "-" else singleton.red),
            end="",
        )
        window.refresh()
        sleep(pause)


def print_intro(window):
    """Prints intro with print_line()."""
    intro = " " * 7 + "Use Q to exit or Press Space to continue ... \n\n\n"
    print_line(window, intro, 0.05)


def print_instructions(window):
    """Prints the instructions file with print_line()."""
    with open(instructions_file, "r") as file:
        lines = file.readlines()

    for x in lines:
        print_line(window, x, 0.025, color=singleton.green)
