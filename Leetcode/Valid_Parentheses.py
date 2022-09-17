from collections import deque


class Solution:
    def isValid(self, s: str) -> bool:
        reverse = {"(": ")", "[": "]", "{": "}", ")": "|", "]": "|", "}": "|"}
        stack = deque()
        for i in s:
            if stack and (reverse[stack[-1]] == i):
                stack.pop()
            else:
                stack.append(i)

        return len(stack) == 0

for each char in the string,
if stack is not empty and the reverse of the "peek"-ed brace is the current char, pop the stack. 
else push to stack. 
At the end if there are un-pop-ed chars return False.

class SolutionBetter:
    def isValid(self, s: str) -> bool:
        stack = []
        dict = {"]": "[", "}": "{", ")": "("}
        for char in s:
            if char in dict.values():
                stack.append(char)
            elif char in dict:
                if stack == [] or dict[char] != stack.pop():
                    return False
            else:
                return False
        return stack == []

for each char in the string,
if it is an opening brace, push to stack.
else if it is a closing brace,
    if stack is empty return False. (If stack is empty then an empty brace means string is not valid)
    else if the popped char and the reverse of the current brace don't match that also would mean the string is not valid. (Because this char has no opening brace)
else if char is not a brace also return false.
Note : Only the closing braces have entries in the "reverse" dictionary.


class SolutionBest:
    def isValid(self, s: str) -> bool:
        stack = deque()
        stack.append("placeholder")
        reverse = {')':'(',']':'[','}':'{'}
        for i in s:
            if i in reverse:
                if stack.pop() != reverse[i]:
                    return False
            else:
                stack.append(i)
                
        return len(stack) == 1

This solution is a bit tricky.
Initialize the stack with a placeholder.
Then for every char in string, if it is a closing brace, and the "peek"ed element in the stack is not the reverse of the current char, then return False.
if not closing brace push to stack.
The placeholder is there, for the case of [")"], as the stack is empty, when we require to pop, we instead match the popped placeholder with the brace and return False.
This case requires the placeholder no other fixes work.


https://leetcode.com/problems/valid-parentheses/discuss/9203/Simple-Python-solution-with-stack

# Runtime: 45 ms, faster than 44.81% of Python3 online submissions for Valid Parentheses.
# Memory Usage: 13.9 MB, less than 70.27% of Python3 online submissions for Valid Parentheses.