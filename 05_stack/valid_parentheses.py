"""
Problem: Valid Parentheses
Pattern: Stack
Difficulty: Easy

Time Complexity: O(n)
We scan the string once.

Space Complexity: O(n)
In the worst case, the stack stores all opening brackets.

Key Idea:
Use a stack to track opening brackets.
When we see a closing bracket, it must match the
most recent opening bracket on the stack.
"""


class Solution:
    def isValid(self, s: str) -> bool:

        stack = []
        mapping = {")": "(", "}": "{", "]": "["}

        for char in s:

            if char in mapping:
                top = stack.pop() if stack else "#"

                if mapping[char] != top:
                    return False

            else:
                stack.append(char)

        return not stack
    

#============================================
# BRUTE FORCE 
#============================================
class Solution:
    def isValid(self, s: str) -> bool:
        while '()' in s or '{}' in s or '[]' in s:
            s = s.replace('()', '')
            s = s.replace('{}', '')
            s = s.replace('[]', '')
        return s == ''
#TC: O(N^2)
#SC: O(N)