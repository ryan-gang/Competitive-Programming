class Solution:
    # Sort the sequence, and find out the differece between each consecutive
    # item, if it's not same, AP can't be created.
    # T : O(NLogN), S : O(N) (for sorting)
    def canMakeArithmeticProgression(self, arr: list[int]) -> bool:
        arr.sort()
        diff = arr[1] - arr[0]
        for i in range(1, len(arr)):
            d = arr[i] - arr[i - 1]
            if diff != d:
                return False
        return True

    # T : O(N), S : O(N)
    def canMakeArithmeticProgression1(self, arr: list[int]) -> bool:
        smallest, largest, n = min(arr), max(arr), len(arr)
        if (largest - smallest) % (n - 1) != 0:
            return False
        diff = (largest - smallest) // (n - 1)
        items: set[int] = set()
        if diff == 0:
            return True
        # Now every element's difference with the smallest elements should be
        # `k * diff`, k = [0, n-1], And to make sure that there aren't duplicates,
        # we can store the elements in a set. Or we can also actually put the
        # element in its proper place after finding out the k.
        for i in arr:
            d = i - smallest
            if d % diff != 0:
                return False
            items.add(i)
        return len(items) == n

    # T : O(N), S : O(1)
    def canMakeArithmeticProgression2(self, arr: list[int]) -> bool:
        smallest, largest, n = min(arr), max(arr), len(arr)
        if (largest - smallest) % (n - 1) != 0:
            return False
        diff = (largest - smallest) // (n - 1)
        if diff == 0:
            return True
        # We will find out the proper place of every element in the AP, and try
        # to place it there.
        i = 0
        while i < n:
            item = arr[i]
            d = item - smallest
            if d % diff != 0:
                return False

            position = (item - smallest) // diff
            if position == i:
                i += 1
            elif arr[position] == arr[i]:
                # Handle infinite loop, this case wouldn't happen for an actual
                # AP with d > 0, so return False.
                return False
            else:  # SWAP.
                arr[i], arr[position] = arr[position], arr[i]
        return True


if __name__ == "__main__":
    sol = Solution()
    assert not sol.canMakeArithmeticProgression2([1, 2, 4])
    assert sol.canMakeArithmeticProgression2([1, 3, 5])
