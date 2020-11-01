# Definition for singly-linked list.
#Given head which is a reference node to a singly-linked list.
# The value of each node in the linked list is either 0 or 1.
# The linked list holds the binary representation of a number.

#Return the decimal value of the number in the linked list.

#Input: head = [1,0,1]
#Output: 5
#Explanation: (101) in base 2 = (5) in base 10

#Input: head = [1,0,0,1,0,0,1,1,1,0,0,0,0,0,0]
#Output: 18880

class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution:
    def __init__(self):
        self.headval = None

    # Function returns Converted Binary Number in a Linked List to an Integer
    def getDecimalValue(self):
        # String to maintain elements in a Linked List
        values = ""
        printval = self.headval
        # Traverse till end of Linked List
        while printval is not None:
            # Store all the values of Linked List
            values += str(printval.val)
            printval = printval.next
        # Converts binary number to integer
        return (int(values, 2))

# Sample creation and insertion of linked list
# We can insert custom test cases and execute
# In this I have executed second test case
# and the output is correctly matched
list = Solution()
list.headval = ListNode(1)
e2 = ListNode(0)
e3 = ListNode(0)
e4 = ListNode(1)
e5 = ListNode(0)
e6 = ListNode(0)
e7 = ListNode(1)
e8 = ListNode(1)
e9 = ListNode(1)
e10 = ListNode(0)
e11 = ListNode(0)
e12 = ListNode(0)
e13 = ListNode(0)
e14 = ListNode(0)
e15 = ListNode(0)

list.headval.next = e2
e2.next = e3
e3.next = e4
e4.next = e5
e5.next = e6
e6.next = e7
e7.next = e8
e8.next = e9
e9.next = e10
e10.next = e11
e11.next = e12
e12.next = e13
e13.next = e14
e14.next = e15

#The result is as expected
result = list.getDecimalValue()
print(result)





