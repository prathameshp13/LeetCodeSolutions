#!/usr/local/bin/python3

"""
Leetcode Problem 21. Merge Two Sorted Lists

Merge two sorted linked lists and return it as a sorted list.
The list should be made by splicing together the nodes of the first two lists.
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        head =  ListNode()
        start = head
        while l1 and l2:
            if l1.val < l2.val:
                head.next = l1
                l1 = l1.next
            else:
                head.next = l2
                l2 = l2.next
            head = head.next
                
        if l1:
                head.next = l1
        elif l2:
                head.next = l2
                
        return start.next