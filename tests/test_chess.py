#!/usr/bin/env python3
from elemenrary_task.Task1 import chess as cb
import unittest
from unittest import TestCase
from elemenrary_task.Task1.chess import ChessBoard
from unittest import mock


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

    def test_parse_cmdline_args(self):
        args = ('-wb', '3', '-hb', '7')
        self.assertEqual(cb.parse_cmdline_args(args), (3, 7))

    def test_parse_cmdline_args_0(self):
        args = ()
        self.assertIsNone(cb.parse_cmdline_args(args))

    def test_choose_mode_1(self):
        args = (6, 9)
        self.assertEqual(cb.choose_mode(args), (6, 9))

    def test_input_values(self):
        with mock.patch('builtins.input', return_value="2"):
            self.assertEqual(cb.input_values(), (2, 2))


if __name__ == '__main__':
    unittest.main()
