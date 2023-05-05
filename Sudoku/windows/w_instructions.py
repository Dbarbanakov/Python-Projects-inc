from .utils import *


instructions = f"{path.dirname(__file__)}/../files/instructions.txt"

layout_instructions = [
    [
        sg.MLine(
            key="-ML1-" + sg.WRITE_ONLY_KEY,
            size=(40, 8),
            background_color="black",
        )
    ],
    [sg.Button("Go"), sg.Button("Exit")],
]

window_instructions = sg.Window(
    "Window Title",
    layout_instructions,
    font=font_window_high_scores,
    button_color=(color_red, "black"),
)
