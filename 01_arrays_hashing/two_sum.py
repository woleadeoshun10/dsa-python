"""
Problem: Two Sum
Pattern: Arrays & Hashing
Difficulty: Easy

Approach 1 (Optimized – Hash Map)
Time Complexity: O(n)
Space Complexity: O(n)

Approach 2 (Brute Force)
Time Complexity: O(n^2)
Space Complexity: O(1)

Key Idea:
Use a hash map to store previously seen numbers.
For each element, check if its complement exists.
"""

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Optimized Solution (Single Pass Hash Map)
        """
        seen = {}

        for i, num in enumerate(nums):
            diff = target - num
            if diff in seen:
                return [seen[diff], i]
            seen[num] = i

        return []


# -----------------------------------
# Brute Force Version
# -----------------------------------

class BruteForceSolution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)

        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]

        return []