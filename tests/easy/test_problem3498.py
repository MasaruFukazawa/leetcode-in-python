#
# problems : Reverse Degree of a String
#
from leetcode.easy.problem3498 import Solution


def test_solution():
    solution = Solution()
    assert solution.reverseDegree("abc") == 148
    assert solution.reverseDegree("zaza") == 160
