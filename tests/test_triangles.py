#!usr/bin/env python3
import unittest
from unittest import TestCase
from elemenrary_task.Task3.Triangles import Triangle


class TestTriangles(TestCase):
    def test_constructor(self):
        triangle = Triangle('Red', 3, 4, 5)
        self.assertEqual((triangle.name, triangle.length_a,
                          triangle.length_b, triangle.length_c,
                          triangle.half_perimeter, triangle.square),
                         ('Red', 3, 4, 5, 6.0, 6.0))

    def test_check_is_valid(self):
        triangle = Triangle('Blue', 5, 6, 7)
        self.assertIsNone(triangle._check_is_valid())

    def test_count_square(self):
        triangle = Triangle('Red', 3, 4, 5)
        self.assertEqual((triangle._count_square()), 6.0)


if __name__ == '__main__':
    unittest.main()






