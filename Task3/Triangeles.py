import math


class Triangle:
    def __init__(self, name, length_a, length_b, length_c):
        self.name = name
        self.length_a = length_a
        self.length_b = length_b
        self.length_c = length_c
        self.valid = self._check_is_valid()
        if self.valid:
            self.half_perimeter = (self.length_a + self.length_b + self.length_c) / 2
            self.square = self._count_square()
        else:
            print('It is not a triangle')

    def _check_is_valid(self):
        if (
                self.length_a + self.length_b > self.length_c and
                self.length_b + self.length_c > self.length_a and
                self.length_c + self.length_a > self.length_b
        ):
            return True
        return False

    def _count_square(self):
        return math.sqrt(self.half_perimeter *
                         (self.half_perimeter - self.length_a) *
                         (self.half_perimeter - self.length_b) *
                         (self.half_perimeter - self.length_c))


if __name__ == '__main__':
    triangle_table = []
    while True:
        print('Enter parameters of your triangle: ')
        try:
            name, length_a, length_b, length_c = input("Name, Length A, Length B, LengthC : ").split()
            triangle_instance = Triangle(name, length_a, length_b, length_c)
        except ValueError:
            print('Incorrect value')
            continue
        else:
            triangle_table.append(triangle_instance)
        question = input("Do you want to add another Triangle? [Y/N]: ")
        assertion = ['YES', 'yes', 'Y', 'y']
        if question not in assertion:
            break

    if triangle_table:

        print("============= Triangles Table ===============")
        for triangle in triangle_table:
            print(triangle.name, triangle.square)
