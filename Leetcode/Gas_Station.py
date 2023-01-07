from typing import List


class Solution:
    # Runtime: 700 ms, faster than 81.89%.
    # Memory Usage: 19.2 MB, less than 49.17%.
    # T : O(N), S : O(1)
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        """
        Things to keep in mind :
        If tank goes below 0, while traversing from A to Z, none of the points in
        between A to Z, is suitable to start from to reach Z.
        We need to start from Z + 1. So we set tank to 0, and start again.
        If we are sure, that an answer is present, we don't need to check the final
        conditions, like in the next implementation.
        """
        if sum(gas) < sum(cost):
            return -1
        start = tank = 0
        for idx in range(len((gas))):
            tank += gas[idx] - cost[idx]
            if tank < 0:
                start = idx + 1
                tank = 0
        return start

    def canCompleteCircuit1(self, gas: List[int], cost: List[int]) -> int:
        """
        Same as the first implementaion, but instead of a sum at the beginning,
        we do the check later. total_surplus contains the sum of the tank fills
        and cost, across the entire journey. So if total_surplus > 0, we can
        be sure that this is a feasible path.
        """
        n, total_surplus, surplus, start = len(gas), 0, 0, 0

        for i in range(n):
            total_surplus += gas[i] - cost[i]
            surplus += gas[i] - cost[i]
            if surplus < 0:
                surplus = 0
                start = i + 1
        return -1 if (total_surplus < 0) else start


if __name__ == "__main__":
    sol = Solution()
    assert sol.canCompleteCircuit(gas=[1, 2, 3, 4, 5], cost=[3, 4, 5, 1, 2]) == 3
    assert sol.canCompleteCircuit(gas=[2, 3, 4], cost=[3, 4, 3]) == -1
