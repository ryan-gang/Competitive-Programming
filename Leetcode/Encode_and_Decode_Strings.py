from typing import List


# 611 ms 6.14MB 32.80% beat %.
class Solution:
    DELIMITER = "↔↕"
    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    """

    def encode(self, strs):
        # write your code here
        enc_strs = Solution.DELIMITER.join(strs)[::-1]
        return enc_strs

    """
    @param: str: A string
    @return: dcodes a single string to a list of strings
    """

    def decode(self, str):
        # write your code here
        rev_strs = str[::-1]
        strings = rev_strs.split(Solution.DELIMITER)
        return strings


# Question is simple, but still I feel bad. I chose the delimiter intelligently.
# If there was a word equal to my delimiter, my code would have broken.
# So, other approach.
# Using the word length as the delimiter. Will make the code a bit more complicated.


class Solution2:
    # [w1, w2, w3] -encode-> len(w1)#w1len(w2)#w2len(w3)#w3
    # len(w1)#w1len(w2)#w2len(w3)#w3 -decode-> [w1, w2, w3]
    # len(w)#w
    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    """

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            # type convert and concatenate
            res += str(len(s)) + "#" + s
        return res

    """
    @param: str: A string
    @return: dcodes a single string to a list of strings
    """

    def decode(self, str: str) -> List[str]:
        i = 0
        res = []
        # think about first word to decode
        while i < len(str):
            j = i
            # iterate until hash sign to get length digits
            while str[j] != "#":
                j += 1
            # length digit(s)
            length = int(str[i:j])
            # append the word
            res.append(str[j + 1: j + 1 + length])
            # move pointer to end of the current word
            i = j + 1 + length
        return res
