from functools import cache
from typing import List


class Solution:
    """
    We recursively try to find the best score.
    At every index we have 2 choice, take player, don't take player.
    We can always not take player.
    But can take player only if it doesn't create a conflict.
    """

    # TLE.
    def bestTeamScoreTLE(self, scores: List[int], ages: List[int]) -> int:
        arr = sorted(list(zip(ages, scores)))
        n = len(arr)
        max_score = [0]

        @cache
        def recurse(idx: int, prev: int, score: int):
            if idx == n:
                max_score[0] = max(score, max_score[0])
                return
            if prev < 0 or arr[idx][1] >= arr[prev][1]:
                recurse(idx + 1, idx, score + arr[idx][1])

            recurse(idx + 1, prev, score)

        recurse(0, -1, 0)
        return max_score[0]

    # Runtime: 1982 ms, faster than 63.83%.
    # Memory Usage: 14.3 MB, less than 22.70%.
    # T : O(N^2), S : O(N)
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        """
        We sort the zipped array based on ages.
        Then the problem essentially boils down to find the Longest Increasing Subsequence
        on the scores array. Because the age conflict is taken care of due to sorting.
        """
        players = sorted(list(zip(ages, scores)))
        n = len(players)

        ans = 0
        dp = [0] * n

        for i in range(n):
            score = players[i][1]
            dp[i] = score
            for j in range(i):
                if players[i][1] >= players[j][1]:
                    dp[i] = max(dp[i], dp[j] + score)
            ans = max(ans, dp[i])

        return ans


if __name__ == "__main__":
    sol = Solution()
    assert (
        sol.bestTeamScore(
            scores=[
                564,
                915,
                436,
                927,
                784,
                205,
                186,
                992,
                518,
                467,
                264,
                180,
                528,
                594,
                557,
                462,
                667,
                856,
                104,
                911,
                960,
                176,
                382,
                96,
                153,
                685,
                359,
                370,
                623,
                480,
                213,
                180,
                881,
                333,
                658,
                964,
                367,
                261,
                758,
                822,
                790,
                904,
                246,
                441,
                97,
                938,
                202,
                434,
                88,
                24,
                881,
                147,
                439,
                260,
                47,
                27,
                39,
                79,
                751,
                758,
                493,
                950,
                94,
                224,
                769,
            ],
            ages=[
                6,
                92,
                61,
                16,
                66,
                19,
                63,
                57,
                6,
                29,
                17,
                30,
                67,
                57,
                89,
                88,
                4,
                78,
                29,
                36,
                18,
                17,
                41,
                70,
                5,
                52,
                4,
                71,
                35,
                57,
                46,
                85,
                21,
                45,
                58,
                54,
                45,
                58,
                93,
                67,
                59,
                25,
                58,
                11,
                95,
                79,
                94,
                81,
                85,
                50,
                29,
                93,
                3,
                29,
                21,
                27,
                6,
                70,
                24,
                58,
                96,
                65,
                4,
                49,
                73,
            ],
        )
        == 7484
    )
