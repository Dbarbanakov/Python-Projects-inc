import copy

maze1 = [
    [" ", " ", "*", "*", " ", " ", "*", " "],
    [" ", " ", " ", " ", "*", " ", " ", " "],
    [" ", "*", "*", " ", " ", " ", "*", "*"],
    [" ", " ", " ", "*", "*", " ", " ", " "],
    [" ", "*", " ", " ", "*", " ", "*", " "],
    [" ", " ", "*", " ", " ", " ", "*", " "],
    ["*", " ", "*", "*", "*", "*", "*", " "],
    [" ", " ", " ", " ", " ", " ", " ", "e"],
]
maze2 = [
    [" ", "*", "*", "*", "*"],
    [" ", " ", " ", " ", " "],
    [" ", " ", " ", "*", " "],
    ["*", "*", "*", "*", " "],
    ["*", "*", "*", "*", "e"],
]


class FindPath:
    def __init__(self, lab):
        self.labyrinth = copy.deepcopy(lab)
        self.routes = list()
        self.height = len(self.labyrinth)
        self.length = len(self.labyrinth[0])

    def print_lab(self, labyrinth):
        """Prints the labyrinth (routed or not.)"""
        print("--" + "-" * 2 * self.height)
        for i in range(self.height):
            print("-", end="")
            for j in range(self.length):
                print(labyrinth[i][j], end=" ")
            print("-", end="")
            print()
        print("--" + "-" * 2 * self.length)
        print("Printing current route finished.")
        print()

    def find_route(self, h=0, l=0, direction=""):
        """Finds all possible routes from start(labyrinth[0][0] to end(labyrinth[n-1][n-1]).)"""
        if h < 0 or h >= self.height or l < 0 or l >= self.length:
            return
        if self.labyrinth[h][l] == "e":
            self.routes.append(direction)

        if self.labyrinth[h][l] == " ":
            self.labyrinth[h][l] = "v"

            self.find_route(h + 1, l, direction + "D")  #  Down
            self.find_route(h - 1, l, direction + "U")  #  Up
            self.find_route(h, l + 1, direction + "R")  #  Right
            self.find_route(h, l - 1, direction + "L")  #  Left

            self.labyrinth[h][l] = " "

    def print_routes(self):
        """Prints all routes."""
        if not self.routes:
            raise IOError("Please run a function to find all possible routes first.")

        for x in self.routes:
            temp = copy.deepcopy(self.labyrinth)

            row = 0
            col = 0
            step = 1
            for y in x:
                if y == "R":
                    col += 1
                if y == "L":
                    col -= 1
                if y == "U":
                    row -= 1
                if y == "D":
                    row += 1

                temp[row][col] = step
                step += 1
            print(f"Printing route - {x} ...")
            self.print_lab(temp)


# lab = FindPath(maze1)
# lab.print_lab(maze1)
# lab.find_route()
# lab.print_route()
lab2 = FindPath(maze2)
lab2.print_lab(maze2)
lab2.find_route()
lab2.print_routes()
