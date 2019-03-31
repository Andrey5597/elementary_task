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


def parse_cmdline_args(*args):
    parser = argparse.ArgumentParser(usage="Task1 (Chess Board)")
    parser.add_argument("-wb", help="The width of the board. "
                                    "Must be prime positive number", type=int)
    parser.add_argument("-hb", help="The height of the board. "
                                    "Must be prime positive number", type=int)
    args = parser.parse_args(*args)
    if args.wb and args.hb:
        return args.wb, args.hb
    return None


def input_values():
    while True:
        try:
            input_width = int(input("Enter the value of width of the board: "))
            input_height = int(input("Enter the value of height of the board: "))
            if input_height <= 0 or input_width <= 0:
                print('Incorrect value! Values should be prime positive numbers')
                continue
            return input_width, input_height
        except ValueError:
            print('Incorrect value! Values should be prime positive numbers')
            continue


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
    if not lines > t_window_height or columns > t_window_width:
        return True


def choose_mode(result_from_parser):
    if result_from_parser is None:
        board_width, board_height = input_values()
    elif result_from_parser[0] <= 0 or result_from_parser[1] <= 0:
        print('Incorrect value! Values should be prime positive numbers')
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
        if not can_place_in_terminal_window(board_width, board_height,
                                            t_window_width, t_window_height):
            print(f'Specified parameters exceed your console window size: '
                  f'Max. params - width: {t_window_width} '
                  f'height: {t_window_height}')
            board_width, board_height = input_values()
            continue
        break

    board = ChessBoard(board_width, board_height).create_board()
    print(board)


if __name__ == '__main__':
    main()
