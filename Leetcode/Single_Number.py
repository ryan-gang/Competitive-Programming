from typing import List


class Solution:
    # Runtime: 133 ms, faster than 97.41% of Python3 online submissions.
    # Memory Usage: 16.7 MB, less than 49.71% of Python3 online submissions.
    # T : O(N), S : O(1)
    """Keeping in mind the O(1) space constraint, we also could've simply sorted the array.
    And found consecutive dissimilar items.
    In our solution we use the XOR logic gate.
    Because a ^ a is 0. So all the double number of elements will be reduced to 0.
    And finally 0 ^ ANSWER will give our required answer.
    Which is why we start with out = 0. Because later on we gonna see the same element (0)
    which will again give us 0, not changing our out.
    Ref : https://leetcode.com/problems/single-number/discuss/
    1771720/C%2B%2B-EASY-SOLUTIONS-(SORTING-XOR-MAPS-(OR-FREQUENCY-ARRAY))
    """

    def singleNumber(self, nums: List[int]) -> int:
        out = 0
        for num in nums:
            out = out ^ num

        return out
