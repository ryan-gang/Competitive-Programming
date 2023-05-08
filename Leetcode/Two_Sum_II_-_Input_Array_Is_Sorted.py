class Solution:
    # Runtime: 120 ms, faster than 99.64%.
    # Memory Usage: 14.9 MB, less than 88.68%.
    # T : O(N), S : O(1)
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        # Two Pointers. Start from both ends, and keep on updating indices based on the sum.
        lo, hi = 0, len(numbers) - 1
        while lo <= hi:
            current_sum = numbers[lo] + numbers[hi]
            if current_sum == target:
                break
            elif current_sum > target:
                # reduce sum, hi has to come down.
                hi -= 1
            else:
                # increase sum, increase lo.
                lo += 1
        return [lo + 1, hi + 1]

    # T : O(N), S : O(N)
    def twoSumDict(self, numbers: list[int], target: int) -> list[int]:
        # Keep all values in a hashmap, directly try to access required value.
        d = {}
        out: list[int] = []
        for i, num in enumerate(numbers):
            if target - num in d:
                out = [d[target - num] + 1, i + 1]
                break
            d[num] = i

        return out

    # T : O(NLogN), S : O(1)
    def twoSumBinSearch(self, numbers: list[int], target: int) -> list[int]:
        # For every value in array, try to search for the required value in the
        # rest of the array.
        def binary_search(nums: list[int], val: int, lo: int, hi: int):
            while lo < hi:
                mid = (lo + hi) // 2
                if nums[mid] >= val:
                    hi = mid
                else:
                    lo = mid + 1
            return lo

        out = []
        for i, num in enumerate(numbers):
            idx = binary_search(numbers, target - num, i + 1, len(numbers) - 1)
            if idx < len(numbers) and numbers[idx] == target - num:
                out = [i + 1, idx + 1]
                break
        return out


if __name__ == "__main__":
    sol = Solution()
    assert sol.twoSum(numbers=[2, 7, 11, 15], target=9) == [1, 2]
    assert sol.twoSum(numbers=[2, 3, 4], target=6) == [1, 3]
    assert sol.twoSum(numbers=[-1, 0], target=-1) == [1, 2]
    assert sol.twoSum(numbers=[-2, -1, 0, 1, 2, 7, 8], target=5) == [1, 6]
