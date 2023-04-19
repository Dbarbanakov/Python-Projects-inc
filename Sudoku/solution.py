import random, copy


class Board:
    def __init__(self):
        self.board = [[0 for x in range(9)] for j in range(9)]
        self.progress_board = copy.deepcopy(self.board)
        self.opened_positions = list()

    def print_board(self):
        """Prints the Sudoku board."""
        for i in range(9):
            for j in range(9):
                print(self.board[i][j], end=" ")
            print()
        print()

    def create_progress_board(self):
        """Creates a 2d list containing the numbers discovered by the player while the solution is running."""
        for x in self.opened_positions:
            row, col = x
            self.progress_board[row][col] = self.board[row][col]

    def get_random_positions(self, n):
        """Takes n(int) as an input and returns a list of unique coords as a tuple from (0,0) to (8,8) -
        (positions in the sudpku board) included."""
        choices = [x for x in range(81)]
        numbers = []

        for i in range(n):
            num = random.choice(choices)
            choices.remove(num)
            numbers.append((num // 9, num % 9))

        # numbers.sort()

        if self.opened_positions:
            self.opened_positions.clear()

        self.opened_positions = numbers
        return numbers

    def generate_random_numbers(self, n=10):
        """Fills the board with n random numbers from 1 to 9,
        which follow the rules of the game.
        Helps for a random board generation each time the game is ran.
        """
        numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

        positions = self.get_random_positions(n)

        for x in positions:
            row, col = x
            num = random.choice(numbers)

            while True:
                if self.check_position(self.board, row, col, num):
                    self.board[row][col] = num
                    break
                num = random.choice(numbers)

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

    def solution(self):
        """Checks for a solution of the current board and return True if there is such."""
        if self.get_free_position() == False:
            return True

        current_row, current_col = self.get_free_position()

        for i in range(1, 10):
            if self.check_position(self.board, current_row, current_col, i) == True:
                self.board[current_row][current_col] = i
                if self.solution():
                    return True
                self.board[current_row][current_col] = 0
        return False

    def get_solution(self):
        """If there is a solution to the board - prints it."""

        self.generate_random_numbers()
        self.solution()

    def generate_sudoku(self, difficulty):
        """Takes difficulty as an input and reveals a random number of positions on the board,
        easy - 30, medium-25, hard - 20.
        """
        # self.get_solution()
        if difficulty == "Easy":
            n = 30
        elif difficulty == "Medium":
            n = 25
        elif difficulty == "Hard":
            n = 20
        else:
            raise IOError("Choose between - easy, medium or hard difficulties please.")

        self.get_random_positions(n)
        self.create_progress_board()
