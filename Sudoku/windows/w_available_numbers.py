import PySimpleGUI as sg
from .utils import *
from solution import *


def get_window_available_numbers(nums):
    return sg.Window(
        "Available Numbers:",
        [
            [
                sg.Frame(
                    " ----- ",
                    [
                        [
                            sg.B(
                                " ",
                                key=nums[i],
                                image_source=f"{os.path.dirname(__file__)}/../files/images/{nums[i]}.png",
                            )
                            for i in range(len(nums))
                        ]
                    ],
                    title_location="s",
                )
            ]
        ],
        no_titlebar=True,
        return_keyboard_events=True,
        relative_location=(100, 0),
    )
