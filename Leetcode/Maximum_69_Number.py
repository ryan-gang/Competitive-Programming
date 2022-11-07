class Solution:
    # Runtime: 49 ms, faster than 71.19% of Python3 online submissions.
    # Memory Usage: 13.9 MB, less than 9.69% of Python3 online submissions.
    # T : O(N), S : O(N)
    # Using a lot of extra space, instead of which we can compute directly on num.
    def maximum69Number(self, num: int) -> int:
        nums = list(str(num))
        for idx, val in enumerate(nums):
            if val == "6":
                nums[idx] = "9"
                return int("".join(nums))
        return num

    # Runtime: 60 ms, faster than 32.91% of Python3 online submissions.
    # Memory Usage: 13.8 MB, less than 54.69% of Python3 online submissions.
    # T : O(N), S : O(1)
    def maximum69Number1(self, num: int) -> int:
        place, max_place, number = 1, 0, num
        while num > 0:
            if num % 10 == 6:
                max_place = max(max_place, place)
            num //= 10
            place += 1

        return (number + 3 * (10 ** (max_place - 1))) if max_place else number


sol = Solution()
assert sol.maximum69Number1(9669) == 9969
assert sol.maximum69Number1(9996) == 9999
assert sol.maximum69Number1(9999) == 9999
assert sol.maximum69Number1(6) == 9
