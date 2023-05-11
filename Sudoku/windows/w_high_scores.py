from .utils import *

from events_utils import read_score


def get_layout_w_high_scores():
    headings = (" ", "User", "  -- Score -- ", "Date")

    return [
        [
            sg.Frame(
                "@ High Scores @",
                [
                    [sg.T(f"{x}", size=14, text_color=COLOR_GREEN) for x in headings],
                    [
                        sg.Column(
                            [
                                [sg.T(col.strip(), size=14) for col in row.split()]
                                for row in read_score()
                            ],
                        )
                    ],
                ],
                title_location="n",
                title_color=COLOR_RED,
            )
        ],
        [
            sg.B(
                "Confirm",
                bind_return_key=True,
                button_color=(COLOR_RED, "black"),
                key="-ENDGAME-",
            ),
        ],
    ]


def get_w_high_scores():
    return sg.Window(
        "High Scores",
        get_layout_w_high_scores(),
        font=FONT_WINDOW_HIGH_SCORES,
        element_justification="c",
        text_justification="center",
        no_titlebar=True,
        margins=(1, 1),
        grab_anywhere=True,
    )
