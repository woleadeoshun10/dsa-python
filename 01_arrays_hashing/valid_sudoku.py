"""
Problem: Valid Sudoku

Determine if a 9x9 Sudoku board is valid.

Rules:
1. Each row must contain digits 1–9 without repetition.
2. Each column must contain digits 1–9 without repetition.
3. Each 3x3 sub-box must contain digits 1–9 without repetition.

Time Complexity:
O(1)
The board size is fixed (9x9).

Space Complexity:
O(1)
At most 81 entries stored across sets.
"""

from typing import List
from collections import defaultdict


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)

        for r in range(9):
            for c in range(9):

                value = board[r][c]

                if value == ".":
                    continue

                if (
                    value in rows[r]
                    or value in cols[c]
                    or value in squares[(r // 3, c // 3)]
                ):
                    return False

                rows[r].add(value)
                cols[c].add(value)
                squares[(r // 3, c // 3)].add(value)

        return True