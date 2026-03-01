"""
Problem: Valid Anagram
Pattern: Arrays & Hashing
Difficulty: Easy

Approach 1 (Optimized – Hash Map with Single Dictionary):
Time Complexity: O(n)
Space Complexity: O(n)  (O(1) if character set is fixed for a-z)

Approach 2 (Two Dictionaries):
Time Complexity: O(n)
Space Complexity: O(n)

Approach 3 (Sorting):
Time Complexity: O(n log n)
Space Complexity: O(n)
"""

from collections import defaultdict


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        Optimized Solution (Single Hash Map)
        """
        if len(s) != len(t):
            return False

        count = defaultdict(int) #50% faster than {}... also shorter

        for ch in s:
            count[ch] += 1

        for ch in t:
            count[ch] -= 1
            if count[ch] < 0:
                return False

        return True


# -----------------------------------
# Alternative: Two Dictionary Method
# -----------------------------------

class TwoMapSolution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        countS = {}
        countT = {}

        for char in s:
            countS[char] = countS.get(char, 0) + 1

        for char in t:
            countT[char] = countT.get(char, 0) + 1

        return countS == countT


# -----------------------------------
# Alternative: Sorting
# -----------------------------------

class SortingSolution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        return sorted(s) == sorted(t)