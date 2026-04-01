"""
Problem: Trapping Rain Water
Pattern: Two Pointers
Difficulty: Hard

Description:
Given n non-negative integers representing an elevation map where the width
of each bar is 1, compute how much water it can trap after raining.

Approach:
Use two pointers (left, right) and track leftMax and rightMax.
- Water at a position depends on the smaller of leftMax and rightMax.
- Move the pointer with the smaller max inward.

Time Complexity: O(n)
Space Complexity: O(1)
"""

from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:

        if not height:
            return 0

        left = 0
        right = len(height) - 1

        leftMax = height[left]
        rightMax = height[right]

        totalWater = 0

        while left < right:

            if leftMax < rightMax:
                left += 1
                leftMax = max(leftMax, height[left])
                totalWater += leftMax - height[left]

            else:
                right -= 1
                rightMax = max(rightMax, height[right])
                totalWater += rightMax - height[right]

        return totalWater

