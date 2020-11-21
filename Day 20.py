# Search in Rotated Sorted Array II

# Suppose an array sorted in ascending order is rotated at
# some pivot unknown to you beforehand.
#
# (i.e., [0,0,1,2,2,5,6] might become [2,5,6,0,0,1,2]).
#
# You are given a target value to search. If found in the
# array return true, otherwise return false.

# Example 1:
#
# Input: nums = [2,5,6,0,0,1,2], target = 0
# Output: true

# Example 2:
#
# Input: nums = [2,5,6,0,0,1,2], target = 3
# Output: false

#

"""class Solution:
    def search(self, nums, target):
        def helper(mid, target):
            for i in range(len(mid)):
                if nums[i] == target:
                    return True
            return False
        nums = sorted(nums)
        mid = len(nums)//2
        print(nums, nums[mid])
        if target >= nums[mid]:
            return(helper(nums[mid-1:], target))
        else:
            return(helper(nums[:mid], target))"""

class Solution:
    def search(self, nums, target):
        def helper(mid, target):
            for i in range(len(mid)):
                    if mid[i] == target:
                        return True
            return False
        if len(nums) == 0:
                return
        nums = sorted(nums)
        mid = len(nums)//2
        if target >= nums[mid]:
            return(helper(nums[mid:], target))
        else:
            return(helper(nums[:mid], target))

print(Solution.search("",[2,5,6,0,0,1], 2))