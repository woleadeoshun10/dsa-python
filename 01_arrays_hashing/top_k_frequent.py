"""
Problem: Top K Frequent Elements
Pattern: Arrays & Hashing
Difficulty: Medium

Approach 1: Bucket Sort (Optimal)
Time Complexity: O(n)
Space Complexity: O(n)

Approach 2: Sorting
Time Complexity: O(n log n)
Space Complexity: O(n)

Key Insight:
Bucket sort avoids full sorting by using frequency as index.
"""

from typing import List


# ------------------------------------------------------
# Approach 1 — Bucket Sort (Optimal)
# ------------------------------------------------------

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for _ in range(len(nums) + 1)]

        # Count frequencies
        for num in nums:
            count[num] = 1 + count.get(num, 0)

        # Fill buckets
        for num, c in count.items():
            freq[c].append(num)

        # Collect top k
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res

        return res


# ------------------------------------------------------
# Approach 2 — Sorting
# ------------------------------------------------------

class SortingSolution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        # Count frequencies
        for num in nums:
            count[num] = 1 + count.get(num, 0)

        # Sort by frequency (descending)
        sorted_nums = sorted(count.keys(), key=lambda x: count[x], reverse=True)

        return sorted_nums[:k]