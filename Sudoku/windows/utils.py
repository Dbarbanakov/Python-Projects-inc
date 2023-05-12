import PySimpleGUI as sg
from os import path
from solution import *


# sudoku init

Sudoku = Board()

# sudoku init


sg.theme("DarkBlack")

HP_BOARD = 81
CP = 10  # Combo Points
COMBO = 0

RED = "#FF3300"
GREEN = "#00b300"
YELLOW = "#ffff66"
ORANGE = "#ff9900"
BLUE = "#99ccff"

FONT_MAIN = ("Purisa", 12, "bold")
FONT_LOAD = ("Ani", 12, "bold")
FONT_BOARD = ("Helvetica", 10, "bold")
FONT_SCORES = ("FreeMono", 12, "bold")
