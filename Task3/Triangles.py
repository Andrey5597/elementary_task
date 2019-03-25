import math


class Triangle:
    def __init__(self, name, length_a, length_b, length_c):
        self.name = name
        self.length_a = length_a
        self.length_b = length_b
        self.length_c = length_c
        self.valid = self._check_is_valid()
        self.half_perimeter = (self.length_a + self.length_b + self.length_c) / 2
        self.square = self._count_square()

    def _check_is_valid(self):
        if not (
                self.length_a + self.length_b > self.length_c or
                self.length_b + self.length_c > self.length_a or
                self.length_c + self.length_a > self.length_b
        ):
            raise ValueError('It is not a triangle')

    def _count_square(self):
        return math.sqrt(self.half_perimeter *
                         (self.half_perimeter - self.length_a) *
                         (self.half_perimeter - self.length_b) *
                         (self.half_perimeter - self.length_c))


if __name__ == '__main__':
    triangle_table = []
    while True:
        print('Enter parameters of your triangle: ')
        name, length_a, length_b, length_c = input("Name, Length A, Length B, LengthC : ").split()
        try:
            triangle_instance = Triangle(name, float(length_a), float(length_b), float(length_c))
        except ValueError:
            print('Incorrect value! You must pass Name(str) Length A(int), Length B(int), LengthC(int)')
            continue
        triangle_table.append(triangle_instance)

        question = input("Do you want to add another Triangle?: "
                         "Type 'Y' to continue or any key to show table and exit: ")
        assertion = ['YES', 'yes', 'Y', 'y']
        if question not in assertion:
            break

    if triangle_table:

        print("============= Triangles Table ===============")
        triangle_table.sort(key=lambda x: x.square, reverse=True)
        for n, t in enumerate(triangle_table):
            print(f'{n + 1}. [Triangle {t.name}]: {round(t.square, 2)} cm')
    else:
        print("Table of triangles is empty.")
