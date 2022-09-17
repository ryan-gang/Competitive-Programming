from collections import deque


class Solution:
    # Runtime: 139 ms, faster than 28.91% of Python3 online submissions.
    # Memory Usage: 14.2 MB, less than 13.37% of Python3 online submissions.
    # T : O(N), S : O(N)
    # Space is not optimal, we use both stack and set.
    def lengthOfLongestSubstring(self, s: str) -> int:
        hi = 0
        count = max_count = 0
        value_set = set()
        stack = deque()
        while hi < len(s):
            char = s[hi]
            if char not in value_set:
                value_set.add(char)
                stack.append((char, hi))
                count = len(value_set)
                max_count = max(count, max_count)
            else:
                popped_val = None
                while popped_val != char:
                    popped_val, index = stack.popleft()
                    value_set.remove(popped_val)
                count = len(value_set)
                hi -= 1
            hi += 1

        return max_count

    # Runtime: 85 ms, faster than 72.58% of Python3 online submissions.
    # Memory Usage: 14 MB, less than 49.55% of Python3 online submissions.
    # T : O(N), S : O(N)
    def lengthOfLongestSubstringOptimised(self, s: str) -> int:
        start = max_length = i = 0
        used = {}
        while i < len(s):
            char = s[i]
            # Can use range, and enumerate for more readability.
            if char in used and start <= used[char]:
                start = used[char] + 1
            else:
                max_length = max(max_length, i - start + 1)
            used[char] = i
            i += 1

        return max_length


sol = Solution()
assert sol.lengthOfLongestSubstringOptimised(s="abcabcbb") == 3
assert sol.lengthOfLongestSubstringOptimised(s="bbbbb") == 1
assert sol.lengthOfLongestSubstringOptimised(s="pwwkew") == 3
assert sol.lengthOfLongestSubstringOptimised(s="abcdefabcdfe") == 6
assert sol.lengthOfLongestSubstringOptimised(s="adbcfdegh") == 7
