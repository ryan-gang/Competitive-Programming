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
            # Our recursion loop check code will fail if this is true. Endless recursion hell.
            return self.image
        self.fill(sr, sc, color)
        return self.image

    def fill(self, i, j, color):
        # Here we have a check based on the array value, which helps to break recursion loops.
        # A -> B -> A -> B ...
        # If this check on prev_color was not present we would've had to pass a set of all the
        # computed on indices to the fill method and then check on that.
        if self.image[i][j] == self.prev_color:
            self.image[i][j] = color
            # Check boundary conditions before making the next call.
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
