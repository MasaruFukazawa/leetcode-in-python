#
# problems : mirror-distance-of-an-integer
#
class Solution:
    def mirrorDistance(self, n: int) -> int:
        return abs(n - int("".join(list(reversed(str(n))))))
