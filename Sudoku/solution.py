from random import choice
from copy import deepcopy
from time import time


class Board:
    def __init__(self):
        self.board = [[0 for col in range(9)] for row in range(9)]
        self.progress_board = deepcopy(self.board)
        self.init_positions = set()
        self.opened_coords = list()

    def check_position(self, board, row, col, n):
        def check_row():
            return False if n in board[row] else True

        def check_column():
            return False if n in [board[i][col] for i in range(9)] else True

        def check_square():
            square = [
                [board[row // 3 * 3 + i][col // 3 * 3 + j] for j in range(3)]
                for i in range(3)
            ]

            return False if n in square else True

        return check_row() and check_column() and check_square()

    def get_free_position(self):
        for row in range(9):
            for col in range(9):
                if self.board[row][col] == 0:
                    return (row, col)
        return False

    def generate_random_coords(self, n):
        while len(self.init_positions) < n:
            self.init_positions.add(choice(range(81)))

        self.opened_coords = [(x // 9, x % 9) for x in self.init_positions]

    def fill_coords(self):
        for coord in self.opened_coords:
            row, col = coord

            num = choice(range(1, 10))

            while not self.check_position(self.board, row, col, num):
                num = choice(range(1, 10))

            self.board[row][col] = num

    def solution(self, endtime):
        if time() > endtime:
            print("Timeout")
            self.board = deepcopy(self.progress_board)
            self.generate_board()

        if self.get_free_position() == False:
            return True

        row, col = self.get_free_position()

        for i in range(1, 10):
            if self.check_position(self.board, row, col, i) == True:
                self.board[row][col] = i
                if self.solution(endtime):
                    return True
                self.board[row][col] = 0

        return False

    def generate_board(self):
        self.generate_random_coords(15)
        self.fill_coords()
        self.solution(time() + 5)

    def apply_difficulty(self, difficulty):
        difficulties = {
            "Easy": 30,
            "Medium": 25,
            "Hard": 20,
        }

        self.generate_random_coords(difficulties[difficulty])

        for coord in self.opened_coords:
            row, col = coord

            self.progress_board[row][col] = self.board[row][col]
