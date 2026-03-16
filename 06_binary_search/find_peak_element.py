"""
Problem: Find Peak Element
Pattern: Binary Search
Difficulty: Medium

Description:
A peak element is an element that is greater than its neighbors.

Given an array nums, return the index of any peak element.
You may assume nums[-1] = nums[n] = -∞.

Example:
nums = [1,2,1,3,5,6,4]
Output: 5
Explanation: 6 is a peak element.

Approach:
Use binary search. If nums[mid] < nums[mid+1], the peak must be on the right.
Otherwise, the peak is on the left (including mid).

Time Complexity: O(log n)
Space Complexity: O(1)
"""


class Solution:
    def findPeakElement(self, nums):

        left = 0
        right = len(nums) - 1

        while left < right:

            mid = (left + right) // 2

            if nums[mid] < nums[mid + 1]:
                left = mid + 1
            else:
                right = mid

        return left


"""
nums = [1,2,1,3,5,6,4]
print(Solution().findPeakElement(nums))

output: 5

"""