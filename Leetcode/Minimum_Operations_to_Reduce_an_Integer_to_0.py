class Solution:
    def minOperations(self, n: int) -> int:
        """
        Logic is simple. We consider the binary representation of n.
        If there is a lone "1" at the end. We can get rid of this "1" by subtracting 1 from n.
        So, we do that, and add 1 to our operations.
        But, if there is a contiguous segment of "1"s like "1111", we can add 1 to n,
        and exchange these 4 "1"s with only 1 "1". (Costing us only 1 operation.)
        After adding 1 to "1111", it becomes "10000". Now we can subtract the final "1",
        (Costing us another operation)
        So, initially what would have cost us 4 operations, to convert this to 0.
        We did in only 2 operations.

        To prove that this will always lead us to the optimal number of operations,
        we will see case by case.

        For "1", the optimal way to make this "0" is to subtract 2 ^ 0. (1 operation)
        If we try to add anything, it will inevitably become > 1 operation.
        For "11",
        We can subtract, "1" two times, and make this "0" in 2 operations.
        But, we can also add "1", making it "100", and then subtract "1" to make it 0.
        Still 2 operations.
        But the 2nd path (of adding "1") has the additional advantage of creating a domino effect.
        If n = "11011", if we try going the subtract path from the onset,
        it would cost 4 operations.
        But adding "1", n becomes "11100", (Costing 1 operation.)
        And now we can add another "1" to convert n to "100000". (Costing 1 operation).
        So our final cost in the addition path is 3, as compared to 4 through subtraction.
        So, for n = "11" also, the optimal way is to add "1" to the end.
        And, this benefit only becomes more pronounced for larger segments of contiguous "1"s.

        So, accordingly whenever we see contiguous segments of "1" of length >= 2, we add 1 to n,
        and increase our operations count. Else, if we have a single "1", we subtract the LSB,
        and add 1 to operations count. For "0" we do nothing.
        And finally to iterate over the entire binary representation of n, easily,
        we right shift bits, after we are finished with a bit.
        """
        # T : O(LogN), S : O(1)
        ops = 0
        while n > 0:
            if n & 3 == 3:
                ops += 1
                n += 1
            else:
                ops += n & 1
                n >>= 1

        return ops


if __name__ == "__main__":
    sol = Solution()
    assert sol.minOperations(n=54) == 3
    assert sol.minOperations(n=39) == 3
    assert sol.minOperations(n=7862) == 5
