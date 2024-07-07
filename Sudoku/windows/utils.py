import PySimpleGUI as sg
from os import path
from solution import *


class Singleton:
    _self = None

    def __new__(cls):
        if cls._self is None:
            cls._self = super().__new__(cls)
        return cls._self

    def __init__(self):
        self.hp_board = 81
        self.cp = 10
        self.combo = 0
        # fonts
        self.font_main = ("Purisa", 12, "bold")
        self.font_load = ("Ani", 12, "bold")
        self.font_board = ("Helvetica", 10, "bold")
        self.font_scores = ("FreeMono", 12, "bold")
        # colors
        self.red = "#FF3300"
        self.green = "#00b300"
        self.yellow = "#ffff66"
        self.orange = "#ff9900"
        self.blue = "#99ccff"


singleton = Singleton()

# sudoku init

Sudoku = Board()

# sudoku init


sg.theme("DarkBlack")
