"""
Problem: Reverse Linked List
Pattern: Linked List
Difficulty: Easy

Approach: Iterative Pointer Reversal

Time Complexity: O(n)
We traverse the list once.

Space Complexity: O(1)
We only use a few pointers.

Key Idea:
Traverse the linked list and reverse each node's pointer
so it points to the previous node instead of the next one.
"""

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        prev, curr = None, head

        while curr:
            next_node = curr.next      # store next node
            curr.next = prev           # reverse pointer
            prev = curr                # move prev forward
            curr = next_node           # move curr forward

        return prev