#!/usr/bin/env python3
import argparse
import os

description = '''                
        ================Chessboard================
           This program can be used in two ways.

1. Interactive mode. Required to run the program without 
   parameters. After launch you will be asked to enter the 
   width and height of the chessboard.  After entering 
   in case of admissibility of the entered parameters the 
   board will be displayed. This mode executes by default.
   If you want to quit type 'q' instead of width value. 

2. Run with parameters. To specify the parameters, enter 
   the following command: 'python3 chess.py -wb width -hb height'
   where "width" and "height" define size of the chessboard.

   '''

error_message = '\n \033[31m Incorrect value! Values should be positive integers. ' \
                    'Please try again.\033[0m \n'


def parse_cmdline_args(*args):
    parser = argparse.ArgumentParser(usage="Chess Board")
    parser.add_argument("-wb", help="The width of the board. "
                                    "Must be positive integers", type=int)
    parser.add_argument("-hb", help="The height of the board. "
                                    "Must be positive integers", type=int)
    args = parser.parse_args(*args)
    if args.wb and args.hb:
        return args.wb, args.hb


def input_values():
    while True:
        try:
            input_width = input("Enter the value of width of the board "
                                "or type 'q' to exit: ")
            if input_width == 'q':
                exit()
            input_height = input("Enter the value of height of the board: ")
            value_1 = int(input_width)
            value_2 = int(input_height)
            if value_1 <= 0 or value_2 <= 0:
                print(error_message)
                continue
            return value_1, value_2
        except ValueError:
            print(error_message)


class ChessBoard:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def create_board(self):
        board = ""
        for item in range(1, self.height + 1):
            for elem in range(item, self.width + item):
                if elem % 2 == 0:
                    board += " "
                else:
                    board += "*"
            board += "\n"
        return board[:-1]


def can_place_in_terminal_window(columns, lines, t_window_width,
                                 t_window_height):
    if lines <= t_window_height and columns <= t_window_width:
        return True


def choose_mode(result_from_parser):
    if result_from_parser is None:
        board_width, board_height = input_values()
    elif result_from_parser[0] <= 0 or result_from_parser[1] <= 0:
        print(error_message)
        board_width, board_height = input_values()
    else:
        board_width, board_height = result_from_parser
    return board_width, board_height


def main():
    print(description)
    terminal_window_size = os.get_terminal_size()
    t_window_width = terminal_window_size.columns
    t_window_height = terminal_window_size.lines
    result_from_parser = parse_cmdline_args()
    board_width, board_height = choose_mode(result_from_parser)
    while True:
        if can_place_in_terminal_window(board_width, board_height,
                                        t_window_width, t_window_height):
            break
        print(f'\n \033[94m Specified parameters exceed your console window size: '
              f'Max. params - width: {t_window_width} '
              f'height: {t_window_height} \033[0m \n ')
        board_width, board_height = input_values()

    board = ChessBoard(board_width, board_height).create_board()
    print(board)


if __name__ == '__main__':
    main()
