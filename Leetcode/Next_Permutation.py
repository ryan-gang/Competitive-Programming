class Solution:
    # Runtime: 48 ms, faster than 29.91%.
    # Memory Usage: 13.9 MB, less than 59.79%.
    # T : O(N), S : O(1)
    def nextPermutation(self, nums: list[int]) -> list[int]:
        """
        Ref : https://www.youtube.com/watch?v=JDOXKqF60RQ.
        1. Find the largest index k such that nums[k] < nums[k + 1]. If no such
           index exists, just reverse nums and get done.
        2. Find the largest index l > k such that nums[k] < nums[l].
        3. Swap nums[k] and nums[l].
        4. Reverse the sub-array nums[k + 1:].
        """
        n = len(nums)
        idx = -1
        for i in range(n - 2, -1, -1):
            if nums[i + 1] > nums[i]:
                idx = i
                break

        if idx == -1:
            nums.sort()
            return nums

        for i in range(n - 1, idx, -1):
            if nums[i] > nums[idx]:
                nums[i], nums[idx] = nums[idx], nums[i]
                break

        nums[idx + 1 :] = sorted(nums[idx + 1 :])
        print(nums)
        return nums


if __name__ == "__main__":
    sol = Solution()
    assert sol.nextPermutation(nums=[1, 2, 3, 4, 5, 6]) == [1, 2, 3, 4, 6, 5]
    assert sol.nextPermutation(nums=[2, 1, 5, 4, 3, 0, 0]) == [2, 3, 0, 0, 1, 4, 5]
    assert sol.nextPermutation(nums=[3, 2, 1]) == [1, 2, 3]
