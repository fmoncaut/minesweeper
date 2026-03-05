"""This module implements the Minesweeper game."""

import random


class Minesweeper:
    def __init__(self, rows: int, cols: int, num_mines: int):
        self.rows = rows
        self.cols = cols
        self.num_mines = num_mines
        self.board = [["" for _ in range(cols)] for _ in range(rows)]
        self.mines = set()
        self.revealed = set()
        self.place_mines()

    def place_mines(self):
        """Randomly place mines on the board, updating adjacent cells with mine counts."""
        all_positions = [(r, c) for r in range(self.rows) for c in range(self.cols)]
        self.mines = set(random.sample(all_positions, self.num_mines))
        for r, c in self.mines:
            self.board[r][c] = "M"
            for dr in [-1, 0, 1]:
                for dc in [-1, 0, 1]:
                    nr, nc = r + dr, c + dc
                    if (
                        0 <= nr < self.rows
                        and 0 <= nc < self.cols
                        and (nr, nc) not in self.mines
                    ):
                        if self.board[nr][nc] == "":
                            self.board[nr][nc] = 0
                        self.board[nr][nc] += 1

    def reveal(self, row: int, col: int) -> str:
        """Reveal a cell on the board."""
        if (row, col) in self.mines:
            return "Game Over"
        self.revealed.add((row, col))
        if self.board[row][col] == 0:
            for dr in [-1, 0, 1]:
                for dc in [-1, 0, 1]:
                    nr, nc = row + dr, col + dc
                    if (
                        0 <= nr < self.rows
                        and 0 <= nc < self.cols
                        and (nr, nc) not in self.revealed
                    ):
                        self.reveal(nr, nc)
        return "Continue"

    def get_board(self) -> list:
        """Return the board as seen by the player (hidden cells are empty strings)."""
        visible_board = [["" for _ in range(self.cols)] for _ in range(self.rows)]
        for r in range(self.rows):
            for c in range(self.cols):
                if (r, c) in self.revealed:
                    visible_board[r][c] = self.board[r][c]
        return visible_board

    def is_winner(self) -> bool:
        """Check if the game has been won."""
        return len(self.revealed) == (self.rows * self.cols) - self.num_mines

    def restart(self) -> None:
        """Restart the game with the same parameters."""
        self.__init__(self.rows, self.cols, self.num_mines)
