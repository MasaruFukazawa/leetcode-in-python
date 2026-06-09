#
# problems : find-the-degree-of-each-vertex
#
from leetcode.problem3512 import Solution


def test_solution():
    solution = Solution()
    assert solution.minOperations([6, 13], 13) == 6
    assert solution.minOperations([3, 9, 7], 5) == 4
    assert solution.minOperations([4, 1, 3], 4) == 0
    assert solution.minOperations([3, 2], 6) == 5
