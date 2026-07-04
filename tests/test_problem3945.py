#
# problems : digit-frequency-score
#
from leetcode.problem3945 import Solution


def test_solution():
    solution = Solution()
    assert solution.digitFrequencyScore(122) == 5
    assert solution.digitFrequencyScore(101) == 2
