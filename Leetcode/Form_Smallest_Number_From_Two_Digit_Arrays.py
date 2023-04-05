class Solution:
    """
    If the arrays, have the same number in both the arrays, we can create a
    single digit number. Which is always more preferable. Else, choose the min
    from both the arrays, and order them in sorted array.
    """

    def minNumber(self, nums1: list[int], nums2: list[int]) -> int:
        if len(set(nums1).intersection(nums2)) > 0:
            out = str(min(list(set(nums1).intersection(nums2))))
        else:
            arr = sorted([min(nums1), min(nums2)])
            str_arr = list(map(str, arr))
            out = "".join(str_arr)

        return int(out)

    def minNumber1(self, n1: list[int], n2: list[int]) -> int:
        common, m1, m2 = set(n1).intersection(n2), min(n1), min(n2)
        return min(common) if common else min(m1, m2) * 10 + max(m1, m2)


if __name__ == "__main__":
    sol = Solution()
    assert sol.minNumber(nums1=[3, 5, 2, 6], nums2=[3, 1, 7]) == 3
