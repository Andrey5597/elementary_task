#!usr/bin/env python3

help_message = 'This program can show list of numbers which square less then entered value'


def input_values():
    while True:
        try:
            end_number = int(input("Enter the number of the ending of the list: "))
            if end_number <= 0:
                print('Number should not be negative. Enter correct value')
                continue
            return end_number
        except ValueError:
            print('Incorrect format! You should pass numbers')
            continue


def create_list(sq_number):
    sequence = ''
    number = 1
    while True:
        if number**2 < sq_number:
            sequence += str(number) + ','
            number += 1
        else:
            break
    return sequence[0:-1]


def main():
    print(help_message)
    end_number = input_values()
    print(create_list(end_number))


if __name__ == '__main__':
    main()
