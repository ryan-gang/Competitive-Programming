from collections import defaultdict


class Solution:
    """If the string contains a char, an even number of times, it can be symmetrically put in both
    sides of the centre. But if the char is present an odd number of times, we can't put it
    anywhere except the centre. So we are constrained by the number of chars occurring
    an odd number of times."""

    def canPermutePalindrome(self, s: str) -> bool:
        d = defaultdict(int)
        odd_count = 0
        seen = set()
        for char in s:
            d[char] += 1
            if d[char] % 2:
                odd_count += 1
                seen.add(char)
            if d[char] % 2 == 0 and char in seen:
                odd_count -= 1

        print(odd_count)
        return odd_count < 2


if __name__ == "__main__":
    sol = Solution()
    assert sol.canPermutePalindrome("bbccddaaaffffeeeeeeddeedede")
