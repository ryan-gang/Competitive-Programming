class Solution:
    # Runtime: 1287 ms, faster than 54.32%.
    # Memory Usage: 18.1 MB, less than 72.13%.
    # We fix one pointer, and then iterate the list using 2 pointers,
    # to get progressively closer to our target.
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        out: list[list[int]] = []

        n = len(nums)
        for left in range(0, n - 2):
            mid = left + 1
            right = n - 1
            if left > 0 and nums[left] == nums[left - 1]:
                # Ignoring duplicates
                continue
            while mid < right:
                curr_sum = nums[left] + nums[mid] + nums[right]
                if curr_sum < 0:
                    mid += 1
                elif curr_sum > 0:
                    right -= 1
                else:  # curr_sum == 0
                    out.append([nums[left], nums[mid], nums[right]])
                    while mid < right and nums[mid] == nums[mid + 1]:
                        # Ignoring duplicates
                        mid += 1
                    while mid < right and nums[right] == nums[right - 1]:
                        # Ignoring duplicates
                        right -= 1
                    mid += 1
                    right -= 1

        return out

    # Using a dict, we keep track of all the values in our list, and then
    # get the sum of all combinations of 2 elements taken together, and
    # see if its complement is there in the dict or not.
    def threeSum1(self, nums: list[int]) -> list[list[int]]:
        d = {val: idx for idx, val in enumerate(nums)}

        n = len(nums)
        res: set[tuple[int, int, int]] = set()
        for i in range(n):
            for j in range(i + 1, n):
                add = nums[i] + nums[j]
                if -add in d:
                    idx = d[-add]
                    if i != idx and j != idx:
                        values = sorted([nums[i], nums[j], -add])
                        res.add(tuple(values))  # type: ignore

        return list(res)  # type: ignore


if __name__ == "__main__":
    sol = Solution()
    assert sol.threeSum(nums=[-1, 0, 1, 2, -1, -4]) == [[-1, -1, 2], [-1, 0, 1]]
    assert sol.threeSum(nums=[0, 1, 1]) == []
    assert sol.threeSum(nums=[0, 0, 0]) == [[0, 0, 0]]
