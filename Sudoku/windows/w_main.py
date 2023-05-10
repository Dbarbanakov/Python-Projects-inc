from .utils import *

bar_colors = {
    0: (color_green, color_red),
    1: (color_yellow, color_green),
    2: (color_blue, color_yellow),
    3: (color_orange, color_blue),
    4: (color_yellow, color_orange),
    5: (color_green, color_yellow),
    6: (color_red, color_green),
    7: (color_blue, color_red),
}


def update_score(conseq):
    update_value = 10 + conseq
    prev_score = int(window_main["-SCORE-"].get().split()[-1])
    current_score = prev_score + update_value
    window_main["-SCORE-"].update(f"Score - {current_score}")


def update_health_bar(window, hp):
    count = hp % 10
    colors = bar_colors[(hp // 10) % (len(bar_colors) - 1)]
    return window["-HEALTH-PLAYER-"].update(count, bar_color=colors)


def get_health_bar(name, max, colors):
    """Used for both Player's and Board's health bars."""
    return sg.ProgressBar(
        max,
        orientation="h",
        key=f"-HEALTH-{name}-",
        bar_color=colors,
        visible=False,
        size=(15, 20),
    )


layout_main = [
    [
        sg.vbottom(
            [
                sg.Image(
                    f"{path.dirname(__file__)}/../files/images/avatar_player.png",
                    key="-AVATAR-PLAYER-",
                    visible=False,
                ),
                sg.Column(
                    [
                        [sg.T("Player", key="-USER-")],
                        [get_health_bar("PLAYER", 10, (color_green, color_red))],
                    ]
                ),
                sg.Text(
                    "0", key="-TIMER-", visible=False, size=(6), justification="center"
                ),
                sg.Column(
                    [
                        [sg.Push(), sg.T("Board")],
                        [get_health_bar("BOARD", 81, (color_green, color_red))],
                    ]
                ),
                sg.Image(
                    f"{path.dirname(__file__)}/../files/images/avatar_board.png",
                    key="-AVATAR-BOARD-",
                    visible=False,
                ),
            ]
        ),
    ],
    [
        sg.pin(
            sg.T(
                "Consequence - 0",
                key="-CONSEQUENCES-",
                text_color=color_red,
                visible=False,
            )
        ),
        sg.Push(),
        sg.T("Score - 0", key="-SCORE-", text_color=color_yellow, visible=False),
    ],
    [
        sg.Frame(
            "Choose a difficulty.",
            [
                [
                    sg.B("Easy"),
                    sg.B("Medium"),
                    sg.B("Hard"),
                ]
            ],
            key="-FRAME-DIFFICULTY-",
            title_location="n",
        ),
        sg.Frame(
            "",
            [
                [
                    sg.B(
                        " ",
                        size=(4, 2),
                        key=(i, j),
                        pad=(0, 0),
                        border_width=2,
                        font=font_window_high_scores,
                    )
                    for j in range(9)
                ]
                for i in range(9)
            ],
            key="-FRAME-BUTTONS-",
            title_location="n",
            visible=False,
        ),
    ],
    [
        sg.T(
            "Thanks for the appreciation!",
            text_color=color_red,
            key="-THANKS-",
            visible=False,
        )
    ],
    [
        sg.B("Rate me", key="-RATE-"),
        sg.Push(),
        sg.pin(
            sg.Frame(
                "",
                [
                    [
                        sg.Image(
                            f"{path.dirname(__file__)}/../files/images/star.png",
                            key=f"star{x}",
                            visible=False,
                        )
                        for x in range(5)
                    ]
                ],
                key="-FRAME-STARS-",
                visible=False,
            )
        ),
        sg.Push(),
        sg.B("High Scores", key="-HIGH-SCORES-"),
    ],
    [sg.B("Instructions", key="-INSTRUCTIONS-", button_color=color_yellow)],
]

window_main = sg.Window(
    "Sudoku",
    layout_main,
    element_justification="c",
    font=font_window_main,
    return_keyboard_events=True,
    use_default_focus=False,
)
