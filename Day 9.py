# Maximum Difference Between Node and Ancestor

# Given the root of a binary tree, find the maximum value V for which there
# exist different nodes A and B where V = |A.val - B.val| and A is an ancestor of B.
# A node A is an ancestor of B if either: any child of A is equal to B, or any child
# of A is an ancestor of B.

# Input: root = [8,3,10,1,6,null,14,null,null,4,7,13]
# Output: 7
# Explanation: We have various ancestor-node differences, some of which are given below :
# |8 - 3| = 5
# |3 - 7| = 4
# |8 - 1| = 7
# |10 - 13| = 3
# Among all possible differences, the maximum value of 7 is obtained by |8 - 1| = 7.


# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right


# It is a binary tree, So, all the elements to the left is lesser than the root
# All the element in the right is greater than the root.
# To minimize the time, we will do recursion if the difference of max and min value is
# greater than the previous value.
class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        self.difference = 0
        def diff(node, cur_max, cur_min):
            if not node:
                return 0
            else:
                self.difference = max(self.difference, abs(node.val - cur_min), abs(node.val - cur_max))
                cur_min = min(cur_min, node.val)
                cur_max = max(cur_max, node.val)
                diff(node.left, cur_max, cur_min)
                diff(node.right, cur_max, cur_min)
        diff(root, root.val, root.val)
        return self.difference

