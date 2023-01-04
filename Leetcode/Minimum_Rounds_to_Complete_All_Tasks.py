from collections import Counter
from typing import List


class Solution:
    # Runtime: 1592 ms, faster than 49.35%.
    # Memory Usage: 31.3 MB, less than 8.69%.
    # T : O(N), S : O(N)
    def minimumRounds(self, tasks: List[int]) -> int:
        """
        Things to notice :
        Unless d[level] < 2, it will always be possible to break it into 2x + 3y form.
        We try exactly that.
        Keep subtracting 2 while it's not divisible by 3. If divisible by 3, divide it entirely.
        """
        rounds = 0
        d = Counter(tasks)
        for level in d:
            if d[level] < 2:
                return -1
            else:
                while d[level] % 3 != 0:
                    d[level] -= 2
                    rounds += 1
                if d[level] % 3 == 0:
                    rounds += d[level] // 3
        return rounds

    """
    Tasks with same difficulty level can be done together, in group of 2-tasks or 3-tasks.

    So we count the frequnce freq for each level.

    If freq = 1, not possible, return -1
    If freq = 2, needs one 2-tasks
    If freq = 3, needs one 3-tasks
    If freq = 3k, freq = 3 * k, needs k batchs.
    If freq = 3k + 1, freq = 3 * (k - 1) + 2 + 2, needs k + 1 batchs.
    If freq = 3k + 2, freq = 3 * k + 2, needs k + 1 batchs.

    To summarize, needs (freq + 2) / 3 batch,
    return the sum of (freq + 2) / 3 if it is possible.
    """

    def minimumRounds1(self, tasks):
        freq = Counter(tasks).values()
        return -1 if 1 in freq else sum((a + 2) // 3 for a in freq)


if __name__ == "__main__":
    sol = Solution()
    assert sol.minimumRounds(tasks=[2, 2, 3, 3, 2, 4, 4, 4, 4, 4]) == 4
    assert sol.minimumRounds(tasks=[2, 3, 3]) == -1
