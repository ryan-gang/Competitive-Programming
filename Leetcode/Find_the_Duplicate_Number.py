class Solution:
    # T : O(NLogN), S: O(N)
    # Binary search for N, such that numbers in `nums` lte it is equal to N.
    def findDuplicate(self, nums: list[int]) -> int:
        lo, hi = 1, len(nums) - 1
        while lo < hi:
            mid = (lo + hi) // 2
            count = self.get_count(nums, mid)
            if count > mid:
                hi = mid
            else:
                lo = mid + 1
        return lo

    def get_count(self, nums: list[int], val: int) -> int:
        count = 0
        for num in nums:
            if num <= val:
                count += 1
        return count

    # T : O(N), S : O(1).
    # Floyd's algorithm.
    # Same as Linked_List_Cycle_II.py.
    # But why use here : https://keithschwarz.com/interesting/code/?dir=find-duplicate.
    # We can think of the array as a function mapping from its indices to its values.
    # As there is a duplicate value, there must be 2 indices i & j such that
    # i != j and nums[i] == nums[j]. Given that there are no other dupes,
    # the function must be non repeating but with a cycle,
    # this cycle we need to find using FLoyd's algo.
    def findDuplicate1(self, nums: list[int]) -> int:
        slow = fast = 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        slow = 0
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return slow
