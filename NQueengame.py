import tkinter as tk
from tkinter import simpledialog

class NQueensGame:
    def __init__(self):
        self.current_level = 4  # Initial board size
        self.play_game()

    def play_game(self):
        while True:
            board = NQueensBoard(self.current_level)
            board.print_board()

            print("Place queens by entering row and column (e.g., '2 3'). Enter '-1 -1' to finish.")
            game_lost = False

            while True:
                user_input = self.get_user_input("Enter queen position (row column):")
                row, col = map(int, user_input.split())

                if row == -1 or col == -1:
                    if board.get_queens_placed() != self.current_level:
                        print("Invalid number of queens placed! You lost the game.")
                        game_lost = True
                    break

                if board.is_safe_to_add_queen(row, col):
                    board.place_queen(row, col)
                    print("Queen placed successfully!")
                else:
                    print("Invalid queen placement! You lost the game.")
                    game_lost = True
                    break

                board.print_board()

            if not game_lost:
                if board.get_queens_placed() == self.current_level:
                    print("Congratulations! You have successfully placed all the queens.")
                    self.current_level += 1  # Increase current level on win
                else:
                    print("Invalid number of queens placed! You lost the game.")
            else:
                print("Game Over. You lost.")

            print("Next level with board size", self.current_level)
            choice = input("Enter 'y' to continue or 'n' to quit: ")

            if choice.lower() == "n":
                break

    @staticmethod
    def get_user_input(prompt):
        user_input = simpledialog.askstring("User Input", prompt)
        return user_input if user_input is not None else ""


class NQueensBoard:
    def __init__(self, size):
        self.board = [[0] * size for _ in range(size)]
        self.queens_placed = 0

    def is_safe_to_add_queen(self, row, col):
        for i in range(row):
            if self.board[i][col] == 1:
                return False

        for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
            if self.board[i][j] == 1:
                return False

        for i, j in zip(range(row, -1, -1), range(col, len(self.board))):
            if self.board[i][j] == 1:
                return False

        return True

    def place_queen(self, row, col):
        self.board[row][col] = 1
        self.queens_placed += 1

    def print_board(self):
        print("Current Board:")
        for row in self.board:
            for cell in row:
                if cell == 1:
                    print("Q ", end="")
                else:
                    print(". ", end="")
            print()
        print()

    def get_queens_placed(self):
        return self.queens_placed


if __name__ == "__main__":
    NQueensGame()
