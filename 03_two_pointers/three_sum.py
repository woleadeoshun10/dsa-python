"""
Problem: 3Sum
Pattern: Two Pointers
Difficulty: Medium

Description:
Given an integer array nums, return all unique triplets [nums[i], nums[j], nums[k]]
such that i != j, i != k, j != k, and nums[i] + nums[j] + nums[k] == 0.

The solution set must not contain duplicate triplets.

Approach:
1. Sort the array.
2. Fix one number nums[i].
3. Use two pointers (left, right) to find pairs such that:
   nums[i] + nums[left] + nums[right] == 0
4. Skip duplicates to avoid repeating triplets.

Time Complexity: O(n^2)
Space Complexity: O(1) (excluding output)
"""


class Solution:
    def threeSum(self, nums):

        nums.sort()
        result = []

        for i in range(len(nums)):

            # skip duplicate values for i
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left = i + 1
            right = len(nums) - 1

            while left < right:

                total = nums[i] + nums[left] + nums[right]

                if total < 0:
                    left += 1

                elif total > 0:
                    right -= 1

                else:
                    result.append([nums[i], nums[left], nums[right]])

                    left += 1
                    right -= 1

                    # skip duplicates for left pointer
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

        return result


# Example usage
nums = [-1, 0, 1, 2, -1, -4]
print(Solution().threeSum(nums))  # [[-1, -1, 2], [-1, 0, 1]]