while True:
        try:
            start = int(input("Enter the number of the beginning of the list: "))
            end = int(input("Enter the number of the ending of the list: "))
            if start <= 0 or end <= 0:
                print('Number should not be negative. Enter correct value')
                continue
            break
        except ValueError:
            print('Incorrect format! You should pass numbers')
            continue


def fibo():
    fib_1, fib_2 = 0, 1
    while True:
        yield fib_1
        fib_1, fib_2 = fib_2, fib_1 + fib_2


fibo_series_generator = fibo()
result_list = []


def create_list(list_start, list_end):
    while True:
        fibo_element = next(fibo_series_generator)
        if fibo_element >= list_end:
            break
        elif fibo_element >= list_start:
            result_list.append(fibo_element)

    print(result_list)


if __name__ == '__main__':
    create_list(start, end)