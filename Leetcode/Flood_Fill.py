from typing import List


class Solution:
    # Runtime: 84 ms, faster than 85.07% of Python3 online submissions.
    # Memory Usage: 14.1 MB, less than 31.78% of Python3 online submissions.
    # T : O(m*n), S : O(1)
    # Auxiliary space : O(m*n) -> recursion stack size.
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        self.image = image
        self.m = len(image)
        self.n = len(image[0])
        self.prev_color = self.image[sr][sc]
        if self.prev_color == color:
            return self.image
        self.fill(sr, sc, color)
        return self.image

    def fill(self, i, j, color):
        if self.image[i][j] == self.prev_color:
            self.image[i][j] = color
            if i < (self.m - 1):
                self.fill(i + 1, j, color)
            if i > 0:
                self.fill(i - 1, j, color)
            if j < (self.n - 1):
                self.fill(i, j + 1, color)
            if j > 0:
                self.fill(i, j - 1, color)
        return


sol = Solution()
print(sol.floodFill(image=[[1, 1, 1], [1, 1, 0], [1, 0, 1]], sr=1, sc=1, color=2))
