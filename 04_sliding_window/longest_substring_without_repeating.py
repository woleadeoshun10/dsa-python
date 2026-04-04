"""
Problem: Longest Substring Without Repeating Characters

Given a string s, find the length of the longest substring
without repeating characters.

Example:
Input: s = "abcabcbb"
Output: 3
Explanation: "abc" is the longest substring without duplicates.

Approach: Sliding Window + HashSet
- Use a set to track characters in the current window
- Expand right pointer (r)
- If duplicate found, shrink from left (l)
- Keep updating max length

Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()   # stores unique characters in window
        l = 0          # left pointer
        maxLength = 0     # result

        for r in range(len(s)):
            # shrink window until no duplicate
            while s[r] in charSet:
                charSet.remove(s[l])
                left += 1

            # add current character
            charSet.add(s[r])

            # update max length
            maxLength = max(maxLength, r - l + 1)

        return maxLength

