from collections import Counter


class Solution:
    # Runtime: 64 ms, faster than 65.44%.
    # Memory Usage: 14.8 MB, less than 24.97%.
    # T : O(NLogN), S : O(1)
    def isAnagram1(self, s: str, t: str) -> bool:
        s = "".join(sorted(s))
        t = "".join(sorted(t))
        i = j = 0
        if len(s) != len(t):
            return False
        while i < len(s):
            if s[i] == t[j]:
                i += 1
                j += 1
            else:
                return False
        return True

    # Runtime: 78 ms, faster than 42.50%.
    # Memory Usage: 14.4 MB, less than 66.46%.
    # T : O(N), S : O(1)
    def isAnagram2(self, s: str, t: str) -> bool:
        S = Counter(s)
        T = Counter(t)
        if S.keys() != T.keys():
            return False
        else:
            for key in S:
                if S[key] != T[key]:
                    return False
        return True

    def isAnagram3(self, s: str, t: str) -> bool:
        S = Counter(s)
        T = Counter(t)
        return S == T

    # Runtime: 55 ms, faster than 82.33%.
    # Memory Usage: 14.5 MB, less than 34.67%.
    # T : O(N), S : O(1)
    def isAnagram(self, s: str, t: str) -> bool:
        array = [0 for i in range(26)]
        for char in s:
            index = ord(char) - ord("a")
            array[index] += 1
        for char in t:
            index = ord(char) - ord("a")
            array[index] -= 1
        for val in array:
            if val != 0:
                return False
        return True


if __name__ == "__main__":
    sol = Solution()
    print(sol.isAnagram(s="rat", t="car"))
