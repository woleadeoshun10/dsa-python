"""
Problem: Longest Repeating Character Replacement
Pattern: Sliding Window
Difficulty: Medium

Description:
Given a string s and an integer k, you can replace at most k characters.
Return the length of the longest substring containing the same letter
you can get after performing at most k replacements.

Approach 1:
Use a sliding window and a frequency map.
If the number of characters we need to replace is greater than k,
shrink the window from the left.

Time Complexity: O(n * 26) ≈ O(n)
Space Complexity: O(26) ≈ O(1)
"""


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        charCount = {}
        l = 0
        maxLength = 0

        for r in range(len(s)):
            charCount[s[r]] = 1 + charCount.get(s[r], 0)

            while (r - l + 1) - max(charCount.values()) > k:
                charCount[s[l]] -= 1
                l += 1

            maxLength = max(maxLength, r - l + 1)

        return maxLength

"""
Approach 2 (Optimized):
Use a sliding window with a frequency map and track the highest frequency
character seen in the current window.

If:
window size - maxFreq > k
then shrink the window.

Time Complexity: O(n)
Space Complexity: O(26) ≈ O(1)
"""


class OptimizedSolution:
    def characterReplacement(self, s: str, k: int) -> int:
        charCount = {}
        l = 0
        maxFreq = 0
        maxLength = 0

        for r in range(len(s)):
            charCount[s[r]] = 1 + charCount.get(s[r], 0)
            maxFreq = max(maxFreq, charCount[s[r]])

            while (r - l + 1) - maxFreq > k:
                charCount[s[l]] -= 1
                l += 1

            maxLength = max(maxLength, r - l + 1)

        return maxLength
