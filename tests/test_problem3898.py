#
# problems : find-the-degree-of-each-vertex
#
from leetcode.problem3898 import Solution


def test_solution():
    solution = Solution()
    assert solution.findDegrees([[0, 1, 1], [1, 0, 1], [1, 1, 0]]) == [2, 2, 2]
    assert solution.findDegrees([[0, 1, 0], [1, 0, 0], [0, 0, 0]]) == [1, 1, 0]
    assert solution.findDegrees([[0]]) == [0]
