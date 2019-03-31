#!usr/bin/env python3

import unittest
from unittest.mock import patch, mock_open
from elemenrary_task.Task6 import happy_tickets as ht
from unittest import TestCase


class TestHappyTickets(TestCase):

    def test_read_file(self):
        with patch("builtins.open", mock_open(read_data="Moscow")) as mock_file:
            assert open("path/to/open").read() == "Moscow"
            mock_file.assert_called_with("path/to/open")

    def test_peter(self):
        self.assertEqual(ht.peter(), 55251)

    def test_moscow(self):
        self.assertEqual(ht.peter(), 55251)


if __name__ == '__main__':
    unittest.main()
