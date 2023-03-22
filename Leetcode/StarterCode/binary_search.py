"""
Minimize k, such that condition(k) is True
Binary search template:

1. Correctly initialize the boundary variables left and right.
Only one rule: set up the boundary to include all possible elements;
2. Decide return value. Is it return left or return left - 1?
Remember this: after exiting the while loop, left is the minimal value satisfying the condition;
3. Design the condition function. This is the most difficult and most beautiful part.

Ref : https://leetcode.com/problems/koko-eating-bananas/solutions/769702/
python-clear-explanation-powerful-ultimate-binary-search-template-solved-many-problems
"""

# At the end we will get the lowest index in array, such that it satisfies condition.
# So, condition can be something like value >= n.
# And out of all the indices satisfying this, we get the lowest index.


def binary_search(array: list[int]) -> int:
    def condition(value: int):
        pass

    left, right = 0, len(array)
    while left < right:
        mid = left + (right - left) // 2
        if condition(mid):
            right = mid
        else:
            left = mid + 1
    return left
