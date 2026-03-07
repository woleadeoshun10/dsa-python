"""
Problem: Longest Consecutive Sequence
Pattern: Arrays & Hashing
Difficulty: Medium

Approach 1 (Optimal - HashSet)
Time Complexity: O(n)
Space Complexity: O(n)

Approach 2 (Sorting)
Time Complexity: O(n log n)
Space Complexity: O(1) extra

Key Idea:
The optimal solution uses a set for O(1) lookups and only starts
counting when we find the beginning of a sequence (num - 1 not in set).
The sorting approach simply checks consecutive numbers after sorting.
"""

from typing import List


class Solution:
    """
    Optimal O(n) solution using a hash set
    """

    def longestConsecutive(self, nums: List[int]) -> int:

        num_set = set(nums)
        longest = 0

        for num in num_set:

            # start of sequence
            if num - 1 not in num_set:

                current = num
                length = 1

                while current + 1 in num_set:
                    current += 1
                    length += 1

                longest = max(longest, length)

        return longest


# ------------------------------------------------------
# Alternative Approach (Sorting)
# ------------------------------------------------------

class SortingSolution:
    """
    O(n log n) solution using sorting
    """

    def longestConsecutive(self, nums: List[int]) -> int:

        if not nums:
            return 0

        nums.sort()

        longest = 1
        current = 1

        for i in range(1, len(nums)):

            # skip duplicates
            if nums[i] == nums[i - 1]:
                continue

            # consecutive number
            if nums[i] == nums[i - 1] + 1:
                current += 1
            else:
                longest = max(longest, current)
                current = 1

        return max(longest, current)