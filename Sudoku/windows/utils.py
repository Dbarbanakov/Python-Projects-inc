import PySimpleGUI as sg
from os import path
from solution import *


# sudoku init

sudoku = Board()

# sudoku init


sg.theme("DarkBlack")

color_red = "#FF3300"
color_green = "#00b300"
color_yellow = "#ffff66"
color_orange = "#ff9900"
color_blue = "#99ccff"

font_window_loading = ("Ani", 12, "bold")
font_window_main = ("Purisa", 12, "bold")
font_board = ("Helvetica", 10, "bold")
font_window_high_scores = ("FreeMono", 12, "bold")
