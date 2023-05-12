class Solution:
    # T : O(N), S : O(N)
    def mostPointsDP(self, questions: list[list[int]]) -> int:
        """
        For any given index `idx`, we can either solve the question or skip it.
        If we choose to solve it, our total score will be the score we get from
        this question, and the score from all other questions from idx + q[1]
        +1. If we choose to skip its just from idx + 1. As we can see dp[i] is
        the optimal points we get for questions i to n-1. And dp[i+1] is the
        optimal points we get for questions i+1 to n-1. Which is 1 question
        less. Or in short, dp[i] includes the question range for dp[i+1]. Also,
        in our dp formula, we need the later values for calculation of earlier
        indices, so we start from the back, and make our way to the front.
        """
        n = len(questions)
        dp = [0] * n

        for i in range(n - 1, -1, -1):  # Start from end.
            q = questions[i]
            solve, skip = q[0], 0  # Solve or skip current question
            if i + q[1] + 1 < n:  # If solved, next available question index
                solve += dp[i + q[1] + 1]
            if i + 1 < n:  # If skipped, next available q index
                skip += dp[i + 1]

            dp[i] = max(solve, skip)  # max of both scenarios.

        return dp[0]

    def mostPoints(self, questions: list[list[int]]) -> int:
        # Recursive approach with same logic, and formulas.
        # Extra stack space required.
        n = len(questions)
        dp = [0] * n

        def dfs(idx: int) -> int:
            if idx >= n:
                return 0
            if dp[idx]:
                return dp[idx]
            points, skip = questions[idx]

            # dp[i] = max(skip it, solve it)
            dp[idx] = max(dfs(idx + 1), points + dfs(idx + skip + 1))
            return dp[idx]

        return dfs(0)


if __name__ == "__main__":
    sol = Solution()
    assert sol.mostPointsDP(questions=[[3, 2], [4, 3], [4, 4], [2, 5]]) == 5
    assert sol.mostPointsDP(questions=[[1, 1], [2, 2], [3, 3], [4, 4], [5, 5]]) == 7
