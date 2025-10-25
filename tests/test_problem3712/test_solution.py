# -*- coding:utf-8 -*-

from leetcode.problem3712.solution import Solution


def test_solution():
    solution = Solution()
    assert 16 == solution.sumDivisibleByK([1, 2, 2, 3, 3, 3, 3, 4], 2)
    assert 0 == solution.sumDivisibleByK([1, 2, 3, 4, 5], 2)
    assert 12 == solution.sumDivisibleByK([4, 4, 4, 1, 2, 3], 3)
