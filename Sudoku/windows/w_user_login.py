from .utils import *


def get_w_user_login():
    return sg.popup_get_text(
        "     Log In",
        default_text="user",
        font=FONT_WINDOW_HIGH_SCORES,
        size=(20, 10),
        text_color=COLOR_RED,
        button_color=(COLOR_RED, "black"),
        keep_on_top=True,
        no_titlebar=True,
        grab_anywhere=True,
        image=f"{path.dirname(__file__)}/../files/images/log.png",
    )
