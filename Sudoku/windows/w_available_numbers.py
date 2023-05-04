import PySimpleGUI as sg
from .utils import *
from solution import *


def get_window_available_numbers(nums):
    return sg.Window(
        "",
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
                                button_color=(color_orange, color_blue),
                            )
                            for i in range(len(nums))
                        ]
                    ],
                    title_location="s",
                )
            ]
        ],
        return_keyboard_events=True,
        relative_location=(100, 0),
        grab_anywhere=True,
        keep_on_top=True,
        # modal=True,
        use_custom_titlebar=True,
        titlebar_background_color=color_orange,
    )
