class Solution:
    # Runtime: 60 ms, faster than 84.21%.
    # Memory Usage: 14.1 MB, less than 33.52%.
    # T : O(N), S : O(1) (No extra space except output)
    def shuffle_ez(self, nums: list[int], n: int) -> list[int]:
        # Create a new output array, copy values from nums into their intended indices.
        out = [-1] * 2 * n

        for i in range(n):
            out[2 * i] = nums[i]
        for i in range(n, 2 * n):
            j = i - n
            out[2 * j + 1] = nums[i]

        return out

    # Runtime: 73 ms, faster than 32%.
    # Memory Usage: 14.1 MB, less than 33.52%.
    # T : O(N), S : O(1)
    def shuffle(self, nums: list[int], n: int) -> list[int]:
        # Ref : https://leetcode.com/problems/shuffle-the-array/solutions
        # /675956/in-place-o-n-time-o-1-space-with-explanation-analysis/
        # Inplace algorithm. Exploits the constraint of nums[i] < 1000.
        # As the max value of any number can be stored in at most 10 bits,
        # we can store 2 numbers inside a single int.
        # We do exactly this in the first pass.
        # [x1, x2, x3, y1, y2, y3] -> [x1, x2, x3, x1y1, x2y2, x3y3]
        # In the next pass we put the nums in their proper indices.
        x, y = n - 1, 2 * n - 1
        while x >= 0:
            nums[y] <<= 10
            nums[y] |= nums[x]
            y -= 1
            x -= 1

        x, yx = 0, n
        while x < 2 * n:
            nums[x] = nums[yx] & 1023
            nums[x + 1] = nums[yx] >> 10
            x += 2
            yx += 1

        return nums


if __name__ == "__main__":
    sol = Solution()
    assert sol.shuffle(nums=[1, 2, 3, 4, 4, 3, 2, 1], n=4) == [1, 4, 2, 3, 3, 2, 4, 1]
    assert sol.shuffle(nums=[1, 1, 2, 2], n=2) == [1, 2, 1, 2]
