# Longest Mountain in Array

# Let's call any (contiguous) subarray B (of A) a mountain if the following properties hold:
#
# B.length >= 3
# There exists some 0 < i < B.length - 1 such that B[0] < B[1] < ... B[i-1] < B[i] > B[i+1] > ... > B[B.length - 1]
# (Note that B could be any subarray of A, including the entire array A.)
#
# Given an array A of integers, return the length of the longest mountain.
#
# Return 0 if there is no mountain.

# Example 1:
#
# Input: [2,1,4,7,3,2,5]
# Output: 5
# Explanation: The largest mountain is [1,4,7,3,2] which has length 5.
# Example 2:
#
# Input: [2,2,2]
# Output: 0
# Explanation: There is no mountain.

# Note:
#
# 0 <= A.length <= 10000
# 0 <= A[i] <= 10000

class Solution:
    def longestMountain(self, A):
        n = len(A)
        up, down = [0] * n, [0] * n
        for i in range(1, n):
            if A[i - 1] < A[i]:
                up[i] = up[i - 1] + 1
        for i in range(n - 1)[::-1]:
            if A[i] > A[i + 1]:
                down[i] = down[i + 1] + 1

        res = 0
        for i in range(n):
            if up[i] and down[i]:
                print(up[i], down[i])
        return res