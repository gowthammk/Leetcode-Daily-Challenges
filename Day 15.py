# Range Sum of BST

# Given the root node of a binary search tree, return the
# sum of values of all nodes with a value in the range [low, high].

# Input: root = [10,5,15,3,7,null,18], low = 7, high = 15
# Output: 32

# Input: root = [10,5,15,3,7,13,18,1,null,6], low = 6, high = 10
# Output: 23

# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

# Solution using recursion
class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        self.res = 0

        def helper(node):
            if not node:
                return
            if node:
                if low <= node.val <= high:
                    self.res += node.val
                if low < node.val:
                    helper(node.left)
                if node.val < high:
                    helper(node.right)

        helper(root)
        return self.res
