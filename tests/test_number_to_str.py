#!usr/bin/env Python3
import unittest
from unittest import mock
from elemenrary_task.Task5 import Number_to_string as nts
from unittest import TestCase


class TestNumberToString(TestCase):
    def test_say_number_negative(self):
        i = -5
        self.assertEqual(nts.say_number(i), 'negative five')

    def test_say_number_zero(self):
        i = 0
        self.assertEqual(nts.say_number(i), 'zero')

    def test_say_number_positive(self):
        i = 56
        self.assertEqual(nts.say_number(i), 'fifty six')

    def test_say_number_pos(self):
        i = 15
        self.assertEqual(nts._say_number_pos(i), 'fifteen')

    def test_say_number_pos_20_100(self):
        i = 50
        self.assertEqual(nts._say_number_pos(i), 'fifty')

    def test_say_number_pos_100_1000(self):
        i = 150
        self.assertEqual(nts._say_number_pos(i), 'one hundred fifty')

    def test_say_number_pos_1000_(self):
        i = 10500
        self.assertEqual(nts._say_number_pos(i), 'ten thousand five hundred')

    def test_nput_number(self):
        with mock.patch('builtins.input', return_value=5):
            self.assertEqual(nts.input_number(), 5)


if __name__ == '__main__':
    unittest.main()


