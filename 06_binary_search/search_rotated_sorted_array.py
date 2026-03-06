"""
Problem: Search in Rotated Sorted Array
Pattern: Binary Search
Difficulty: Medium

Time Complexity: O(log n)
Binary search halves the search space each step.

Space Complexity: O(1)

Key Idea:
Even though the array is rotated, one half of the array
around the midpoint will always be sorted. We determine
which half is sorted and check if the target lies within it.
"""

def search(nums, target):
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        # if we found the target
        if nums[mid] == target:
            return mid

        if nums[left] <= nums[mid]:
            # target lies in the sorted left half
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1

        #otherwise in right sorted half
        else:
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1

    # wasnt found
    return -1


