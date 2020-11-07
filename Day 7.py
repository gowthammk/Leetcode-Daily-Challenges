# You are given two non-empty linked lists representing two non-negative integers.
# The most significant digit comes first and each of their nodes contain a single digit.
# Add the two numbers and return it as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Follow up:
# What if you cannot modify the input lists? In other words,
# reversing the lists is not allowed.

# Example:

# Input: (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 8 -> 0 -> 7

#################################################################################################
#################################################################################################
#################################################################################################
#################################################################################################

# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

# Adding two numbers
class Solution:
    def addTwoNumbers(self, l1, l2):
        stack_1 = []
        stack_2 = []
        while l1 is not None:
            stack_1.append(l1)
            l1 = l1.next
        while l2 is not None:
            stack_2.append(l2)
            l2 = l2.next

        carry = 0
        head = None
        while stack_1 or stack_2:
            # Pop the elements in the linked list so that we can do addition from right to left
            v1 = stack_1.pop().val if stack_1 else 0
            v2 = stack_2.pop().val if stack_2 else 0
            # Maintain a carry so that if the val is greater than 10, we can carry the "1" to the next
            val = v1 + v2 + carry
            carry = int(val / 10)
            val = int(val % 10)
            # Create a linked list starting with the first value
            temp = head
            head = ListNode(val)
            # Make the next of the value to Null, To maintain Singly Linked List
            # (The addition of the elements will be on the basis of adding element to the front)
            head.next = temp
        # If there is a carry in case l1 = [5], l2 = [5], then we should return [1,0]
        # Thus maintain a carry to make it simple.
        # The add the 1 at the front of the linked list
        if carry:
            temp = head
            head = ListNode(carry)
            head.next = temp
        return head

