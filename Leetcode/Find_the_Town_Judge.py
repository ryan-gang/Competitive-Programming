from collections import defaultdict


class Solution:
    # Runtime: 773 ms, faster than 66.23%.
    # Memory Usage: 19 MB, less than 25.51%.
    # T : O(N), S : O(N)
    def findJudge(self, n: int, trust: list[list[int]]) -> int:
        """
        d -> person : [trusts, trusted_by] for judge this should be (0, n - 1)
        n - 1 other people excluding judge.
        """
        d: dict[int, list[int]] = defaultdict(lambda: [0, 0])

        if n == 1:
            return 1
            # This special case has to be handled, because input array is empty.

        for trusts, trusted in trust:
            d[trusts][0] += 1
            d[trusted][1] += 1

        for person in d:
            if d[person] == [0, n - 1]:
                return person

        return -1

    def findJudge1(self, N: int, trust: list[list[int]]) -> int:
        """
        Instead of keeping track of both trusts and trusted by, we can just track the diff of them
        both,think of it as a DAG, a judge will have no out degree and N in degrees.
        """
        count = [0] * (N + 1)
        for i, j in trust:
            count[i] -= 1
            count[j] += 1
        for i in range(1, N + 1):
            if count[i] == N - 1:
                return i
        return -1


if __name__ == "__main__":
    sol = Solution()
    assert sol.findJudge(n=3, trust=[[1, 3], [2, 3]]) == 3
    assert sol.findJudge(n=3, trust=[[1, 3], [2, 3], [3, 1]]) == -1
    assert sol.findJudge(n=1, trust=[]) == 1
