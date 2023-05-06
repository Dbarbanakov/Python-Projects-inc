from .utils import *


def get_layout_window_rating():
    return (
        [
            sg.Frame(
                "Stars",
                [
                    [
                        sg.Radio(
                            f"{i+1}",
                            "-RADIO-STARS-",
                            font=font_window_loading,
                            text_color=color_green,
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


def get_window_rating():
    return sg.Window(
        " ",
        get_layout_window_rating(),
        element_justification="c",
        modal=True,
        keep_on_top=True,
    )
