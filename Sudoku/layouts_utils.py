import PySimpleGUI as sg
import os
from scores import *


# Colors and Fonts

color_red = "#FF3300"
color_green = "#00b300"

font_window_loading = ("Ani", 12, "bold")
font_window_main = ("Purisa", 12, "bold")
font_board = ("Helvetica", 10, "bold")
font_window_high_scores = ("FreeMono", 12, "bold")

# Colors and Fonts


def get_pics_from_nums(nums):
    """Helper function for get_layout_window_available_numbers()."""
    pics = []
    for i in range(len(nums)):
        pics.append(
            sg.B(
                " ",
                key=nums[i],
                image_source=f"{os.path.dirname(__file__)}/files/images/{nums[i]}.png",
            )
        )
    return pics


def get_layout_window_available_numbers(nums):
    return [[sg.Frame(" ----- ", [get_pics_from_nums(nums)], title_location="s")]]


def col_high_scores():
    """Helper function for get_layout_window_high_scores()."""
    return sg.Column(
        [[sg.T(col.strip(), size=12) for col in row.split()] for row in read_score()],
        element_justification="left",
    )


def get_layout_window_high_scores():
    text = ("     User", " -- Score -- ", "       Date")

    return [
        [
            sg.Frame(
                "@ High Scores @",
                [
                    [sg.T(f"{x}", size=12, text_color=color_green) for x in text],
                    [col_high_scores()],
                ],
                title_location="n",
                pad=20,
                title_color=color_red,
            )
        ],
        [sg.B("Agreed", bind_return_key=True)],
    ]


def get_health_bar(name, max, colors):
    """Used for both Player's and Board's health bars."""
    return sg.ProgressBar(
        max,
        orientation="h",
        key=f"-HEALTH-{name}-",
        bar_color=colors,
        visible=False,
        size=(20, 20),
    )


def get_button(i, j, text=" "):
    """Used to place a button for each coord[x,y] on the Board."""
    return sg.B(
        text,
        size=(4, 2),
        key=(i, j),
        pad=(0, 0),
        border_width=2,
        font=font_window_high_scores,
    )
