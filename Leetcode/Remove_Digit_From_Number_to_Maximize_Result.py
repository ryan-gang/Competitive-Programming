class Solution:
    # Naive solution.
    # Runtime: 59 ms, faster than 45.97%.
    # Memory Usage: 13.8 MB, less than 66.45%.
    # T : O(N*N), S : O(N) ; worst case when all the digits in number are `digit`.
    def removeDigit(self, number: str, digit: str) -> str:
        """
        Create all the possible numbers possible by removing digit.
        Returning max of all these numbers.
        """
        nums: list[str] = []
        for idx, val in enumerate(number):
            if val == digit:
                new_num = number[:idx] + number[idx + 1 :]
                nums.append(int(new_num))

        return str(max(nums))

    # Runtime: 63 ms, faster than 31.78%.
    # Memory Usage: 13.8 MB, less than 97.53%.
    # T : O(N), S : O(1)
    def removeDigit2(self, number: str, digit: str) -> str:
        """
        Optimised solution.
        There are 2 scenarios.
        1. There exists an index with `digit` such that the value at the next index is greater.
        2. All indices with `digit` are only followed by smaller values.
        In the case of 1, as we have `digit` indices followed by indices with
        higher value, we can for sure increase our final int. So, now we focus
        on increasing it by the highest value. Towards that we replace the
        "earliest" `digit` index, as it has the highest placevalue. (we are
        iterating from higher placevalue to smaller). But in case of 2, if we
        replace digit, it is guaranteed to reduce our final int. So we replace
        the `digit` index with the smallest placevalue. So as to take the
        minimal hit to our initial number..
        """
        last_idx, n = 0, len(number)
        for idx, val in enumerate(number):
            if val == digit:
                last_idx = idx
                if idx < n - 1 and number[idx + 1] > val:
                    return number[:idx] + number[idx + 1 :]

        return number[:last_idx] + number[last_idx + 1 :]
