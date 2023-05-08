class Solution:
    # Runtime: 117 ms, faster than 23.28%.
    # Memory Usage: 16.7 MB, less than 5.3%.
    # T : O(N), S : O(1)
    def diagonalSum(self, mat: list[list[int]]) -> int:
        N, K, add = len(mat), len(mat) - 1, 0
        for i in range(N):
            # Add elements from primary diagonal (Top left to bottom right)
            add += mat[i][i]
            # Add elements from secondary diagonal (Top right to bottom left)
            add += mat[i][K - i]

        # In case of odd length array, middle element is added twice, so we
        # remove it once.
        if N % 2:
            add -= mat[N // 2][N // 2]

        return add


if __name__ == "__main__":
    sol = Solution()
    assert sol.diagonalSum(mat=[[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == 25
    assert sol.diagonalSum(mat=[[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]]) == 8
