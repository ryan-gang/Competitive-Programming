class Solution:
    # Naive solution.
    # Runtime: 59 ms, faster than 45.97%.
    # Memory Usage: 13.8 MB, less than 66.45%.
    # T : O(N), S : O(N)
    def removeDigit(self, number: str, digit: str) -> str:
        nums = []
        for idx, val in enumerate(number):
            if val == digit:
                new_num = number[:idx] + number[idx + 1 :]
                nums.append(int(new_num))

        return str(max(nums))

    # Runtime: 63 ms, faster than 31.78%.
    # Memory Usage: 13.8 MB, less than 97.53%.
    # T : O(N), S : O(N)
    def removeDigit2(self, number: str, digit: str) -> str:
        """
        Optimised solution.
        If we find an index with 'val' such that the next index is greater than it,
        we remove this val and return, cause removing this increases the new number.
        Else we return the LAST index with 'val' in it.
        """
        last_idx, n = None, len(number)
        for idx, val in enumerate(number):
            if val == digit:
                last_idx = idx
                if idx < n - 1 and number[idx + 1] > val:
                    return number[:idx] + number[idx + 1 :]

        return number[:last_idx] + number[last_idx + 1 :]
