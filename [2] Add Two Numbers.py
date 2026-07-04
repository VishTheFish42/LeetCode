'''
PROBLEM 2 (MEDIUM)
Add Two Numbers

FOCUS
Linked List, Math, Recursion

DESCRIPTION
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.
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

# SOLUTION
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

'''
EXPLANATION
[1] Initialize total as a new ListNode as well as cur_total and cur_sum.
[2] We iterate through this process while either l1 or l2 is None. If either one is None on the current iteration, 
    we add val of that appropriate list to cur_sum and move to the next node in that list.
[3] We set cur_digit to the sum % 10. After initializing the next node of cur_total to a ListNode with val as cur_digit, we set cur_total to this next node.
[4] We set carry to cur_sum // 10 and cur_sum to carry.
[5] Once we exit the while loop, if cur_sum is greater than 0, then we set the next node of cur_total to a new ListNode with val as carry.
[6] Finally, we return the next node of total.

ANALYSIS
Let n be the length of l1 and m be the length of l2.
Time Complexity: O(max(n, m))
Space Complexity: O(max(n, m))
'''
