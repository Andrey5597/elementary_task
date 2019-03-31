#!usr/bin/env/ python3
import unittest
from elemenrary_task.Task7 import sequence as s
from unittest import mock
from unittest import TestCase


class TestSequence(TestCase):
    def test_input_values(self):
        with mock.patch('builtins.input', return_value=120):
            self.assertEqual(s.input_values(), 120)

    def test_create_list(self):
        end_number = 465
        self.assertEqual(s.create_list(end_number),
                         '1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21')


if __name__ == '__main__':
    unittest.main()
