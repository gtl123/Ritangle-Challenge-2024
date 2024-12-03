import math
from multiprocessing import Pool, Manager, cpu_count


class Crossword:
    def __init__(self):
        self.template = [["1", "2", " "],
                         [" ", "3", "4"],
                         ["5", " ", " "]]
        self.Crossword = [[0, 0, 0],
                          [0, 0, 0],
                          [0, 0, 0]]

    @staticmethod
    def is_prime(n):
        """Check if a number is prime."""
        if n <= 1:
            return False
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True

    @staticmethod
    def is_square(n):
        """Check if a number is a perfect square."""
        return n >= 0 and int(math.sqrt(n)) ** 2 == n

    @staticmethod
    def is_prime_multiple(a, b):
        """Check if a is divisible by b and the result is prime."""
        return b != 0 and a % b == 0 and Crossword.is_prime(a // b)

    def gv(self, clue):
        """Get the value from the grid based on a clue."""
        row, col = self.find_index(clue[0], self.template)
        if clue[1:] == "dn":
            digits = [self.Crossword[i][col] for i in range(row, len(self.Crossword)) if self.Crossword[i][col] != 0]
        else:
            digits = [self.Crossword[row][j] for j in range(col, len(self.Crossword[0])) if self.Crossword[row][j] != 0]
        return int("".join(map(str, digits))) if digits else 0

    def find_index(self, item, lst):
        """Find the index of the clue in the template."""
        for i, row in enumerate(lst):
            if item in row:
                return i, row.index(item)
        return None

    def is_valid(self):
        """Check the constraints on the grid."""
        try:
            # Apply only the most important constraints first (relaxed checking)
            constraints = [
                Crossword.is_prime_multiple(self.gv("1dn"), self.gv("4dn")),
                Crossword.is_square(self.gv("1ac")),
            ]
            # Apply stricter constraints only after grid is completely filled
            if self.is_filled():
                constraints += [
                    Crossword.is_square(sum(int(d) for d in str(self.gv("2dn")) if d.isdigit())),  # Sum of digits is square
                    Crossword.is_prime(int(str(self.gv("3ac"))[::-1])),  # Reversed value is prime
                ]
            return all(constraints)
        except ValueError:
            # Handle cases where gv() returns invalid numbers due to incomplete grid
            return False

    def is_filled(self):
        """Check if the crossword grid is completely filled."""
        for row in self.Crossword:
            if 0 in row:
                return False
        return True

    def get_next_variable(self):
        """Find the next empty cell to fill."""
        for i in range(3):
            for j in range(3):
                if self.Crossword[i][j] == 0:
                    return i, j
        return None

    def get_sorted_values(self, row, col):
        """Get sorted values for a cell."""
        return range(1, 10)  # All possible values from 1 to 9

    def backtracking_search(self, grid):
        """Solve the crossword using backtracking."""
        self.Crossword = grid
        empty_cell = self.get_next_variable()
        if not empty_cell:  # No empty cells left, solution found
            return True

        row, col = empty_cell
        for value in self.get_sorted_values(row, col):
            self.Crossword[row][col] = value
            if self.is_valid():
                if self.backtracking_search([row[:] for row in self.Crossword]):
                    return True
            self.Crossword[row][col] = 0  # Undo the move (backtrack)

        return False

    def parallel_solve(self):
        """Parallelized backtracking using multiprocessing."""
        initial_cell = self.get_next_variable()
        if not initial_cell:
            print("The crossword is already solved.")
            return

        row, col = initial_cell
        tasks = [(row, col, value) for value in self.get_sorted_values(row, col)]

        with Manager() as manager:
            solution = manager.list()  # Shared list to store the solution
            with Pool(cpu_count()) as pool:
                results = pool.map(self.worker, [(row, col, value, [row[:] for row in self.Crossword]) for value in range(1, 10)])

            # Check if any solution was found
            for result in results:
                if result:
                    print("Solution found:")
                    self.Crossword = result
                    self.print_crossword()
                    return

            print("No solution exists.")

    def worker(self, args):
        """Worker function for parallel processing."""
        row, col, value, grid = args
        Crossword_copy = Crossword()
        Crossword_copy.Crossword = [row[:] for row in grid]
        Crossword_copy.Crossword[row][col] = value

        if Crossword_copy.backtracking_search([row[:] for row in Crossword_copy.Crossword]):
            return Crossword_copy.Crossword  # Return the solution
        return None

    def print_crossword(self):
        """Print the current state of the crossword."""
        for row in self.Crossword:
            print(row)


if __name__ == "__main__":
    crossword_solver = Crossword()
    crossword_solver.parallel_solve()
