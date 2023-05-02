import PySimpleGUI as sg
from .uts import *
from solution import *

sudoku = Board()


def get_layout_window_available_numbers(nums):
    return [
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
    ]


def get_available_numbers(board, row, col):
    """Helper function for get_window_available_numbers()."""
    available_numbers = []

    for i in range(1, 10):
        if sudoku.check_position(board, row, col, i):
            available_numbers.append(i)

    return available_numbers


def get_window_available_numbers(nums):
    """Returns the window after clicking on an empty Board coord[x,y] with the available numbers to choose from."""
    return sg.Window(
        "Available Numbers:",
        get_layout_window_available_numbers(nums),
        no_titlebar=True,
        return_keyboard_events=True,
    ).read(close=True)
