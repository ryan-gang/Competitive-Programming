class Solution:
    # Runtime: 53 ms, faster than 10.33%.
    # Memory Usage: 16.3 MB, less than 68.57%.
    # T : O(LogA), S : O(1)
    def minFlips(self, a: int, b: int, c: int) -> int:
        flips = 0
        OR = a | b
        for i in range(32):  # Iterate over every bit
            mask = 1 << i  # Generate mask
            if mask & OR == mask & c:  # If c and OR have same bit continue
                continue
            if (mask & a == mask & b) and (mask & a == mask):
                # If c and OR don't have same bits and a and b have the same
                # bits and the bit is 1, then we need to flip both 1's to 0,
                # only in this case there will be an extra flip, all other cases
                # need a single flip.
                flips += 1
            flips += 1
        return flips

    def minFlipsEditorial1(self, a: int, b: int, c: int) -> int:
        answer = 0
        while a or b or c:
            if c & 1:  # bit of c is 1
                # Either one of a or b has to have a 1 bit
                answer += 0 if ((a & 1) or (b & 1)) else 1
            else:  # bit of c is 0
                # Both bits of a and b have to be 0
                answer += (a & 1) + (b & 1)
            a >>= 1
            b >>= 1
            c >>= 1
        return answer

    # In 3.10 or later
    def minFlipsEditorial2(self, a: int, b: int, c: int) -> int:
        # ^ gives the number of bits that are different between a | b and c.
        # But in the case where c bit is 0, and a, b both have 1 bits, we need an extra flip.
        # OR = a | b
        # DIFFERENT_BITS = OR ^ c
        # This case is (a & b) & DIFFERENT_BITS
        return ((a | b) ^ c).bit_count() + (a & b & ((a | b) ^ c)).bit_count()


if __name__ == "__main__":
    sol = Solution()
    assert sol.minFlips(a=2, b=6, c=5) == 3
    assert sol.minFlips(a=4, b=2, c=7) == 1
    assert sol.minFlips(a=1, b=2, c=3) == 0
