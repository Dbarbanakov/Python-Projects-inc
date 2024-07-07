from .utils import *


def get_w_user_login():
    return sg.popup_get_text(
        "     Log In",
        default_text="user",
        font=singleton.font_scores,
        size=(20, 10),
        text_color=singleton.red,
        button_color=(singleton.red, "black"),
        keep_on_top=True,
        no_titlebar=True,
        grab_anywhere=True,
        image=f"{path.dirname(__file__)}/../files/images/log.png",
    )
