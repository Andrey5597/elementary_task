#!/usr/bin/env python3

from elemenrary_task.Task1 import chess as cb
import unittest
from unittest import TestCase
from elemenrary_task.Task1.chess import ChessBoard


class TestChessBoard(TestCase):

    def test_can_place_in_terminal_window_true(self):
        args = [5, 6, 8, 9]
        self.assertTrue(cb.can_place_in_terminal_window(*args))

    def test_constructor(self):
        board = ChessBoard(10, 15)
        self.assertEqual((board.width, board.height), (10, 15))

    def test_print_board(self):
        board = ChessBoard(6, 3)
        self.assertEqual(board.create_board(),
                         '* * * \n'
                         ' * * *\n'
                         '* * * ')


if __name__ == '__main__':
    unittest.main()
