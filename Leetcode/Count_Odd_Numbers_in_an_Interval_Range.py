from math import ceil, floor


class Solution:
    # Runtime: 30 ms, faster than 76.46%.
    # Memory Usage: 13.8 MB, less than 50.4%.
    # T : O(1), S : O(1)
    def countOdds(self, low: int, high: int) -> int:
        if high % 2 and low % 2:
            out = floor((high - low - 1) / 2) + 2
        elif not high % 2 and not low % 2:
            out = ceil((high - low - 1) / 2)
        else:
            out = (high - low - 1) / 2 + 1

        return int(out)

    def countOdds1(self, low: int, high: int) -> int:
        """
        (high - low) // 2 is the number of odds between low + 1 and high.
        If low is odd, or high is odd. We need to add 1 to the answer.
        Can be better understood, by breaking this into a case by case basis.
        """
        out = ((high - low) // 2) + ((high % 2) or (low % 2))
        return int(out)

    def countOdds2(self, low: int, high: int) -> int:
        """
        Odds between 0 to high -> high + 1 // 2
        Odds between 0 to low - 1 -> low // 2
        """
        return (high + 1) // 2 - low // 2


if __name__ == "__main__":
    sol = Solution()
    assert sol.countOdds2(low=3, high=7) == 3
    assert sol.countOdds2(low=8, high=10) == 1
    assert sol.countOdds2(low=21, high=22) == 1
