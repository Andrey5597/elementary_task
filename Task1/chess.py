#!/usr/bin/env python3
import argparse
import os

description = '''                
        ================Chessboard================
           This program can be used in two ways.

1. Interactive mode. Required to run the program without 
   parameters. After launch you will be asked to enter the 
   width and height of the chessboard.  After entering the 
   board will be displayed. This mode executes by default. 

2. Run with parameters. To specify the parameters, enter 
   the following command: python3 chess.py -wb width -hb height'
   where "width" and "height" define size of the chessboard.

   '''


def parse_cmdline_args():
    board_width = None
    parser = argparse.ArgumentParser(usage="Task1 (Chess Board)")
    parser.add_argument("-wb", help="The width of the board. "
                                    "Must be prime positive number", type=int)
    parser.add_argument("-hb", help="The height of the board. "
                                    "Must be prime positive number", type=int)
    args = parser.parse_args()
    if args.wb:
        board_width = args.wb
    if args.hb:
        board_height = args.hb
    else:
        return None
    return board_width, board_height


def input_values():
    while True:
        f_height = int(input("Enter the value of height of the board: "))
        f_width = int(input("Enter the value of width of the board: "))
        if f_height <= 0 or f_width <= 0:
            print('Values should be prime positive number')
            continue
        break
    return f_height, f_width


class ChessBoard:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def print_board(self):
        board = ""
        for item in range(1, self.height + 1):
            for elem in range(item, self.width + item):
                if elem % 2 == 0:
                    board += "  "
                else:
                    board += "* "
            board += "\n"
        return board[:-1]


def can_place_in_terminal_window(lines, columns, t_height, t_width):
    if lines > t_height or columns > t_width:
        return False
    return True


def choose_mode():
    if parse_cmdline_args() is None:
        board_width, board_height = input_values()
    else:
        board_width, board_height = parse_cmdline_args()
    return board_width, board_height


def main():
    print(description)
    while True:
        try:
            board_height, board_width = choose_mode()
            terminal_window_size = os.get_terminal_size()
            t_window_width = terminal_window_size.columns
            t_window_height = terminal_window_size.lines
            if not can_place_in_terminal_window(board_height, board_width,
                                                t_window_height, t_window_width):
                print(f'Specified parameters exceed your console window size: '
                      f'Max. params - height: {t_window_height} '
                      f'width: {t_window_width}')
                continue
            break
        except ValueError:
            print('Values should be prime positive number!')
            continue

    board = ChessBoard(board_width, board_height).print_board()
    print(board)


if __name__ == '__main__':
    main()
