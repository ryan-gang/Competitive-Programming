from typing import Dict, List


# Runtime: 1926 ms, faster than 42.02% of Python3 online submissions for Maximum Erasure Value.
# Memory Usage: 27.6 MB, less than 50.11% of Python3 online submissions for Maximum Erasure Value.
class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        start, end = 0, 0
        numSum = 0
        maxSum = 0
        d: Dict[int, int] = {}

        for i in range(len(nums)):
            val = nums[i]
            end += 1
            numSum += val
            if val in d and d[val] >= start:
                while start < d[val] + 1:
                    numSum -= nums[start]
                    start += 1
            d[val] = i
            maxSum = max(maxSum, numSum)

        return maxSum


# Sliding window method.
# Keep 2 pointers, which will tell us the start and end of the window (which in this case is the longest unique subarray).
# When we come across a value, we add that to our running Sum. And then check if this is already present in the subarray or not.
# If it is present : Then we have to bring our `start` pointer to the index after that number.
# We run a while loop until the start pointer is after that index, and remove all values from our running Sum.
# And at the end of each iteration in the loop, we add the current number and it's index to a hashmap. This is the one which will be used to keep track of numbers present before or after the start pointer.
# We also keep a track of the max value of our runnning Sum after every iteration.
