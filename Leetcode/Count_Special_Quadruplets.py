from collections import defaultdict


class Solution:
    # T : O(N^2), S : O(N^2)
    def countQuadruplets(self, nums: list[int]) -> int:
        # Ref : https://leetcode.com/problems/count-special-quadruplets/
        # solutions/1446988/java-c-python3-real-o-n-2-solution/
        res = 0
        l = len(nums)
        count: defaultdict[int, int] = defaultdict(int)

        # find a + b == d - c, and a < b < c < d
        for a in range(l - 1, 0, -1):  # A
            # res += the numbers of cases which a + b == d - c.
            # a: nums[b], b: nums[a], c: previous nums[a]
            for b in range(a - 1, -1, -1):  # B
                # a ranges from last element to second element
                # b ranges from the (last - 1)th element to the first element
                res += count[nums[a] + nums[b]]

            # count d - c, d: nums[b], c: nums[a],
            # start from the end of nums,
            # because a < b < c < d
            for d in range(l - 1, (c := a), -1):  # D
                # k ranges from the last element to the (c + 1)th element
                # We are essentially fixing C to the ath index
                count[nums[d] - nums[c]] += 1

        return res

    # T : O(N^4), S : O(1)
    def countQuadrupletsBrute(self, nums: list[int]) -> int:
        n, count = len(nums), 0
        for a in range(n):
            for b in range(a + 1, n):
                for c in range(b + 1, n):
                    for d in range(c + 1, n):
                        actual = nums[a] + nums[b] + nums[c]
                        expected = nums[d]
                        count += actual == expected
        return count


if __name__ == "__main__":
    sol = Solution()
    assert sol.countQuadruplets(nums=[1, 1, 1, 1]) == 0
    assert sol.countQuadruplets(nums=[1, 2, 3, 6]) == 1
    assert sol.countQuadruplets(nums=[3, 3, 6, 4, 5]) == 0
    assert sol.countQuadruplets(nums=[1, 1, 1, 3, 5]) == 4
