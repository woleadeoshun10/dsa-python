
"""
Problem: Group Anagrams
Pattern: Arrays & Hashing
Difficulty: Medium

Approach 1 (Optimized - Character Count)
Time Complexity: O(n * k)
Space Complexity: O(n * k)

Approach 2 (Sorting)
Time Complexity: O(n * k log k)
Space Complexity: O(n * k)

Key Insight:
Anagrams share identical character frequency distributions.
We use a tuple of character counts as a hashable key.
"""

from typing import List
from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        Optimized solution using 26-length frequency array.
        """
        group = defaultdict(list)

        for word in strs:
            count = [0] * 26

            for ch in word:
                index = ord(ch) - ord('a')
                count[index] += 1

            group[tuple(count)].append(word)

        return list(group.values())


# ------------------------------------------------------
# Alternative Approach (Sorting)
# ------------------------------------------------------

class SortingSolution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = defaultdict(list)

        for word in strs:
            key = "".join(sorted(word))
            group[key].append(word)

        return list(group.values())
