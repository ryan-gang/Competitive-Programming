# Runtime: 57 ms, faster than 86.52%.
# Memory Usage: 13.9 MB, less than 96.79%.
# T : O(N), S : O(1)
class Solution:
    """
    We keep a running count of our current chars occurrences.
    If the streak is broken, we write the char and its count in the same array.
    But, rest assured we will never lose information.
    Because :
    1. If we are processing a char that occurs only once, we will write it to its index,
    and no extra index will be taken up.
    2. For a char with streak = 2, we require 2 indices to write it out.
    <char>, 2.
    3. For all other cases, the number of indices required to write out the compressed string
    is LESS than the number of original chars.
    So our write_index will always be behind the read_index.
    And we never lose data.
    """

    @staticmethod
    def write(chars: list[str], idx: int, count: int, write_idx: int) -> int:
        chars[write_idx] = chars[idx - 1]
        write_idx += 1
        if count > 1:
            for _ in str(count):
                chars[write_idx] = _
                write_idx += 1
        return write_idx

    def compress(self, chars: list[str]) -> int:
        write_idx = 0
        count = 1
        for idx, val in enumerate(chars):
            if idx > 0 and chars[idx - 1] == val:
                count += 1
            else:
                if idx > 0:
                    write_idx = Solution.write(chars, idx, count, write_idx)
                count = 1

        # We want to write the final character in this instruction.
        # But as we have a for loop, we will never go to idx + 1.
        # And our write function always writes the char at idx - 1.
        # Where idx = len(chars)
        write_idx = Solution.write(chars, idx + 1, count, write_idx)
        print(chars)
        return write_idx


# Leetcode Editorial.
# Clear, concise code.
class Solution1:
    def compress(self, chars: list[str]) -> int:
        i = 0
        res = 0
        while i < len(chars):
            group_length = 1
            while i + group_length < len(chars) and chars[i + group_length] == chars[i]:
                group_length += 1
            chars[res] = chars[i]
            res += 1
            if group_length > 1:
                str_repr = str(group_length)
                chars[res : res + len(str_repr)] = list(str_repr)
                res += len(str_repr)
            i += group_length
        return res


if __name__ == "__main__":
    sol = Solution()
    assert sol.compress(chars=["a", "a", "b", "b", "c", "c", "c"]) == 6
    assert (
        sol.compress(chars=["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"]) == 4
    )
    assert sol.compress(["a", "b", "c"]) == 3
