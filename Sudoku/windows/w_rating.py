from .utils import *


def get_layout_w_rating():
    return (
        [
            sg.Frame(
                "Stars",
                [
                    [
                        sg.Radio(
                            f"{i+1}",
                            "-RADIO-STARS-",
                            font=FONT_WINDOW_LOADING,
                            text_color=COLOR_GREEN,
                            enable_events=True,
                        )
                        for i in range(5)
                    ]
                ],
                key="-FRAME-RADIO-",
                title_location="n",
            ),
        ],
    )


def get_w_rating():
    return sg.Window(
        " ",
        get_layout_w_rating(),
        element_justification="c",
        modal=True,
        keep_on_top=True,
    )
