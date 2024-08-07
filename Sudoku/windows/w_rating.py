from .utils import *


def get_layout_w_rating():
    """Returns layout with 5 radio buttons, keys from 1 to 5 included."""
    return (
        [
            sg.Frame(
                "Stars",
                [
                    [
                        sg.Radio(
                            f"{i}",
                            "-RADIO-STARS-",
                            key=i,
                            font=singleton.font_load,
                            text_color=singleton.green,
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
