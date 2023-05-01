from layouts import *
from solution import *


sudoku = Board()


def get_available_numbers(board, row, col):
    """Helper function for get_window_available_numbers()."""
    available_numbers = []

    for i in range(1, 10):
        if sudoku.check_position(board, row, col, i):
            available_numbers.append(i)

    return available_numbers


def get_window_available_numbers(event):
    """Returns the window after clicking on an empty Board coord[x,y] with the available numbers to choose from."""
    return sg.Window(
        "Available Numbers:",
        get_layout_window_available_numbers(
            get_available_numbers(sudoku.progress_board, event[0], event[1])
        ),
        no_titlebar=True,
        return_keyboard_events=True,
    ).read(close=True)


def get_window_user_login():
    return sg.popup_get_text(
        "     Log In",
        default_text="user",
        font=font_window_high_scores,
        size=(20, 10),
        text_color=color_red,
        button_color=(color_red, "black"),
        keep_on_top=True,
        no_titlebar=True,
        grab_anywhere=True,
        image=f"{os.path.dirname(__file__)}/files/images/log.png",
    )


def get_window_high_scores():
    return sg.Window(
        "High Scores",
        get_layout_window_high_scores(),
        font=font_window_high_scores,
        element_justification="c",
        no_titlebar=True,
        margins=(1, 1),
    ).read(close=True)


window_main = sg.Window(
    "Sudoku",
    layout_window_main,
    element_justification="c",
    font=font_window_main,
    return_keyboard_events=True,
    use_default_focus=False,
)


window_rating = sg.Window(
    " ",
    layout_window_rating,
    element_justification="c",
    modal=True,
    keep_on_top=True,
)

window_loading = sg.Window(
    "",
    layout_window_loading,
    element_justification="c",
    modal=True,
    keep_on_top=True,
    alpha_channel=0.5,
)
