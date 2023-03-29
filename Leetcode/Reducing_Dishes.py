class Solution:
    # Runtime: 46 ms, faster than 58.23%.
    # Memory Usage: 13.8 MB, less than 98.73%.
    # T : O(NLogN), S : O(1)
    def maxSatisfaction(self, satisfaction: list[int]) -> int:
        """
        To maximize the satisfaction, we need to cook the highest satisfaction
        dishes at the very end, as the satisfaction is being multiplied by time
        passed, we keep on adding all dishes from highest satisfaction to lowest
        satisfaction, as long as our total increases. When we add a dish (at the
        beginning), our total satisfaction increases by the total satisfaction
        on the right + this dish's satisfaction. So until this dish goes very
        negative we continue. And if negative we break.
        If we have chosen 3 dishes : N-2, N-1, N.
        Our total satisfaction is 1 * (N-2) + 2 * (N-1) + 3 * N.
        Now if we want to add N - 3.
        Our total satisfaction will become 1 * (N-3) + 2 * (N-2) + 3 * (N - 1) + 4 * N.
        which is an increase of (N-3 + N-2 + N-1 + N), as long as this is
        positive, we can keep adding dishes. Greedily.
        """
        satisfaction.sort()
        n = len(satisfaction)
        suffix_sum = total_satisfaction = 0
        for i in range(n - 1, -1, -1):
            val = satisfaction[i]
            diff = suffix_sum + val
            if diff < 0:
                break
            suffix_sum += val
            total_satisfaction += suffix_sum

        return total_satisfaction


if __name__ == "__main__":
    sol = Solution()
    assert sol.maxSatisfaction(satisfaction=[-1, -8, 0, 5, -9]) == 14
    assert sol.maxSatisfaction(satisfaction=[4, 3, 2]) == 20
    assert sol.maxSatisfaction(satisfaction=[-1, -4, -5]) == 0
