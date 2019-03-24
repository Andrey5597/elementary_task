import argparse

board_width = 0
board_height = 0

description = '''This program can be used in two ways. 
                 1. Interactive input. Required to run the program without parameters. 
                    After launch you will be asked to enter the width and height of the chessboard. 
                    After entering the board will be displayed. 
                 2. Run with parameters. To specify the parameters, enter the following command: 
                    'python3 chess.py --width w --height h'
                    where "w" is the width and "h" is the height of the chessboard.'''
print(description)

parser = argparse.ArgumentParser(prog="Task1 (Chess Board", usage=description)
parser.add_argument("--width", help="The width of the board. Must be prime positive number", type=int)
parser.add_argument("--height", help="   The height of the board. Must be prime positive number", type=int)
args = parser.parse_args()
if args.width:
    board_width = args.width
if args.height:
    board_height = args.height


def input_values(f_width, f_height):
    while True:
        try:
            if f_height <= 0 or f_width <= 0:
                f_height = int(input("Enter the value of height of the board: "))
                f_width = int(input("Enter the value of width of the board: "))
                if f_height <= 0 or f_width <= 0:
                    print('Value should be prime positive number')
                continue
            break
        except ValueError:
            print('Incorrect format! You must enter prime positive number.')
            continue
    return f_width, f_height


class ChessBoard:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.print_board()

    def print_board(self):
        board = ""
        for item in range(1, self.height + 1):
            for elem in range(item, self.width + item):
                if elem % 2 == 0:
                    board += " "
                else:
                    board += "*"
            board += "\n"
        print(board[:-1])


if __name__ == '__main__':
    board_width, board_height = input_values(board_width, board_height)
    ChessBoard(board_width, board_height)
