from random import choice
from copy import deepcopy
from time import time


class Board:
    def __init__(self):
        self.board = [[0 for x in range(9)] for j in range(9)]
        self.progress_board = deepcopy(self.board)
        self.opened_positions = list()

    def check_row(self, board, row, n):
        """Returns True if n is not present in the current row."""

        for x in board[row]:
            if n == x:
                return False
        return True

    def check_column(self, board, col, n):
        """Returns True if n is not present in the current column."""

        for i in range(9):
            if n == board[i][col]:
                return False
        return True

    def check_square(self, board, row, col, n):
        """Returns True if n is not present in the current 3x3 square."""

        row_range = row - row % 3
        col_range = col - col % 3

        for i in range(3):
            for j in range(3):
                if n == board[i + row_range][j + col_range]:
                    return False
        return True

    def check_position(self, board, row, col, n):
        """
        Returns True if the current position on the board is suitable for n.
        n is not in the current - row, column and square.
        """

        return (
            self.check_column(board, col, n)
            and self.check_row(board, row, n)
            and self.check_square(board, row, col, n)
        )

    def get_free_position(self):
        """Checks for a free position, return tuple(row,col) or False.."""

        for i in range(9):
            for j in range(9):
                if self.board[i][j] == 0:
                    return (i, j)
        return False

    def get_random_coords(self, n):
        """Returns a list with n tuples with random coords(0-8, 0-8)."""
        coords = list()
        numbers = set()

        while len(numbers) < n:
            numbers.add(choice(range(81)))

        for num in numbers:
            coords.append((num // 9, num % 9))

        return coords

    def generate_random_numbers(self, n=15):
        """Generates n random numbers on the empty board applying the rules."""

        coords = self.get_random_coords(n)

        for coord in coords:
            choices = list()

            row, col = coord

            for i in range(1, 10):
                if self.check_position(self.board, row, col, i):
                    choices.append(i)

            num = choice(choices)
            self.board[row][col] = num

    def create_progress_board(self, n):
        """Opens n positions on the board, after the difficulty is selected."""

        coords = self.get_random_coords(n)

        for coord in coords:
            self.opened_positions.append(coord)

            row, col = coord

            self.progress_board[row][col] = self.board[row][col]

    def solution(self, endtime):
        """Checks for a solution of the current board and return True if there is such.
        endtime is the amount of time the recursion process should run before resetting itself with new RNG.
        """

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
        """Generates random numbers then goes for a solution with a timeout of 5 seconds on it."""

        self.generate_random_numbers()
        self.solution(time() + 5)

    def apply_difficulty(self, difficulty):
        """Takes difficulty as an input and reveals a random number of positions on the board,
        easy - 30, medium-25, hard - 20.
        """

        difficulties = {
            "Easy": 30,
            "Medium": 25,
            "Hard": 20,
        }

        self.create_progress_board(difficulties[difficulty])
