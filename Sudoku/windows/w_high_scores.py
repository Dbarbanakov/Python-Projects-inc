from .utils import *

from events_utils import read_score


def get_layout_w_high_scores():
    headings = (" ", "User", "  -- Score -- ", "Date")

    return [
        [
            sg.Frame(
                "@ High Scores @",
                [
                    [sg.Text(f"{x}", size=14, text_color=GREEN) for x in headings],
                    [
                        sg.Column(
                            [
                                [sg.Text(col.strip(), size=14) for col in row.split()]
                                for row in read_score()
                            ],
                        )
                    ],
                ],
                title_location="n",
                title_color=RED,
            )
        ],
        [
            sg.Button(
                "Confirm",
                bind_return_key=True,
                button_color=(RED, "black"),
                key="-ENDGAME-",
            ),
        ],
    ]


def get_w_high_scores():
    return sg.Window(
        "High Scores",
        get_layout_w_high_scores(),
        font=FONT_SCORES,
        element_justification="c",
        text_justification="center",
        no_titlebar=True,
        margins=(1, 1),
        grab_anywhere=True,
    )
