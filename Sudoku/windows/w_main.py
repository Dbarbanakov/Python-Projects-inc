from .utils import *


def toggle_element_visibility(*captions):
    for capt in captions:
        element = w_main[capt]
        element.update(visible=not element.visible)


def update_hp_bar(hp):
    bar_colors = {
        0: (COLOR_GREEN, COLOR_RED),
        1: (COLOR_YELLOW, COLOR_GREEN),
        2: (COLOR_BLUE, COLOR_YELLOW),
        3: (COLOR_ORANGE, COLOR_BLUE),
        4: (COLOR_YELLOW, COLOR_ORANGE),
        5: (COLOR_GREEN, COLOR_YELLOW),
        6: (COLOR_RED, COLOR_GREEN),
        7: (COLOR_BLUE, COLOR_RED),
    }

    count = hp % 10
    colors = bar_colors[(hp // 10) % (len(bar_colors) - 1)]
    return w_main["-HP-PLAYER-"].update(count, bar_color=colors)


def get_hp_bar(name, max, colors):
    return sg.ProgressBar(
        max,
        orientation="h",
        key=f"-HP-{name}-",
        bar_color=colors,
        visible=False,
        size=(15, 20),
    )


def update_score(combo):
    update_value = 10 + combo
    prev_score = int(w_main["-SCORE-"].get().split()[-1])
    current_score = prev_score + update_value
    w_main["-SCORE-"].update(f"Score - {current_score}")


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
                        [sg.T("Player", key="-USER-")],
                        [get_hp_bar("PLAYER", 10, (COLOR_GREEN, COLOR_RED))],
                    ]
                ),
                sg.Text(
                    "0", key="-TIMER-", visible=False, size=(6), justification="center"
                ),
                sg.Column(
                    [
                        [sg.Push(), sg.T("Board")],
                        [get_hp_bar("BOARD", 81, (COLOR_GREEN, COLOR_RED))],
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
                "Combo - 0",
                key="-COMBO-",
                text_color=COLOR_RED,
                visible=False,
            )
        ),
        sg.Push(),
        sg.T("Score - 0", key="-SCORE-", text_color=COLOR_YELLOW, visible=False),
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
                        font=FONT_WINDOW_HIGH_SCORES,
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
            text_color=COLOR_RED,
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
    [sg.B("Instructions", key="-INSTRUCTIONS-", button_color=COLOR_YELLOW)],
]

w_main = sg.Window(
    "Sudoku",
    layout_w_main,
    element_justification="c",
    font=FONT_WINDOW_MAIN,
    return_keyboard_events=True,
    use_default_focus=False,
)
