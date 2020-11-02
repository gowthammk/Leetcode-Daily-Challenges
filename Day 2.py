# Algorithm of Insertion Sort:

# Insertion sort iterates, consuming one input element each repetition,
# and growing a sorted output list.
# At each iteration, insertion sort removes one element from the input data,
# finds the location it belongs within the sorted list, and inserts it there.
# It repeats until no input elements remain.
# Definition for singly-linked list.

class ListNode:
     def __init__(self, val=0, next = None):
         self.val = val
         self.next = next


class Solution:
    # Function to implement insertion sort
    def insertionSortList(self, head):
        # If there is no head then return None
        if head == None:
            return None
        # Else, create a new list called sortedList and assign head to it
        sortedList = head
        # Move the head pointer to next
        head = head.next
        # Sorted List is an empty list thus, the next element is assigned to None
        sortedList.next = None
        # Loop to go until end of head
        while head != None:
            current = head
            head = head.next
            if current.val < sortedList.val:
                # if the first element is less than second element then it is sorted
                # thus, maintain the linked list current.next link it to sortedLsit
                # and also, make the current pointer to point at the second element
                current.next = sortedList
                sortedList = current
            else:
                # If the value is greater then, create a new element search and assign sortedList
                search = sortedList
                while search.next != None and current.val > search.next.val:
                    search = search.next
                # When the loop exits which means it has either come to last element or
                # the value of current elemets is greater than search element
                # Thus, current's next is search's next
                # Search's next is current
                current.next = search.next
                search.next = current
        return sortedList

    #Function to print the list
    def print(self, values):
        s = ""
        while values is not None:
            s += str(values.val) + "->"
            values = values.next
        print(s[:-2])

list = Solution()
list.headval = ListNode(5)
e2 = ListNode(4)
e3 = ListNode(6)
e4 = ListNode(2)

list.headval.next = e2
e2.next = e3
e3.next = e4

l = list.headval

a = list.insertionSortList(l)
b = a
Solution.print(0, b)


