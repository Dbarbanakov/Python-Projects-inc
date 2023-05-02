import PySimpleGUI as sg
from .uts import *


def get_layout_window_high_scores():
    text = ("User", " -- Score -- ", "Date")

    return [
        [
            sg.Frame(
                "@ High Scores @",
                [
                    [
                        sg.T(
                            f"{x}",
                            size=12,
                            text_color=color_green,
                            justification="center",
                        )
                        for x in text
                    ],
                    [
                        sg.Column(
                            [
                                [
                                    sg.T(col.strip(), size=12, justification="center")
                                    for col in row.split()
                                ]
                                for row in read_score()
                            ],
                        )
                    ],
                ],
                title_location="n",
                pad=20,
                title_color=color_red,
            )
        ],
        [sg.B("Agreed", bind_return_key=True)],
    ]


def get_window_high_scores():
    return sg.Window(
        "High Scores",
        get_layout_window_high_scores(),
        font=font_window_high_scores,
        element_justification="c",
        no_titlebar=True,
        margins=(1, 1),
    ).read(close=True)
