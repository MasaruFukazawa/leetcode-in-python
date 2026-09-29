#
# problems : 3110. Score of a String
#
from leetcode.easy.problem3110 import Solution


def test_solution():
    solution = Solution()
    assert solution.scoreOfString("hello") == 13
    assert solution.scoreOfString("zaz") == 50
