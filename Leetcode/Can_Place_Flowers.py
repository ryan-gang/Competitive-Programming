class Solution:
    # Runtime: 151 ms, faster than 98.73%.
    # Memory Usage: 14.4 MB, less than 20.94%.
    # T : O(N), S : O(1)
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        # Scan over the array, finding all possible plots for flowers, if the
        # empty plots >= n return True.
        i = flowers = 0
        while i < len(flowerbed):
            if flowerbed[i]:
                i += 2
            else:
                empty_left_plot = i == 0 or not flowerbed[i - 1]
                empty_right_plot = i == (len(flowerbed) - 1) or not flowerbed[i + 1]
                if empty_left_plot and empty_right_plot:
                    flowerbed[i] = 1
                    flowers += 1
                    if flowers >= n:
                        return True
                i += 1
        return flowers >= n


if __name__ == "__main__":
    sol = Solution()
    assert sol.canPlaceFlowers(flowerbed=[1, 0, 0, 0, 1], n=1)
    assert not sol.canPlaceFlowers(flowerbed=[1, 0, 0, 0, 1], n=2)
