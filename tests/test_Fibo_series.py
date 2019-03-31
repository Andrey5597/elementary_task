#!/usr/bin/env python3

import unittest
from unittest import mock
from elemenrary_task.Task8 import Fibo_series as Fs
from unittest import TestCase


class TestFiboSequence(TestCase):
    def test_input_start_end(self):
        with mock.patch('builtins.input', return_value=90):
            self.assertEqual(Fs.input_start_end(), (90, 90))

    def test_create_list(self):
        args = [7, 90, Fs.fibo(), []]
        expected = [8, 13, 21, 34, 55, 89]
        self.assertEqual(Fs.create_list(*args), expected)


if __name__ == "__main__":
    unittest.main()
