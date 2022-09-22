class Solution:
    # Runtime: 120 ms, faster than 19.48% of Python3 online submissions.
    # Memory Usage: 14.5 MB, less than 97.44% of Python3 online submissions.
    # T : O(N), S : O(N)
    def reverseWords(self, s: str) -> str:
        # Words are demarcated by " "
        out = ""
        idx = start = 0
        while idx < len(s):
            if s[idx] == " " or idx == len(s) - 1:
                # If encounter " ", that means word break, add the previous word in reverse to out.
                for i in range(idx, start - 1, -1):
                    out += s[i]
                # Set start to the start of the next word.
                start = idx + 1
            idx += 1
        return out

    # Runtime: 174 ms, faster than 8.21% of Python3 online submissions.
    # Memory Usage: 15.1 MB, less than 13.98% of Python3 online submissions.
    # T : O(N), S : O(N)
    def reverseWords2(self, s: str) -> str:
        """
        Ideally instead of creating a new array, we would swap elements in the same input string,
        but python doesn't allow index assignment in a string.
        So my hands are kinda tied, in that I have to create a new array.
        And in that I can swap values as required.
        """
        # Words are demarcated by " "
        s = list(s)
        s.append(" ")
        idx = 0
        start = 0
        while idx < len(s):
            if s[idx] == " ":
                # Instead of adding chars into a new array, we swap the chars with the proper char.
                lo, hi = start, idx - 1
                while lo < hi:
                    s[lo], s[hi] = s[hi], s[lo]
                    lo += 1
                    hi -= 1
                start = idx + 1
            idx += 1
        return "".join(s[:-1])

    # Runtime: 259 ms, faster than 5.04% of Python3 online submissions.
    # Memory Usage: 14.6 MB, less than 46.10% of Python3 online submissions.
    def reverseWords3(self, s: str) -> str:
        s = list(s)  # Because python strings are immutable,this is reqired for inplace swapping.
        s.append(" ")
        # Words are demarcated by, spaces so the last word is not getting processed.
        # This helps in processing the last word.
        i, n, start_prev = 0, len(s), 0
        while i < n:
            if s[i] == " ":
                # Finding out spaces, and then reversing the word ending in the prev index.
                self.reverse(s, start_prev, i - 1)
                start_prev = i + 1
            i += 1
        return "".join(s)[
            :-1
        ]  # Return a string from the list, and remove the extra space we added.

    def reverse(self, s, start, end):
        # Swap chars in place.
        while start < end:
            s[start], s[end] = s[end], s[start]
            start += 1
            end -= 1


sol = Solution()
assert sol.reverseWords(s="Let's take LeetCode contest") == "s'teL ekat edoCteeL tsetnoc"
assert sol.reverseWords(s=" ") == " "
assert sol.reverseWords(s="a b c") == "a b c"
