class Solution:
    def checkPalindrome(self, string):
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
        d, count = {}, 0
        for width in range(1, len(word) + 1):
            for start in range(len(word) - width + 1):
                end = start + width
                string = word[start:end]
                innerString = word[start + 1: end - 1]
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
        print(count)

    def countSubstringsBruteForce(self, word: str) -> int:
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


sol = Solution()
sol.countSubstrings("aaa")


# Brute Force works on creating every possible *contiguos* substring and checking for a palindrome. We can optimise this by using a dictionary and keeping track of all strings checked till now. Then in our loop iteration, if we get a string "abcde" we check if "cde" is in the dictionary or not, if it is there then if it is False. We can confidently the whole string is also not a palindrome as its inner string is not a palindrome. If inner string is a palindrome then we check if the 2 extreme chars in the String is same or not. If same then the string is palindrome. We can increase count. If it is not in d, then do from scratch.
# We start from small strings, length = 1, and make our way up.
