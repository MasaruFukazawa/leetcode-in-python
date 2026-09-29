#
# problems : concatenate-array-with-reverse
#
from leetcode.easy.problem3925 import Solution


def test_solution():
    solution = Solution()
    assert solution.concatWithReverse([1, 2, 3]) == [1, 2, 3, 3, 2, 1]
    assert solution.concatWithReverse([1]) == [1, 1]
