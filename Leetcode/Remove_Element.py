from typing import List


class Solution:
    def removeElement1(self, nums: List[int], val: int) -> int:
        if not nums:
            return 0
        last = len(nums) - 1
        while nums[last] == val and last >= 0:
            last -= 1
        idx = 0
        while idx <= last:
            v = nums[idx]
            if v == val:
                nums[idx], nums[last] = nums[last], nums[idx]
                last -= 1
            idx += 1
        print(nums, nums[: last + 1])
        return last + 1

    # Runtime: 33 ms, faster than 89.65%.
    # Memory Usage: 13.9 MB, less than 13.16%.
    # T : O(N), S : O(1)
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        for idx, v in enumerate(nums):
            nums[k] = nums[idx]
            if v != val:
                k += 1

        return k

    def removeElement2(self, nums: List[int], val: int) -> int:
        slow = 0
        for fast in range(len(nums)):
            if nums[fast] != val:
                nums[slow], nums[fast] = nums[fast], nums[slow]
                slow += 1

        return slow


if __name__ == "__main__":
    sol = Solution()
    assert sol.removeElement(nums=[3, 2, 2, 3], val=3) == 2
    assert sol.removeElement(nums=[0, 1, 2, 2, 3, 0, 4, 2], val=2) == 5
    assert sol.removeElement(nums=[], val=0) == 0
    assert sol.removeElement(nums=[1], val=1) == 0
    assert sol.removeElement(nums=[2, 2, 3], val=2) == 1
