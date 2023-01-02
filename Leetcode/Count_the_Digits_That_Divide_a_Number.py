class Solution:
    # Runtime: 37 ms, faster than 83.33%.
    # Memory Usage: 13.8 MB, less than 100%.
    # T : O(N), S : O(N)
    def countDigits(self, num: int) -> int:
        chars = [int(i) for i in str(num)]
        factors = [i for i in chars if num % i == 0]
        return len(factors)

    def countDigits1(self, num: int) -> int:
        return sum(1 if num % int(d) == 0 else 0 for d in str(num))
