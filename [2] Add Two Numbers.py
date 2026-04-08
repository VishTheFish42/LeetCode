'''
PROBLEM 2
Add Two Numbers


FOCUS
Linked List, Math, Recursion


DESCRIPTION
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each 
of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.


CONSTRAINTS
[1] The number of nodes in each linked list is in the range [1, 100].
[2] 0 <= Node.val <= 9
[3] It is guaranteed that the list represents a number that does not have leading zeros.
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def addTwoNumbers(l1, l2):
    total = ListNode()
    cur_total = total
    carry = 0
    cur_sum = carry

    while (l1 != None or l2 != None):
        if (l1 != None):
            cur_sum += l1.val
            l1 = l1.next
        if (l2 != None):
            cur_sum += l2.val
            l2 = l2.next

        cur_digit = cur_sum % 10
        cur_total.next = ListNode(val=cur_digit)
        cur_total = cur_total.next

        carry = cur_sum // 10
        cur_sum = carry

    if (cur_sum > 0):
        cur_total.next = ListNode(val=carry)

    return total.next
