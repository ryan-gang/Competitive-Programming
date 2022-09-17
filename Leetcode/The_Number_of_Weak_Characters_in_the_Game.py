from typing import List


class Solution:
    # Runtime: 4793 ms, faster than 9.21% of Python3 online submissions.
    # Memory Usage: 67.1 MB, less than 63.30% of Python3 online submissions.
    # T : O(N), S : O(1)
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        # Sort properties, based on the 1st value, in decreasing order,
        # and then if the 1st values are same, ascending order for the 2nd value.
        # So if 1st value is not equal, we can check if the 2nd value is also smaller,
        # if 1st value is equal, 2nd values will be in increasing order, wont be smaller.
        properties.sort(key=lambda x: (-x[0], x[1]))

        # Our aim is to find the largest element upto now,
        # so we can find the max no of elements smaller than it.
        # Completely forget the first element, only think about the 2nd element.
        curr_max, ans = 0, 0
        for _, d in properties:
            if d < curr_max:
                ans += 1
            else:
                curr_max = d

        return ans

    # T : O(N), S : O(N)
    def numberOfWeakCharactersStack(self, properties: List[List[int]]) -> int:
        properties.sort(key=lambda x: (x[0], -x[1]))
        stack = []
        ans = 0
        for a, d in properties:
            while stack and stack[-1] < d:
                stack.pop()
                ans += 1
            stack.append(d)
        return ans


sol = Solution()
assert sol.numberOfWeakCharacters(properties=[[1, 5], [10, 4], [4, 3]]) == 1
assert sol.numberOfWeakCharacters(properties=[[1, 2], [1, 3], [1, 4]]) == 0
