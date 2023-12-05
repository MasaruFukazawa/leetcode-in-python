# -*- coding:utf-8 -*-

from leetcode.build_array_from_permutation import Solution


def test_solution():
    solution = Solution()
    assert solution.buildArray([0, 2, 1, 5, 3, 4]) == [0, 1, 2, 4, 5, 3]
    assert solution.buildArray([5, 0, 1, 2, 3, 4]) == [4, 5, 0, 1, 2, 3]
