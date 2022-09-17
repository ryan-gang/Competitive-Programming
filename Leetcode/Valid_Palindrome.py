s: str = "A man, a plan, a canal: Panama"


class Solution:
    # Runtime: 80 ms, faster than 41.94%.
    # Memory Usage: 14.3 MB, less than 99.25%.
    # T : O(N), S : O(1)
    def isPalindrome(self, s: str) -> bool:
        start, end = 0, len(s) - 1
        while start < end:
            startChar = s[start].lower()
            endChar = s[end].lower()
            if startChar.isalnum():
                if endChar.isalnum():
                    if startChar != endChar:
                        return False
                else:
                    end -= 1
                    continue
            else:
                start += 1
                continue
            start += 1
            end -= 1

        return True

    # T : O(N), S : O(N)
    def isPalindrome2Liner(self, s: str) -> bool:
        A = [i.lower() for i in s if i.isalnum()]
        return A == A[::-1]
