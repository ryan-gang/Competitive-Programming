from audioop import add
from typing import List


# Runtime: 122 ms, faster than 58.52% of Python3 online submissions for Valid Sudoku.
# Memory Usage: 13.9 MB, less than 81.20% of Python3 online submissions for Valid Sudoku.
# class Solution:
def isValidSudoku(board: List[List[str]]) -> bool:
    seen: set = set()
    for i in range(len(board)):
        for j in range(len(board[i])):
            cell = board[i][j]
            row_index, col_index, sub_index = i, j, f"{i // 3}{j // 3}"
            if cell != ".":
                row_string = f"{cell} in row {row_index}"
                col_string = f"{cell} in col {col_index}"
                sub_string = f"{cell} in sub {sub_index}"
                if row_string in seen or col_string in seen or sub_string in seen:
                    return False
                else:
                    seen.update({row_string, col_string, sub_string})
    return True


board = [
    ["3", ".", "6", "5", ".", "8", "4", ".", "."],
    ["5", "2", ".", ".", ".", ".", ".", ".", "."],
    [".", "8", "7", ".", ".", ".", ".", "3", "1"],
    [".", ".", "3", ".", "1", ".", ".", "8", "."],
    ["9", ".", ".", "8", "6", "3", ".", ".", "5"],
    [".", "5", ".", ".", "9", ".", "6", ".", "."],
    ["1", "3", ".", ".", ".", ".", "2", "5", "."],
    [".", ".", ".", ".", ".", ".", ".", "7", "4"],
    [".", ".", "5", "2", ".", "6", "3", ".", "."],
]
# sol = Solution()
# print(sol.isValidSudoku(board))
all_digits = set([str(i) for i in range(1, len(board) + 1)])


def get_remaining_digits(BOARD: List[List], I: int, J: int) -> List:
    used_digits_row = set(board[I])
    used_digits_col = set([board[_][J] for _ in range(len(board))])
    used_digits = used_digits_row.union(used_digits_col)
    used_digits.discard(".")
    remaining_digits = all_digits.difference(used_digits)
    return list(remaining_digits)


def add_digit_to_board(BOARD: List[List], I: int, J: int) -> bool:
    if I >= len(BOARD) and J >= len(BOARD):
        return isValidSudoku(BOARD)
    elif I >= len(BOARD):
        add_digit_to_board(BOARD, 0, J + 1)
    elif J >= len(BOARD):
        add_digit_to_board(BOARD, I + 1, 0)

    if BOARD[I][J] != ".":
        add_digit_to_board(BOARD, I, J + 1)
        return True
    else:
        if not isValidSudoku(BOARD):
            return False
        else:
            digits = get_remaining_digits(BOARD, I, J)
            for digit in digits:
                BOARD[I][J] = digit
                if add_digit_to_board(BOARD, I, J + 1):
                    return True

    return False


for row in range(9):
    for col in range(9):
        add_digit_to_board(BOARD=board, I=row, J=col)


print(board)

# Ref : https://www.geeksforgeeks.org/sudoku-backtracking-7/
