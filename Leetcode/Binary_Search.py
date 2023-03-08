class Solution:
    # Runtime: 251 ms, faster than 94.37% of Python3 online submissions.
    # Memory Usage: 15.4 MB, less than 97.68% of Python3 online submissions.
    # T : O(logN), S : O(1)
    def search(self, nums: list[int], target: int) -> int:
        lo, hi = 0, len(nums) - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                hi = mid - 1
            else:
                lo = mid + 1

        return -1

    # Runtime: 240 ms, faster than 82.49%.
    # Memory Usage: 15.5 MB, less than 59.87%.
    # T : O(LogN), S : O(1)
    # Using the template @ StarterCode.binary_search
    def search1(self, nums: list[int], target: int) -> int:
        def condition(array: list[int], value: int):
            return array[value] >= target

        def binary_search(array: list[int]) -> int:
            left, right = 0, len(array)
            while left < right:
                mid = left + (right - left) // 2
                if condition(array, mid):
                    right = mid
                else:
                    left = mid + 1
            return left

        idx = binary_search(nums)
        return idx if idx >= 0 and idx < len(nums) and nums[idx] == target else -1


if __name__ == "__main__":
    sol = Solution()
    assert sol.search1(nums=[-1, 0, 3, 5, 9, 12], target=9) == 4
    assert sol.search1(nums=[-1, 0, 3, 5, 9, 12], target=13) == -1
