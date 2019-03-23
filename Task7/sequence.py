while True:
        try:
            end_number = int(input("Enter the number of the ending of the list: "))
            if end_number <= 0:
                print('Number should not be negative. Enter correct value')
                continue
            break
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
    print(sequence)


if __name__ == '__main__':
    create_list(end_number)
