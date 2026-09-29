#
# problems : 2894. Divisible and Non-divisible Sums Difference
#
from leetcode.easy.problem2894 import Solution


def test_solution():
    solution = Solution()
    assert solution.differenceOfSums(10, 3) == 19
    assert solution.differenceOfSums(5, 6) == 15
    assert solution.differenceOfSums(5, 1) == -15
