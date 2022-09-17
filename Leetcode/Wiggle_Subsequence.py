from typing import List


class Solution:
    # Runtime: 59 ms, faster than 46.46%..
    # Memory Usage: 13.9 MB, less than 77.55%...
    def wiggleMaxLength(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return 1
        else:
            # Length is *atleast* 3.
            dp = [0 for _ in range(len(nums))]
            dp[0] = 1
            prevSign = None
            # Initial previous Sign will be None.
            for i in range(1, len(nums)):
                # Iterating from 2nd element to the end.
                sign = self.getSign(nums[i - 1], nums[i])
                # Calculate current sign (from i-1 to i), and compare to prev sign.
                if sign == 0:
                    # If same value as prev element, then no way dp will increment.
                    dp[i] = dp[i - 1]
                    sign = prevSign
                    # Don't want to overwrite prevSign, so storing it in sign
                elif prevSign is None:
                    # If 2nd element in array, (prevSign is None) then add 1 to prev value.
                    # Also sign has to be != 0 which is satisfied in this block.
                    dp[i] = dp[i - 1] + 1
                elif sign == -1 * prevSign:
                    # sign and prevsign are reverse, increment dp
                    dp[i] = dp[i - 1] + 1
                else:
                    # sign and prevsign are same
                    dp[i] = dp[i - 1]
                prevSign = sign

            return dp[-1]

    def getSign(self, a: int, b: int) -> int:
        """
        Given 2 ints as param,
        what is the sign of the latter number - the earlier one.
        """
        if a == b:
            return 0
        else:
            return int((b - a) / abs(b - a))


nums = [1, 17, 5, 10, 13, 15, 10, 5, 16, 8]
nums = [0, 0, 0]  # 1
nums = [3, 3, 3, 2, 5]  # 3
