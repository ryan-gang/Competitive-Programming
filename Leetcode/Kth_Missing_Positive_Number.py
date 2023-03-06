class Solution:
    # Runtime: 62 ms, faster than 35.59%.
    # Memory Usage: 14 MB, less than 80.43%.
    # T : O(N), S : O(N)
    # T : O(N + K), but N and K are comparable.
    def findKthPositive1(self, arr: list[int], k: int) -> int:
        array = set(arr)
        for i in range(1, len(array) + k + 1):
            if i not in array:
                k -= 1
                if k == 0:
                    return i

    def findKthPositive(self, arr: list[int], k: int) -> int:
        """
        arr = [2, 3, 4, 7, 11]
        miss = [1, 1, 1, 3, 6] <- How many numbers are missing, at index i.
        miss[i] = arr[i] - (i + 1)
        So, we use binary search to find out the index where miss[i] is equals or just more than k.
        We know this index, is the first element gte than k.
        We can linearly go back in miss, upto K to find our corresponding supposed value in arr.
        (As this is the first element gte k, there wont be any abrupt changes in miss)
        So, once we find out idx in arr, we know our answer will be arr[i] - (miss[i] - (k - 1))
        But miss[i] = arr[i] - (i+1)
        Hence, out = i + k.
        Ref : https://leetcode.com/problems/kth-missing-positive-number/solutions
        /1004535/python-two-solutions-o-n-and-o-log-n-explained/
        """
        lo, hi = 0, len(arr)
        while lo < hi:
            mid = (hi + lo) // 2
            print(mid)
            if arr[mid] - mid - 1 > k:
                hi = mid
            else:
                lo = mid + 1

        return hi + k


if __name__ == "__main__":
    sol = Solution()
    assert sol.findKthPositive(arr=[2, 3, 4, 7, 11], k=5) == 9
    assert sol.findKthPositive(arr=[1, 2, 3, 4], k=2) == 6
    assert sol.findKthPositive(arr=[1, 2], k=1) == 3
