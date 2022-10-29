from typing import List


class Solution:
    # WRONG ANSWER.
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        time = [(i, j) for i, j in zip(plantTime, growTime)]
        time.sort(key=lambda x: (-x[1], x[0]))  # desc growTime, asc plantTime
        plant = 0
        grow = 0
        for item in time:
            plant += item[0]
            grow += item[1]

        if grow > plant:
            return grow
        return plant + time[-1][1]

    # Runtime: 1913 ms, faster than 87.42% of Python3 online submissions.
    # Memory Usage: 41.1 MB, less than 10.97% of Python3 online submissions.
    # T : O(NLogN), S : O(N)
    def earliestFullBloom1(self, plantTime: List[int], growTime: List[int]) -> int:
        time = [(i, j) for i, j in zip(plantTime, growTime)]
        """
        First, we need to sort the arrays in descending order of growTime.
        The plants with longest growTimes, need to be planted first so that they
        get more time to grow (while the other trees are planted, and don't require
        extar time at the end.) If the growTime is same, we want the trees to be
        sorted in ascending order of plantTimes, again we want to give the trees
        max time to grow, while the other trees are planted.
        """
        time.sort(key=lambda x: (-x[1], x[0]))  # Desc growTime, Asc plantTime
        plant = result = 0
        """
        We keep 2 variables, plant and result, in plant we store our total time to
        plant all the trees, and result is the total time (upto ith tree in the ith
        iteration) to plant and grow the trees. And we store the max of these 2
        variables, because we need to keep the time where the tree has actually grown.
        """
        for item in time:
            plant += item[0]
            result = max(result, plant + item[1])

        return result


if __name__ == "__main__":
    sol = Solution()
    assert (
        sol.earliestFullBloom1(
            plantTime=[
                27,
                5,
                24,
                17,
                27,
                4,
                23,
                16,
                6,
                26,
                13,
                17,
                21,
                3,
                9,
                10,
                28,
                26,
                4,
                10,
                28,
                2,
            ],
            growTime=[
                26,
                9,
                14,
                17,
                6,
                14,
                23,
                24,
                11,
                6,
                27,
                14,
                13,
                1,
                15,
                5,
                12,
                15,
                23,
                27,
                28,
                12,
            ],
        )
        == 348
    )
