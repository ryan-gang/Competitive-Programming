class Solution:
    # Runtime: 29 ms, faster than 94.78%.
    # Memory Usage: 13.8 MB, less than 97.34%.
    # T : O(N), S : O(1)
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        # Naive simulation. Can be done better, in O(1) time.
        out = 0
        while k > 0:
            if numOnes > 0:
                out += 1
                numOnes -= 1
                k -= 1
            elif numZeros > 0:
                numZeros -= 1
                k -= 1
            else:
                out -= 1
                numNegOnes -= 1
                k -= 1

        return out

    # Runtime: 41 ms, faster than 32.28%.
    # Memory Usage: 13.9 MB, less than 56.28%.
    # T : O(1), S : O(1)
    def kItemsWithMaximumSum1(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        # Constant time solution.
        ans = 0
        ans += min(k, numOnes)
        k -= min(k, numOnes)
        k -= min(k, numZeros)
        ans -= min(k, numNegOnes)
        return ans

    def kItemsWithMaximumSum2(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        # One liner, same logic.
        return min(k, numOnes) - max(0, k - numZeros - numOnes)
