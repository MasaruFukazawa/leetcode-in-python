#
# problems : mirror-distance-of-an-integer
#
from leetcode.problem3783 import Solution


def test_solution():
    solution = Solution()
    assert solution.mirrorDistance(25) == 27
    assert solution.mirrorDistance(10) == 9
    assert solution.mirrorDistance(7) == 0
