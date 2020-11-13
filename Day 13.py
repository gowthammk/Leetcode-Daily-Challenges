# Populating Next Right Pointers in Each Node

# You are given a perfect binary tree where all leaves are on the same level, and every parent has two children. The binary tree has the following definition:
#
# struct Node {
#   int val;
#   Node *left;
#   Node *right;
#   Node *next;
# }

# Populate each next pointer to point to its next right node.
# If there is no next right node, the next pointer should be set to NULL.
#
# Initially, all next pointers are set to NULL.
#
#
#
# Follow up:
#
# You may only use constant extra space.
# Recursive approach is fine, you may assume implicit stack space does
# not count as extra space for this problem.

# Input: root = [1,2,3,4,5,6,7]
# Output: [1,#,2,3,#,4,5,6,7,#]
# Explanation: Given the above perfect binary tree (Figure A),
# your function should populate each next pointer to point to its next right node,
# \just like in Figure B. The serialized output is in level order as connected by the
# next pointers, with '#' signifying the end of each level.

"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root is not None:
            self.connectChildren(root)
        return root

    def getNextNodeForChild(self, node: 'Node') -> 'Node':
        while node is not None:
            if node.left:
                return node.left
            if node.right:
                return node.right
            node = node.next

    def connectChildren(self, node: 'Node') -> None:
        nextNode = self.getNextNodeForChild(node.next)
        if node.right is not None:
            node.right.next = nextNode
            self.connectChildren(node.right)
            nextNode = node.right
        if node.left is not None:
            node.left.next = nextNode
            self.connectChildren(node.left)