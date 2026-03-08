"""
Problem: Valid Palindrome
Pattern: Two Pointers
Difficulty: Easy

Approach 1 (Two Pointers - Optimal)
Time Complexity: O(n)
Space Complexity: O(1)

Approach 2 (Build New String)
Time Complexity: O(n)
Space Complexity: O(n)

Key Idea:
Ignore non-alphanumeric characters and compare letters case-insensitively.
The optimal approach uses two pointers from both ends of the string.
"""

class Solution:
    """
    Optimal solution using two pointers
    """
    def isPalindrome(self, s: str) -> bool:

        l = 0
        r = len(s) - 1

        while l < r:

            while l < r and not self.alphanum(s[l]):
                l += 1

            while r > l and not self.alphanum(s[r]):
                r -= 1

            if s[l].lower() != s[r].lower():
                return False

            l += 1
            r -= 1

        return True

    def alphanum(self, c):
        return (
            ord('A') <= ord(c) <= ord('Z') or
            ord('a') <= ord(c) <= ord('z') or
            ord('0') <= ord(c) <= ord('9')
        )


# ------------------------------------------------------
# Alternative Approach (Build New String)
# ------------------------------------------------------

class StringSolution:
    """
    Simpler solution that builds a filtered string
    """
    def isPalindrome(self, s: str) -> bool:

        newStr = ""

        for c in s:
            if c.isalnum():
                newStr += c.lower()

        return newStr == newStr[::-1]