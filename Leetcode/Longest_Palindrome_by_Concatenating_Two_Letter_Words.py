from collections import Counter
from typing import List


class Solution:
    """
    Intuition behind the solution is that :
    1. If reverse of a word is present in the Counter, eg "ab" and "ba" means
    we can add these two words in our palindrome. But the issue is with the count of their
    occurences. If "ab" is present 12 times, and "ba" is present 2 times, we can only take
    2 of each. So we add min(d[word], d[reversed_word]).
    2. If the word itself is a palindrome, it gets a bit tricky. We can add this word to our
    palindrome, only if it occurs an even number of times, as their is no seperate
    reversed_word of this. But if it occurs an odd number of time, we add d[word] - 1 counts
    of it to the palindrome.
    3. But remember we can add 1 odd number of "palindrome word" to our palindrome.
    Which is where the `flag` comes into use, if we have an odd number of palindrome word, we set
    flag to True, and finally add 1 to our final length.
    4. Also as we are adding entire occurences of a word to our palindrome, we keep a track of all
    these words in our set, so we do not double count any occurence. We only add the word to our set
    and not the reverse because when we get to the reverse we want to add its count too,
    which is not added previously.
    5. Finally we multiply pals by 2, as this is the count of 2 letter words, not letters.
    """

    # Runtime: 3424 ms, faster than 32.64% of Python3 online submissions.
    # Memory Usage: 38.5 MB, less than 25.74% of Python3 online submissions.
    # T : O(N), S : O(N)
    def longestPalindrome(self, words: List[str]) -> int:
        seen = set()

        d = Counter(words)
        flag = False
        pals = 0

        for word in d:
            reversed_word = word[::-1]
            if reversed_word in d and word not in seen:
                if word[0] == word[1]:
                    if d[word] % 2:
                        flag = True
                        pals += d[word] - 1
                        seen.add(word)
                    else:
                        pals += d[word]
                else:
                    pals += min(d[word], d[reversed_word])
                    seen.add(word)
        if flag:
            pals += 1

        return pals * 2


if __name__ == "__main__":
    sol = Solution()
    assert sol.longestPalindrome(words=["ab", "ty", "yt", "lc", "cl", "ab"]) == 8
    assert sol.longestPalindrome(words=["ab", "ty", "yt", "lc", "cl", "ab", "ba", "ba", "ba"]) == 16
    assert sol.longestPalindrome(words=["lc", "cl", "gg"]) == 6
    assert sol.longestPalindrome(words=["cc", "ll", "xx"]) == 2
    assert sol.longestPalindrome(words=["cc", "ll", "xx", "cc", "cc"]) == 6
    assert sol.longestPalindrome(words=["cc", "ll", "xx", "cc", "cc", "cc"]) == 10
    assert sol.longestPalindrome(words=["cc", "aa", "aa", "aa", "cc", "cc", "cc"]) == 14
