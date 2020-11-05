class Solution:
    def minCostToMoveChips(self, position):
        even = 0
        odd = 0
        # Parity here is the odd position or even position
        # If all the elements are in same parity
        # i.e all the position is odd or even
        # Then the answer is 0
        # Count the number of elements is each parity i.e even position and
        # odd position and return the elements which has the least value
        for i in position:
            if i % 2 == 0:
                even += 1
            else:
                odd += 1
        return (min(even, odd))


Solution.minCostToMoveChips("", [1,2,3])
Solution.minCostToMoveChips("", [2,2,2,3,3])
Solution.minCostToMoveChips("", [2,3,3])
Solution.minCostToMoveChips("", [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30])
Solution.minCostToMoveChips("", [1,2,2,2,2])