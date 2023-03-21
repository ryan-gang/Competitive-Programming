from collections import defaultdict
import sys


class Solution:
    # Runtime: 1028 ms, faster than 23.70%.
    # Memory Usage: 32.3 MB, less than 92.95%.
    # T : O(N), S : O(N) ; In the worst case right and left pointer both will
    # traverse N indices. And d will hold all N vals.
    def minimumCardPickup(self, cards: list[int]) -> int:
        """
        Using two pointers, we increment the window until we find 2 cards.
        And then keep on reducing the window until we get the smallest viable window.
        """
        l, r, n, min_window = 0, 0, len(cards), sys.maxsize
        d: dict[int, int] = defaultdict(int)

        d[cards[l]] += 1
        while r < n - 1:
            r += 1
            d[cards[r]] += 1  # Add current val to dict.
            if d[cards[r]] > 1:  # If current val appears twice in dict.
                min_window = min(min_window, r - l + 1)  # Get the current length.
                while l < r and d[cards[r]] > 1:  # And try to shorten window.
                    # While shortening window, don't just put the condition as
                    # while l < r, in that case l WILL come to r - 1. We can't
                    # make the window shorter than our current shortest window.
                    # So, shorten only upto the index where the current shortest
                    # window started. (With the same value as card[r])
                    d[cards[l]] -= 1
                    l += 1
                    if d[cards[r]] > 1:
                        min_window = min(min_window, r - l + 1)
                        # If window still valid, get shorter length.
        return min_window if min_window < sys.maxsize else -1

    # Runtime: 837 ms, faster than 75.95%.
    # Memory Usage: 33.4 MB, less than 67.86%.
    # T : O(N), S : O(N)
    def minimumCardPickup1(self, cards: list[int]) -> int:
        """
        Further optimised approach.
        Instead of just counting the number of times a number is present in a
        window. We can keep track of the index where the number was seen LAST.
        And from the stored index, we can directly get the window size. And
        finally update the index with the current one (latest).
        """
        d: dict[int, int] = {}
        ans = sys.maxsize
        for i in range(len(cards)):
            if cards[i] in d:
                ans = min(ans, i - d[cards[i]] + 1)
            d[cards[i]] = i
        return ans if ans != sys.maxsize else -1


if __name__ == "__main__":
    sol = Solution()
    assert sol.minimumCardPickup1(cards=[3, 4, 2, 3, 4, 7]) == 4
    assert sol.minimumCardPickup1(cards=[1, 0, 5, 3]) == -1
    assert (
        sol.minimumCardPickup1(
            cards=[
                746,
                464,
                175,
                787,
                105,
                164,
                370,
                110,
                642,
                413,
                353,
                410,
                200,
                141,
                915,
                170,
                928,
                326,
                123,
                528,
                8,
                11,
                474,
                168,
                992,
                43,
                901,
                133,
                579,
                152,
                135,
                893,
                950,
                102,
                863,
                119,
                835,
                795,
                783,
                728,
                35,
                916,
                770,
                698,
                832,
                324,
                391,
                338,
                102,
                770,
                183,
                739,
                804,
                468,
                591,
                174,
                929,
                992,
                406,
                349,
                472,
                260,
                586,
                938,
                677,
                331,
                629,
                769,
                148,
                566,
                501,
                628,
                845,
                197,
                48,
                369,
                754,
                542,
                608,
                632,
                639,
                815,
                758,
                206,
                400,
                105,
                298,
                993,
                187,
                133,
                950,
                430,
                92,
                225,
                609,
                507,
                753,
                873,
                732,
                353,
                894,
                63,
                867,
                814,
                736,
                109,
                440,
                288,
                846,
                152,
                164,
                42,
                96,
                134,
                170,
                649,
                832,
                385,
                265,
                178,
                447,
                678,
                415,
                32,
                428,
                524,
                118,
                775,
                593,
                221,
                247,
                887,
                119,
                159,
                391,
                661,
                220,
                175,
                693,
                184,
                534,
                281,
                569,
                306,
                383,
                330,
                355,
                408,
                30,
                200,
                391,
                136,
                721,
                925,
            ]
        )
        == 8
    )
