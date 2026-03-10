"""
Problem: Two Sum II – Input Array Is Sorted
Pattern: Two Pointers
Difficulty: Medium

You are given a 1-indexed array of integers numbers that is already sorted in
non-decreasing order.

Find two numbers such that they add up to a specific target number and return
their indices (1-indexed).

There is exactly one solution, and you may not use the same element twice.

Approach 1 (Optimal – Two Pointers)
Time Complexity: O(n)
Space Complexity: O(1)

Key Insight:
Since the array is sorted, we can use two pointers from both ends.
If the sum is too large → move right pointer left.
If the sum is too small → move left pointer right.
"""

from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        left, right = 0, len(numbers) - 1

        while left < right:
            currSum = numbers[left] + numbers[right]

            if currSum > target:
                right -= 1
            elif currSum < target:
                left += 1
            else:
                return [left + 1, right + 1]

        return []


# ------------------------------------------------------
# Alternative Approach (Brute Force)
# ------------------------------------------------------

"""
Approach 2 (Brute Force)
Time Complexity: O(n²)
Space Complexity: O(1)
"""


class BruteForceSolution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        for i in range(len(numbers)):
            for j in range(i + 1, len(numbers)):
                if numbers[i] + numbers[j] == target:
                    return [i + 1, j + 1]

        return []