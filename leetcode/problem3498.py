#
# problems : Reverse Degree of a String
#
class Solution:
    def reverseDegree(self, s: str) -> int:

        sum: int = 0

        for i, c in enumerate(s, start=1):
            sum += (ord("z") - ord(c) + 1) * i

        return sum
