class Envelope:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __lt__(self, other):
        if (self.width < other.width and self.height < other.height or
                self.width < other.height and self.height < other.width):
            return True
        return False

    def __gt__(self, other):
        if (self.width > other.width and self.height > other.height or
                self.width > other.height and self.height > other.width):
            return False
        return True


def comparison():

    while True:
        try:
            a = float(input('Enter width of first envelope :'))
            b = float(input('Enter height of first envelope :'))
            c = float(input('Enter width of second envelope :'))
            d = float(input('Enter height of second envelope :'))
            if a <= 0 or b <= 0 or c <= 0 or d <= 0:
                print('The side of envelope should not be negative. Enter correct value')
                continue
        except ValueError:
            print('Incorrect format! You should pass numbers')
            continue

        first = Envelope(a, b)
        second = Envelope(c, d)
        if first < second:
            print('First envelope can Value should be positivebe puted in second')
        elif second > first:
            print('Second envelope can be puted in first')
        else:
            print('It can not be done')

        question = str(input('Do you want to continue?'))
        assertion = ['Yes', 'yes', 'y']

        if question not in assertion:
            break


if __name__ == '__main__':
    comparison()