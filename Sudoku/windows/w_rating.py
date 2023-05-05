from .utils import *


layout_window_rating = (
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


window_rating = sg.Window(
    " ",
    layout_window_rating,
    element_justification="c",
    modal=True,
    keep_on_top=True,
)
