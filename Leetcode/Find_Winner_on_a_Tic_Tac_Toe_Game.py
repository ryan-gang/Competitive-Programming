class Solution:
    """
    Create a 2 x 8 size grid, to store the number of moves in a particular row,
    column and diagonal for each player.
    """

    # Runtime: 41 ms, faster than 80%.
    # Memory Usage: 16.4 MB, less than 38.24%.
    # T : O(1), S : O(1)
    # Both moves and sol are constrained.
    def tictactoe(self, moves: list[list[int]]) -> str:
        sol = [[0 for _ in range(8)] for __ in range(2)]  # (3 x R + 3 x C + 2 x Diagonal) x 2 Users
        # sol[0] for "0" and sol[1] for "X"
        for idx, move in enumerate(moves):
            r, c = move
            if idx % 2:  # odd moves are : "O"
                sol[0][r] += 1
                sol[0][3 + c] += 1
                sol[0][6] += r == c  # top left to bottom right diagonal
                sol[0][7] += r + c == 2  # top right to bottom left diagonal
            else:  # even moves are : "X"
                sol[1][r] += 1
                sol[1][3 + c] += 1
                sol[1][6] += r == c
                sol[1][7] += r + c == 2

        print(sol)
        if len(list(filter(lambda x: x >= 3, sol[0]))) > 0:
            return "B"
        elif len(list(filter(lambda x: x >= 3, sol[1]))) > 0:
            return "A"
        elif (len(moves)) < 9:
            return "Pending"
        else:
            return "Draw"


if __name__ == "__main__":
    sol = Solution()
    assert (
        sol.tictactoe([[0, 0], [1, 1], [2, 0], [1, 0], [1, 2], [2, 1], [0, 1], [0, 2], [2, 2]])
    ) == "Draw"
