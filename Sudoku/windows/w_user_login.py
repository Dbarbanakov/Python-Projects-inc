from .utils import *


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
        image=f"{path.dirname(__file__)}/../files/images/log.png",
    )
