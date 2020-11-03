# Given a string s, the power of the string is the
# maximum length of a non-empty substring that contains
# only one unique character.

# Return the power of the string.

# Example 1:

# Input: s = "leetcode"
# Output: 2
# Explanation: The substring "ee" is of length 2 with the character 'e' only.

#Example 2:

#Input: s = "abbcccddddeeeeedcba"
#Output: 5
#Explanation: The substring "eeeee" is of length 5 with the character 'e' only.
#Example 3:

#Input: s = "triplepillooooow"
#Output: 5
#Example 4:

#Input: s = "hooraaaaaaaaaaay"
#Output: 11
#Example 5:

#Input: s = "tourist"
#Output: 1

class Solution:
    def maxPower(self, s):
        count = 1
        maximum = 1
        for i in range(0, len(s) - 1):
            if (s[i] == s[i + 1]):
                count += 1
                maximum = max(maximum, count)
            elif (s[i] != s[i + 1]):
                count = 1
        return maximum



Solution.maxPower("", "leetcode")
Solution.maxPower("", "abbcccddddeeeeedcba")
Solution.maxPower("", "triplepillooooow")
Solution.maxPower("", "hooraaaaaaaaaaay")
Solution.maxPower("", "tourist")
Solution.maxPower("", "cc")

