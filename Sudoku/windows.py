from layouts import *
from solution import *


sudoku = Board()


def get_available_choices(board, row, col):
    available_choices = []

    for i in range(1, 10):
        if sudoku.check_position(board, row, col, i):
            available_choices.append(i)

    return available_choices


def window_choices(event):
    return sg.Window(
        "Available Numbers:",
        generate_frame_with_buttons(
            get_available_choices(sudoku.progress_board, event[0], event[1])
        ),
        no_titlebar=True,
        return_keyboard_events=True,
    ).read(close=True)


def get_user_window():
    return sg.popup_get_text(
        "     Log In",
        default_text="user",
        font=font_login_scores,
        size=(20, 10),
        text_color=color_red,
        button_color=(color_red, "black"),
        keep_on_top=True,
        no_titlebar=True,
        grab_anywhere=True,
        image=f"{os.path.dirname(__file__)}/files/images/log.png",
    )


def get_high_scores_window():
    return sg.Window(
        "High Scores",
        frame_layout_high_scores(),
        font=font_login_scores,
        element_justification="c",
        no_titlebar=True,
        margins=(1, 1),
    ).read(close=True)


window_main = sg.Window(
    "Sudoku",
    layout_main,
    element_justification="c",
    font=font_main_window,
    return_keyboard_events=True,
    use_default_focus=False,
)


def window_rating():
    return sg.Window(
        " ",
        layout_rating(),
        element_justification="c",
        modal=True,
        keep_on_top=True,
    )


window_loading = sg.Window(
    "",
    layout_loading,
    element_justification="c",
    modal=True,
    keep_on_top=True,
    alpha_channel=0.5,
)
