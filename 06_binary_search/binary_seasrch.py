"""
Problem: Binary Search
Pattern: Binary Search
Difficulty: Easy

Time Complexity: O(log n)
Each iteration halves the search space.

Space Complexity: O(1)

Key Idea:
Compare target with middle element.
If smaller search left half, if larger search right half.
"""

from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:

        left, right = 0, len(nums) - 1

        while left <= right:

            mid = (left + right) // 2

            if nums[mid] == target:
                return mid

            elif nums[mid] < target:
                left = mid + 1

            else:
                right = mid - 1

        return -1