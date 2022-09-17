from typing import List


nums = [1, 2, 3, 4, 5]


class Solution:
    # Runtime: 391 ms, faster than 27.54%
    # Memory Usage: 22.4 MB, less than 17.40%
    # What if nums is [1] ? Code will break if len(nums) <= 3
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = 1
        forward = []
        for i in nums:
            prod *= i
            forward.append(prod)

        prod = 1
        backward = []
        for i in nums[::-1]:
            prod *= i
            backward.append(prod)
        backward = backward[::-1]

        out = [0 for _ in range(len(nums))]
        for i in range(1, (len(nums)) - 1):
            out[i] = forward[i - 1] * backward[i + 1]
        out[0] = backward[1]
        out[-1] = forward[-2]

        return out

    # Runtime: 252 ms, faster than 83.33%.
    # Memory Usage: 21.1 MB, less than 55.74%.
    def productExceptSelfO1Space(self, nums: List[int]) -> List[int]:
        out = [1 for _ in range(len(nums))]
        for i in range(1, len(nums)):
            out[i] = out[i - 1] * nums[i - 1]
        # Accumulating entire forward products array into out array.
        # out = [1,1,2,6,24]
        prod = 1
        for i in range(len(nums) - 2, -1, -1):
            prod *= nums[i + 1]
            out[i] = out[i] * prod
        # Multiplying the out array with the backwards product array,
        # where prod keeps the running product.

        return out

    # In one iteration.
    def productExceptSelfBetter(self, nums: List[int]) -> List[int]:
        ans, pre, suf = [1] * len(nums), 1, 1
        for i in range(len(nums)):
            ans[i] *= pre
            pre *= nums[i]
            # Pre will be equal to product of elements upto N-1,
            # while multiplying with Array[N]
            ans[-i - 1] *= suf
            # ith element from end is : nums[-i - 1])
            suf *= nums[-1 - i]

        return ans
