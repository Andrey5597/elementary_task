#!/usr/bin/env python3

import unittest
from unittest import TestCase
from elemenrary_task.Task2.envelope import Envelope


class TestEnvelope(TestCase):

    def test_constructor(self):
        envelope = Envelope(7, 8)
        self.assertEqual((envelope.width, envelope.height), (7, 8))

    def test_less_than(self):
        envelope1 = Envelope(4, 7)
        envelope2 = Envelope(5, 18)
        self.assertLess(envelope1, envelope2)

    def test_greater_than(self):
        envelope1 = Envelope(20, 20)
        envelope2 = Envelope(5, 18)
        self.assertGreater(envelope2, envelope1)


if __name__ == '__main__':
    unittest.main()
