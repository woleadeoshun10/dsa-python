"""
Problem: Contains Duplicate
Pattern: Arrays & Hashing
Difficulty: Easy

Brute Force:
Time Complexity: O(n^2)
Space Complexity: O(1)

Optimized (Hash Set):
Time Complexity: O(n)
Space Complexity: O(n)

Key Insight:
Use a hash set to track seen elements.
If we ever encounter a number already in the set,
a duplicate exists.
"""

from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        """
        Optimized Solution (Preferred)
        """
        numChecker = set()

        for num in nums:
            if num in numChecker:
                return True
            numChecker.add(num)

        return False


# ----------------------------
# Brute Force Version
# ----------------------------

class BruteForceSolution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] == nums[j]:
                    return True
        return False


# ----------------------------
# Python One-Liner
# ----------------------------

class OneLinerSolution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))
