from .utils import *


def get_score():
    return int(w_main["-SCORE-"].get().split()[-1])


def toggle_element_visibility(*captions):
    for capt in captions:
        element = w_main[capt]
        element.update(visible=not element.visible)


def cp_colors(cp):
    bar_colors = {
        0: (GREEN, RED),
        1: (YELLOW, GREEN),
        2: (BLUE, YELLOW),
        3: (ORANGE, BLUE),
        4: (YELLOW, ORANGE),
        5: (GREEN, YELLOW),
        6: (RED, GREEN),
        7: (BLUE, RED),
    }
    return bar_colors[(cp // 10) % (len(bar_colors) - 1)]


def get_bar(name, max, colors):
    return sg.ProgressBar(
        max,
        orientation="h",
        key=f"-{name}-",
        bar_color=colors,
        visible=False,
        size=(15, 20),
    )


layout_w_main = [
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
                        [sg.Text("Player", key="-USER-")],
                        [get_bar("CP-BAR", 10, (GREEN, RED))],
                    ]
                ),
                sg.Text(
                    "0", key="-TIMER-", visible=False, size=(6), justification="center"
                ),
                sg.Column(
                    [
                        [sg.Push(), sg.Text("Board")],
                        [get_bar("HP-BOARD", 81, (GREEN, RED))],
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
            sg.Text(
                "Combo - 0",
                key="-COMBO-",
                text_color=RED,
                visible=False,
            )
        ),
        sg.Push(),
        sg.Text("Score - 0", key="-SCORE-", text_color=YELLOW, visible=False),
    ],
    [
        sg.Frame(
            "Choose a difficulty.",
            [[sg.Button(f"{x}") for x in ("Easy", "Medium", "Hard")]],
            key="-FRAME-DIFFICULTY-",
            title_location="n",
        ),
        sg.Frame(
            "",
            [
                [
                    sg.Button(
                        " ",
                        size=(4, 2),
                        key=(x, y),
                        pad=(0, 0),
                        border_width=2,
                        font=FONT_SCORES,
                    )
                    for y in range(9)
                ]
                for x in range(9)
            ],
            key="-FRAME-BUTTONS-",
            title_location="n",
            visible=False,
        ),
    ],
    [
        sg.Text(
            "Thanks for the appreciation!",
            text_color=RED,
            key="-THANKS-",
            visible=False,
        )
    ],
    [
        sg.Button("Rate me", key="-RATE-"),
        sg.Push(),
        sg.pin(
            sg.Frame(
                "",
                [
                    [
                        sg.Image(
                            f"{path.dirname(__file__)}/../files/images/star.png",
                            key=f"{x}",
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
        sg.Button("High Scores", key="-HIGH-SCORES-"),
    ],
    [sg.Button("Instructions", key="-INSTRUCTIONS-")],
]

w_main = sg.Window(
    "Sudoku",
    layout_w_main,
    element_justification="c",
    font=FONT_MAIN,
    return_keyboard_events=True,
    use_default_focus=False,
)
