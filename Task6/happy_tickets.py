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
        ticket = '{:0{}}'.format(i, 6)
        if sum(map(int, (ticket[0]+ticket[2]+ticket[4]))) == sum(map(int, (ticket[1]+ticket[3]+ticket[5]))):
            counter += 1
    print(counter)


def moscow():
    counter = 0
    for i in range(1, 1000000):
        ticket = '{:0{}}'.format(i, 6)
        if sum(map(int, ticket[:3])) == sum(map(int, ticket[3:])):
            counter += 1
    print(counter)


if __name__ == '__main__':
    path = input("Enter the name of the file: ")
    key = read_file(path)
    if key == 'Peter':
        peter()
    elif key == 'Moscow':
        moscow()
    else:
        print('You must enter the name of the file in which '
              'must be one of two keys: "Moscow" or "Peter". '
              'Please make that file and try again')
