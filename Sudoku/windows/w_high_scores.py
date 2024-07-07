from .utils import *

from events_utils import read_score


def get_layout_w_high_scores():
    """Returns a layout with lines from reading the high_scores file."""
    headings = (" ", "User", "  -- Score -- ", "Date")

    return [
        [
            sg.Frame(
                "@ High Scores @",
                [
                    [
                        sg.Text(f"{x}", size=14, text_color=singleton.green)
                        for x in headings
                    ],
                    [
                        sg.Column(
                            [
                                [sg.Text(col, size=14) for col in row.split()]
                                for row in read_score()
                            ],
                        )
                    ],
                ],
                title_location="n",
                title_color=singleton.red,
            )
        ],
        [
            sg.Button(
                "Confirm",
                bind_return_key=True,
                button_color=(singleton.red, "black"),
                key="-ENDGAME-",
            ),
        ],
    ]


def get_w_high_scores():
    return sg.Window(
        "High Scores",
        get_layout_w_high_scores(),
        font=singleton.font_scores,
        element_justification="c",
        text_justification="center",
        no_titlebar=True,
        margins=(1, 1),
        grab_anywhere=True,
    )
