from typing import List


# 611 ms
# 6.14MB 32.80%.
class Solution:
    """
    Question is simple, but still I feel bad. I chose the delimiter intelligently.
    If there was a word equal to my delimiter, my code would have broken.
    So, other approach.
    Using the word length as the delimiter. Will make the code a bit more complicated.
    """

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
            res.append(str[j + 1 : j + 1 + length])
            # move pointer to end of the current word
            i = j + 1 + length
        return res


class Solution3:
    """
    encode([ABC, DEFG, HIJ]) = ABC3|DEFG4|HIJ3|
    string + len(string) + |
    """

    SPECIAL_CHAR = "|"

    def encode(self, strs: List[str]) -> str:
        encoded = []
        for string in strs:
            length = len(string)
            encoded.append(f"{string}{length}{Solution3.SPECIAL_CHAR}")
        enc_strs = "".join(encoded)
        return enc_strs

    def decode(self, string: str) -> List[str]:
        strings = []
        idx = 0
        while idx < len(string):
            while idx < len(string) and string[idx] != Solution3.SPECIAL_CHAR:
                idx += 1
            inferred_length = int(string[idx - 1])
            strings.append(string[idx - inferred_length - 1 : idx - 1])
            idx += 1
        return strings


if __name__ == "__main__":
    sol = Solution3()
    strings = ["ABC", "DEFGHIJ", "KLMNOP"]
    enc = sol.encode(strings)
    dec = sol.decode(enc)
    print(f"Actual strings : {strings}\nEncoded strings : {enc}")
    assert strings == dec
