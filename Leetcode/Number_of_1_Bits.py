class Solution:
    # Runtime: 42 ms, faster than 71.15%.
    # Memory Usage: 13.7 MB, less than 94.77%.
    # T : O(N), S: O(1)
    def hammingWeight(self, n: int) -> int:
        return bin(n).count("1")

    # Runtime: 52 ms, faster than 43.20%.
    # Memory Usage: 13.8 MB, less than 94.77%.
    # T : O(N), S: O(1)
    def hammingWeightBit(self, n: int) -> int:
        count = 0
        while n:
            # If last bit is 1, count += 1
            # n = n // 2
            count += n & 1
            n = n >> 1

        return count
