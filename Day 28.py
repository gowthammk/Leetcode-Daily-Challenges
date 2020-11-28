#  You are given an array of integers nums, there is a sliding
#  window of size k which is moving from the very left of the array
#  to the very right. You can only see the k numbers in the window.
#  Each time the sliding window moves right by one position.
#
# Return the max sliding window.
# Example 1:
#
# Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
# Output: [3,3,5,5,6,7]
# Explanation:
# Window position                Max
# ---------------               -----
# [1  3  -1] -3  5  3  6  7       3
#  1 [3  -1  -3] 5  3  6  7       3
#  1  3 [-1  -3  5] 3  6  7       5
#  1  3  -1 [-3  5  3] 6  7       5
#  1  3  -1  -3 [5  3  6] 7       6
#  1  3  -1  -3  5 [3  6  7]      7
# Example 2:
#
# Input: nums = [1], k = 1
# Output: [1]
# Example 3:
#
# Input: nums = [1,-1], k = 1
# Output: [1,-1]
# Example 4:
#
# Input: nums = [9,11], k = 2
# Output: [11]
# Example 5:
#
# Input: nums = [4,-2], k = 2
# Output: [4]

class Solution:
    def maxSlidingWindow(self, nums, k):
        if not nums or not k:
            return []
        dq, res = [], []
        for i in range(k):
            while dq and nums[i] > nums[dq[-1]]:
                dq.pop()
            dq.append(i)
        for i in range(k, len(nums)):
            res.append(nums[dq[0]])
            if i-k+1 > dq[0]:
                dq.pop(0)
            while dq and nums[i] > nums[dq[-1]]:
                dq.pop()
            dq.append(i)
        res.append(nums[dq[0]])
        return res
