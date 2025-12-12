#!/usr/bin/python3

import sys


def safe(board, row, col):
    for r, c in board:
        if c == col:
            return False
        if abs(r - row) == abs(c - col):
            return False
    return True

def boardd(n, row=0, board=None):
    if board is None:
        board = []
    if row == n:
        print(board)
        return
    for col in range(n):
        if safe(board, row, col):
            board.append([row, col])
            solve_nqueens(n, row + 1, board)
            board.pop()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if not type(sys.argv[1]) is int:
        print("N must be a number")
        sys.exit(1)
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)
    boardd(N)
