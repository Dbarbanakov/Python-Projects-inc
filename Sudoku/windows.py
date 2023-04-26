from layouts import *


def get_user_window():
    return sg.popup_get_text(
        "     Log In",
        default_text="user",
        font=("Chilanka", 12, "bold"),
        size=(20, 10),
        text_color="#FF3300",
        button_color=("#FF3300", "black"),
        keep_on_top=True,
        no_titlebar=True,
        grab_anywhere=True,
        image=f"{os.path.dirname(__file__)}/images/log.png",
    )


def get_high_scores_window():
    return sg.Window(
        "High Scores",
        frame_layout_high_scores(),
        font=("FreeSerif", 12, "bold"),
        element_justification="c",
        no_titlebar=True,
        margins=(1, 1),
    ).read(close=True)


window_main = sg.Window(
    "Sudoku", layout_main, element_justification="c", font=("Purisa", 12, "bold")
)

window_modal = sg.Window(
    " ",
    layout_modal,
    element_justification="c",
    modal=True,
    disable_close=True,
)

window_progress_bar = sg.Window(
    "",
    layout_progress_bar,
    element_justification="c",
    modal=True,
    disable_close=True,
    keep_on_top=True,
    alpha_channel=0.5,
)
