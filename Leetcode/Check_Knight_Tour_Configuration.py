class Solution:
    # T : O(N), S : O(1), where N is the total number of cells in the grid.
    # For each cell, we run a loop of size 8. Atmost O(8N) computations.
    def checkValidGrid(self, grid: list[list[int]]) -> bool:
        """
        At every position, we compute all the possible next moves.
        And then see if the actual next move is in this possible moves.
        If it is, we update our current position to this, and continue this process.
        At the end we should have covered n*n positions.
        """
        n = len(grid)

        moves = [[2, 1], [2, -1], [-2, 1], [-2, -1], [1, 2], [1, -2], [-1, 2], [-1, -2]]

        pos: tuple[int, int] = (0, 0)  # Current position.
        move_num = 0  # Current move number.
        while (grid[pos[0]][pos[1]]) == move_num:
            move_num += 1
            for move in moves:  # For all 8 possible knight moves
                new_pos: tuple[int, int] = (
                    pos[0] + move[0],
                    pos[1] + move[1],
                )  # We calculate the next move
                if new_pos[0] < n and new_pos[0] >= 0 and new_pos[1] < n and new_pos[1] >= 0:
                    if (
                        grid[new_pos[0]][new_pos[1]] == move_num
                    ):  # If it is the actual move in the grid
                        pos = new_pos  # update our current position
        return move_num == (n * n)  # Finally the number of correct moves should be n * n

    # T : O(N * N), S : O(N * N), where N is the number of rows.
    def checkValidGrid1(self, grid: list[list[int]]) -> bool:
        """
        Create a dict of move number -> (x,y) in grid.
        Then validate the dict.
        For every move, the change in x and y has to be in range [1, 2]
        """
        index_dict: dict[int, list[int]] = {}
        rows, cols = len(grid), len(grid[0])

        for i in range(rows):
            for j in range(cols):
                index_dict[grid[i][j]] = [i, j]

        if index_dict[0] != [0, 0]:
            return False

        return self.validate(index_dict)

    def validate(self, d: dict[int, list[int]]) -> bool:
        for idx in range(len(d) - 1):
            x_diff = abs(d[idx + 1][0] - d[idx][0])
            y_diff = abs(d[idx + 1][1] - d[idx][1])
            if min(x_diff, y_diff) != 1 or max(x_diff, y_diff) != 2:
                return False
        return True
