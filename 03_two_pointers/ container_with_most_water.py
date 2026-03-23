"""
Problem: Container With Most Water
Pattern: Two Pointers
Difficulty: Medium

Description:
Given an integer array heights, where heights[i] represents the height
of a vertical line at index i, find two lines that together with the x-axis
form a container that holds the most water.

Return the maximum amount of water a container can store.

Approach:
Use two pointers (left, right).
- Calculate area using width * min(height[left], height[right]).
- Move the pointer pointing to the smaller height inward,
  because that limits the area.

Time Complexity: O(n)
Space Complexity: O(1)
"""


from typing import List


class Solution:
    def maxArea(self, heights: List[int]) -> int:

        left = 0
        right = len(heights) - 1
        maxArea = 0

        while left < right:

            width = right - left
            height = min(heights[left], heights[right])
            area = width * height

            maxArea = max(maxArea, area)

            # move the pointer with smaller height
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1

        return maxArea


