class Solution:
    """
    Brute Force works on creating every possible contiguous substring and
    checking for a palindrome. We can optimise this by using a dictionary and
    keeping track of all strings checked till now. Then in our loop iteration, if
    we get a string "abcde" we check if "cde" is in the dictionary or not, if it
    is there then if it is False. We can confidently the whole string is also not
    a palindrome as its inner string is not a palindrome. If inner string is a
    palindrome then we check if the 2 extreme chars in the String is same or not.
    If same then the string is palindrome. We can increase count. If it is not in
    d, then do from scratch. We start from small strings, length = 1, and make our
    way up.
    """

    def checkPalindrome(self, string: str):
        i, j = 0, len(string) - 1
        while i <= j:
            if string[i] == string[j]:
                pass
            else:
                return False

            i += 1
            j -= 1
        return True

    # Runtime: 1616 ms, faster than 5.00% of Python3 online submissions.
    # Memory Usage: 227.2 MB, less than 5.06% of Python3 online submissions.
    def countSubstrings(self, word: str) -> int:
        # We keep a dict, to store the previous results for our palindrome
        # check. For each string we store a bool, could also be done using a dp
        # array. (Which would've been more optimal (?))
        d: dict[str, bool] = {}
        count = 0
        for width in range(1, len(word) + 1):
            for start in range(len(word) - width + 1):
                end = start + width
                string = word[start:end]
                innerString = word[start + 1 : end - 1]
                if innerString in d:
                    check = d[innerString]
                    if check:
                        check = string[0] == string[-1]
                else:
                    check = self.checkPalindrome(string)
                count += check
                d[string] = check
                if check:
                    print(string)
        return count

    def countSubstringsBruteForce(self, word: str) -> int:
        # Create all substrings, and check for palindrome.
        d, count = {}, 0
        for width in range(1, len(word) + 1):
            for start in range(len(word) - width + 1):
                end = start + width
                string = word[start:end]
                check = self.checkPalindrome(string)
                count += check
                d[string] = check
                if check:
                    print(string)
        return count

    # Runtime: 155 ms, faster than 40.65%.
    # Memory Usage: 16.5 MB, less than 25.19%.
    # T : O(N^2), S : O(1)
    def countSubstrings1(self, s: str) -> int:
        # For every char in the string, we try to set this as the palindrome
        # centre and expand outwards, incrementing our answer on the way. O(N^2)
        # worst case time complexity for iterating over all the chars, checking
        # for palindromes is O(1), we rely on our loop logic for this.
        n = len(s)
        ans = 0

        # For palindromes of odd length, we expand from a single centre piece.
        for centre in range(n):
            l = 0
            while centre - l >= 0 and centre + l < n and s[centre - l] == s[centre + l]:
                ans += 1
                l += 1
        # For palindromes of even length, we expand from 2 centre pieces.
        for left in range(n - 1):
            right = left + 1
            l = 0
            while left - l >= 0 and right + l < n and s[left - l] == s[right + l]:
                ans += 1
                l += 1

        return ans

    def countSubstrings2(self, S: str):
        # Same logic, but both loops are implemented together here.
        N = len(S)
        ans = 0
        for center in range(2 * N - 1):
            left = center // 2
            right = left + center % 2
            while left >= 0 and right < N and S[left] == S[right]:
                ans += 1
                left -= 1
                right += 1
        return ans


if __name__ == "__main__":
    sol = Solution()
    assert sol.countSubstrings1(s="abc") == 3
    assert sol.countSubstrings1(s="aaa") == 6
