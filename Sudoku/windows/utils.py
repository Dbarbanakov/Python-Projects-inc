import PySimpleGUI as sg
from os import path
from solution import *


# sudoku init

sudoku = Board()

# sudoku init


sg.theme("DarkBlack")

COLOR_RED = "#FF3300"
COLOR_GREEN = "#00b300"
COLOR_YELLOW = "#ffff66"
COLOR_ORANGE = "#ff9900"
COLOR_BLUE = "#99ccff"

FONT_WINDOW_LOADING = ("Ani", 12, "bold")
FONT_WINDOW_MAIN = ("Purisa", 12, "bold")
FONT_BOARD = ("Helvetica", 10, "bold")
FONT_WINDOW_HIGH_SCORES = ("FreeMono", 12, "bold")
