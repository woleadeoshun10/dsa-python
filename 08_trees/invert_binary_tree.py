"""
Problem: Invert Binary Tree
Pattern: Tree / DFS
Difficulty: Easy

Approach:
Use Depth First Search (recursion).

For every node:
1. Swap its left and right children.
2. Recursively invert the left subtree.
3. Recursively invert the right subtree.

Time Complexity: O(n)
We visit every node exactly once.

Space Complexity: O(h)
Where h is the height of the tree (recursion stack).
Worst case O(n), average O(log n) for balanced trees.
"""

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        # base case
        if not root:
            return None

        # swap children
        root.left, root.right = root.right, root.left

        # recursively invert subtrees
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root