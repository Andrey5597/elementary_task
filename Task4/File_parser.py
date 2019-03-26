import sys
from pathlib import Path

arguments = sys.argv

helpMessage = '''This program can work in two modes:
                1. Search and count matches. 
                        You need to enter 2 positional arguments: "file path"  "string for search and count"
                2. Search and rewrite matches. 
                        You need to enter 3 positional arguments: "file path" "string for search" "string for replace"
                '''


def file_parser(path, mode):

    if mode == 3:
        f = open(path)
        count = 0
        for characters in f:
            count += characters.count(arguments[2])
        f.close()
        return'{} matches found'.format(count)
    else:
        f = open(path)
        s = f.read()
        f.close()
        if arguments[2] in s:
            s = s.replace(arguments[2], arguments[3])
            f = open(path, "w")
            f.write(s)
            f.close()
            return "File text was changed!"
        else:
            return "There are no such string. " + helpMessage


def execution():
    if len(arguments) in (3, 4):
        file_path = arguments[1]
        if Path(file_path).is_file():
            print(file_parser(file_path, len(arguments)))
        else:
            print("There is no such file in that directory")
            print(helpMessage)
    else:
        print("You have entered wrong number of parameters. You need to pass 2 or 3.")
        print(helpMessage)


if __name__ == '__main__':
    execution()
