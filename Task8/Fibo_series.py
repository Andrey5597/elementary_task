#!/usr/bin/env python3

help_message = 'This program can build a list of Fibonacci ' \
               'series elements which are within specified limits'


def input_start_end():
    while True:
        try:
            start = int(input("Enter the number of the beginning of the list: "))
            end = int(input("Enter the number of the ending of the list: "))
            if start <= 0 or end <= 0:
                print('Number should not be negative. Enter correct value')
                continue
            return start, end
        except ValueError:
            print('Incorrect format! You should pass integer numbers')
            continue


def fibo():
    fib_1, fib_2 = 0, 1
    while True:
        yield fib_1
        fib_1, fib_2 = fib_2, fib_1 + fib_2


def create_list(list_start, list_end, fibo_series_generator, result_list):
    while True:
        fibo_element = next(fibo_series_generator)
        if fibo_element >= list_end:
            break
        elif fibo_element >= list_start:
            result_list.append(fibo_element)
    return result_list


def main():
    print(help_message)
    fibo_series_generator = fibo()
    result_list = []
    start, end = input_start_end()
    print(create_list(start, end, fibo_series_generator, result_list))


if __name__ == '__main__':
    main()
