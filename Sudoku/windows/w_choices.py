from .utils import *


def get_w_choices(nums):
    """Returns a window with images, corresponding to the nums passed as an argument."""
    return sg.Window(
        "",
        [
            [
                sg.Frame(
                    " ----- ",
                    [
                        [
                            sg.Button(
                                " ",
                                key=nums[i],
                                image_source=f"{path.dirname(__file__)}/../files/images/{nums[i]}.png",
                                button_color=(ORANGE, BLUE),
                            )
                            for i in range(len(nums))
                        ]
                    ],
                    title_location="s",
                )
            ]
        ],
        return_keyboard_events=True,
        relative_location=(100, -160),
        grab_anywhere=True,
        modal=True,
        use_custom_titlebar=True,
        titlebar_background_color=ORANGE,
    )
