#!usr/bin/env/python3

help_message = 'This program can count quantity of happy tickets in two ways' \
               '("Moscow" and "Peter"). You can specify the way by typing it ' \
               'in text file'


def read_file(file):
    try:
        f = open(file, "r")
        s = f.read()
        s = s.strip()
        f.close()
        return s
    except FileNotFoundError:
        print('No such file in that directory')


def peter():
    counter = 0
    for i in range(1, 1000000):
        ticket = '{:06}'.format(i)
        if sum(map(int, (ticket[0]+ticket[2]+ticket[4]))) == \
                sum(map(int, (ticket[1]+ticket[3]+ticket[5]))):
            counter += 1
    return counter


def moscow():
    counter = 0
    for i in range(1, 1000000):
        ticket = '{:06}'.format(i)
        if sum(map(int, ticket[:3])) == sum(map(int, ticket[3:])):
            counter += 1
    return counter


def input_file_name():
    path = input("Enter the name of the file: ")
    key = read_file(path)
    if key == 'Peter':
        return 'Peter'
    elif key == 'Moscow':
        return 'Moscow'
    else:
        print('You must enter the name of the file in which '
              'must be one of two keys: "Moscow" or "Peter". '
              'Please make that file and try again.')


def main():
    print(help_message)
    mode = input_file_name()
    if mode == "Peter":
        print(peter())
    elif mode == "Moscow":
        print(moscow())


if __name__ == '__main__':
    main()
