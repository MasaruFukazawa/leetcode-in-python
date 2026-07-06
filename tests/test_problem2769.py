#
# problems : find-the-maximum-achievable-number
#
from leetcode.problem2769 import Solution


def test_solution():
    solution = Solution()
    assert solution.theMaximumAchievableX(4, 1) == 6
    assert solution.theMaximumAchievableX(3, 2) == 7
