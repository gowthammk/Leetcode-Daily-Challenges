# Mirror Reflection

# There is a special square room with mirrors on each of the four walls.
# Except for the southwest corner, there are receptors on each of the
# remaining corners, numbered 0, 1, and 2.
#
# The square room has walls of length p, and a laser ray from the
# southwest corner first meets the east wall at a distance q from the 0th receptor.
#
# Return the number of the receptor that the ray meets first.
# (It is guaranteed that the ray will meet a receptor eventually.)


# Input: p = 2, q = 1
# Output: 2
# Explanation: The ray meets receptor 2 the first time it
# gets reflected back to the left wall.

# The solution is using GCD
import  math
class Solution:
    def mirrorReflection(self, p: int, q: int) -> int:

        g = math.gcd(p, q)
        p = (p / g) % 2
        q = (q / g) % 2

        if p and q:
            return 1
        else:
            if p:
                return 0
            else:
                return 2

print(Solution.mirrorReflection("", 2, 1))