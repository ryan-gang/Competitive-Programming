from collections import Counter


class Solution:
    """
    We need to find all the bulls first, cause it is higher priority.
    We just check if the values in both the strings, at the same index are same for the bulls.
    And for the cows, we keep a counter, (and after processing all the bulls)
    we check if the guessed char is present in the counter of 'secret'."""

    # Runtime: 98 ms, faster than 16.50% of Python3 online submissions.
    # Memory Usage: 14 MB, less than 33.13% of Python3 online submissions.
    def getHint(self, secret: str, guess: str) -> str:
        d = Counter(secret)
        bulls = cows = 0
        for i, j in zip(secret, guess):
            if i == j:
                bulls += 1
                d[j] -= 1
                if d[j] == 0:
                    del d[j]

        for i, j in zip(secret, guess):
            if i != j:
                if j in d:
                    cows += 1
                    d[j] -= 1
                    if d[j] == 0:
                        del d[j]

        return f"{bulls}A{cows}B"

    """Just get the bulls, by finding all chars at same indices.
    Then do a Counter intersection of secret and guess, to get all the matching chars
    ie bulls + cows, from this and the bulls count, we can get the cows."""

    def getHint1L(self, secret, guess):
        bulls = sum(a == b for a, b in zip(secret, guess))
        both = Counter(secret) & Counter(guess)
        return f"{bulls}A{sum(both.values()) - bulls}B"


if __name__ == "__main__":
    sol = Solution()
    assert sol.getHint(secret="1807", guess="7810") == "1A3B"
    assert sol.getHint(secret="1123", guess="0111") == "1A1B"
    assert sol.getHint(secret="1122", guess="1222") == "3A0B"
