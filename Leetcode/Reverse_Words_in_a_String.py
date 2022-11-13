import re
from typing import List


class Solution:
    # Runtime: 66 ms, faster than 39.98% of Python3 online submissions.
    # Memory Usage: 14 MB, less than 48.44% of Python3 online submissions.
    # T : O(N), S : O(N)
    def reverseWords(self, s: str) -> str:
        s = re.sub(r"\s{2,}", " ", s)
        words = s.strip().split(" ")
        return " ".join(reversed(words))

    # Swaps chars in place.
    @staticmethod
    def reverse_word(sentence: List[str], lo: int, hi: int) -> None:
        while hi > lo:
            sentence[lo], sentence[hi] = sentence[hi], sentence[lo]
            lo += 1
            hi -= 1

    # Runtime: 67 ms, faster than 37.76% of Python3 online submissions.
    # Memory Usage: 14 MB, less than 48.44% of Python3 online submissions.
    # T : O(N), S : O(N)
    # We are swapping chars in place here. If strings were mutable in Python,
    # this solution would have been O(1) space.
    def reverseWords1(self, s: str) -> str:
        # Replace all consecutive whitespaces, with a single space.
        s = re.sub(r"\s{2,}", " ", s)
        # Remove spaces at the start and end.
        s = s.strip()
        # Reverse the entire sentence.
        S = list(reversed(s))
        lo = hi = 0
        n = len(S)
        while hi < n:
            # To signify the end of a word.
            if S[hi] == " ":
                # Now we reverse the word in place.
                Solution.reverse_word(S, lo, hi - 1)
                lo = hi + 1
            hi += 1
        # Reverse the last word, as there is no space to trigger it.
        Solution.reverse_word(S, lo, hi - 1)

        return "".join(S)


class Solution2:
    """
    Without using an built in functions.
    """

    def reverseWords(self, s):
        arr = list(s)
        self.reverse_string(arr, 0, len(arr) - 1)
        self.reverse_word(arr)
        word = self.trim_sides(arr)
        res = self.trim_space(word)
        return "".join(res)

    def reverse_string(self, arr, l, r):
        """reverse a given string"""
        while l < r:
            arr[l], arr[r] = arr[r], arr[l]
            l += 1
            r -= 1
        return arr

    def reverse_word(self, arr):
        """reverse every words in a string"""
        l, r = 0, 0
        while r < len(arr):
            while r < len(arr) and not arr[r].isspace():
                r += 1
            self.reverse_string(arr, l, r - 1)
            r += 1
            l = r
        return arr

    def trim_sides(self, arr):
        """str.strip() basically"""
        if "".join(arr).isspace():
            return []
        l, r = 0, len(arr) - 1
        while l < r and arr[l].isspace():
            l += 1
        while l < r and arr[r].isspace():
            r -= 1
        return arr[l : r + 1]

    def trim_space(self, word):
        """remove duplicating space in a word"""
        if not word:
            return []
        res = [word[0]]
        for i in range(1, len(word)):
            if res[-1].isspace() and word[i].isspace():
                continue
            res.append(word[i])
        return res


if __name__ == "__main__":
    sol = Solution()
    assert sol.reverseWords(s="   the    sky   is blue    ") == "blue is sky the"
    assert sol.reverseWords(s="the sky is blue") == "blue is sky the"
