"""
Problem: Product of Array Except Self
Pattern: Arrays & Hashing
Difficulty: Medium

Approach: Prefix + Postfix Products
Time Complexity: O(n)
Space Complexity: O(1) extra space (output array not counted)

Key Insight:
For each index i, the result equals the product of all elements
before i multiplied by the product of all elements after i.

Instead of recomputing these values repeatedly, we compute
prefix products in one pass and postfix products in another pass.
"""

from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        Optimized solution using prefix and postfix products.
        """
        res = [1] * len(nums)

        # Prefix pass
        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]

        # Postfix pass
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]

        return res


# ------------------------------------------------------
# Alternative Approach (Brute Force)
# ------------------------------------------------------

class BruteForceSolution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []

        for i in range(len(nums)):
            prod = 1
            for j in range(len(nums)):
                if i != j:
                    prod *= nums[j]
            res.append(prod)

        return res

"""
Explanation

For each position i:
result[i] = product of all numbers before i * product of all numbers after i

We compute this using two passes:

1. Prefix pass
   res[i] stores product of elements before i

2. Postfix pass
   multiply res[i] by product of elements after i

Example:
nums = [1,2,4,6]

Prefix pass → [1,1,2,8]
Postfix pass → [48,24,12,8]

Final result = [48,24,12,8]

Time Complexity: O(n)
Space Complexity: O(1) extra space (output array not counted)
"""
