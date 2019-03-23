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
    ChessBoard(12, 4)
