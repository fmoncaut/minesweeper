# tests/test_minesweeper.py
import pytest

import src.minesweeper as minesweeper


def test_module_exists():
    assert minesweeper


def test_place_mines():
    game = minesweeper.Minesweeper(3, 3, 2)
    assert len(game.mines) == 2
    for row, col in game.mines:
        assert 0 <= row < 3
        assert 0 <= col < 3


def test_reveal():
    import random

    random.seed(0)
    game = minesweeper.Minesweeper(3, 3, 2)
    result = game.reveal(0, 0)
    assert result in ["Continue", "Game Over"]
    if result == "Continue":
        assert (0, 0) in game.revealed
    random.seed(0)
    game2 = minesweeper.Minesweeper(3, 3, 2)
    mine_row, mine_col = next(iter(game2.mines))
    result2 = game2.reveal(mine_row, mine_col)
    assert result2 == "Game Over"


def test_get_board():
    game = minesweeper.Minesweeper(3, 3, 2)
    board = game.get_board()

    # C'est bien une liste
    assert isinstance(board, list)
    # Elle a 3 lignes
    assert len(board) == 3
    # Chaque ligne a 3 colonnes
    assert len(board[0]) == 3
    # Les mines sont marquées "M"
    for r, c in game.mines:
        assert board[r][c] == "M"


def test_is_winner():
    import random

    random.seed(0)
    game = minesweeper.Minesweeper(3, 3, 2)

    # Au départ, pas encore gagné
    assert game.is_winner() == False

    # On révèle toutes les cases sans mine
    for r in range(3):
        for c in range(3):
            if (r, c) not in game.mines:
                game.reveal(r, c)

    # Maintenant on a gagné
    assert game.is_winner() == True
