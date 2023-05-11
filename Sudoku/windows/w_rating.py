from .utils import *


def get_layout_w_rating():
    return (
        [
            sg.Frame(
                "Stars",
                [
                    [
                        sg.Radio(
                            f"{i}",
                            "-RADIO-STARS-",
                            font=FONT_LOAD,
                            text_color=GREEN,
                            enable_events=True,
                        )
                        for i in range(1, 6)
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
