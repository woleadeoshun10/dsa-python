"""
Problem: Minimum Window Substring
Pattern: Sliding Window
Difficulty: Hard

Description:
Given strings s and t, return the minimum window substring of s
such that every character in t (including duplicates) is included.

Approach:
- Use two hashmaps: countT (target) and window (current window)
- Expand right pointer to include characters
- Track how many required chars we "have"
- When we have all needed, shrink from left to find smallest window

Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""

        countT, window = {}, {}

        for c in t:
            countT[c] = 1 + countT.get(c, 0)

        have, need = 0, len(countT)
        res, resLen = [-1, -1], float("inf")
        left = 0

        for right in range(len(s)):
            c = s[right]
            window[c] = 1 + window.get(c, 0)

            if c in countT and window[c] == countT[c]:
                have += 1

            while have == need:
                # update result
                if (right - left + 1) < resLen:
                    res = [left, right]
                    resLen = right - left + 1

                # shrink window
                window[s[left]] -= 1
                if s[left] in countT and window[s[left]] < countT[s[left]]:
                    have -= 1

                left += 1

        l, r = res
        return s[l:r+1] if resLen != float("inf") else ""

