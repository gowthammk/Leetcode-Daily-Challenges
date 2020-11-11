# Valid Square

# Given the coordinates of four points in 2D space, return whether the four
# points could construct a square.
#
# The coordinate (x,y) of a point is represented by an integer array with two integers.
#
# Example:
#
# Input: p1 = [0,0], p2 = [1,1], p3 = [1,0], p4 = [0,1]
# Output: True

# Note:
#
# All the input integers are in the range [-10000, 10000].
# A valid square has four equal sides with positive length and four equal angles (90-degree angles).
# Input points have no order.
class Solution:
    def validSquare(self, p1, p2, p3, p4):
        # The property of a square is all the sides are equal and the diagonals are equal
        # We approach it by calculating the distance between all the given coordinates
        # (i.e) distance between coordinates p1 --> p2, p1 --> p3,
        # p1 --> p4, p2 --> p3, p2 --> p4, p3 --> p4.
        # if all the coordinates are same then it doesnot form a square
        if p1 == p2 == p3 == p4:
            return False

        # Function to calculate the distance between given two coordinates
        # The distance can be calculated as sqaure of first value of two coorinates added
        # to the square of second value of two coordinates
        def length(t1, t2):
            return (t1[0] - t2[0]) ** 2 + (t1[1] - t2[1]) ** 2

        #
        distance = ([length(p1, p2), length(p1, p3), length(p1, p4), length(p2, p3), length(p2, p4), length(p3, p4)])
        # As we know the distance between all the sides will be lesser than the distance between diagonals
        # we can sort the obtained distance to match the properties of a square
        sorteddistance = sorted(distance)
        # The sorted distance will have the first 4 values equal if it is a square
        # if this property is true then the last two values will be equal as the diagonals are equal

        if sorteddistance[0] == sorteddistance[1] == sorteddistance[2] == sorteddistance[3]:
            if sorteddistance[4] == sorteddistance[5]:
                return True
        return False