# -*- coding:utf-8 -*-

from leetcode.shuffle_the_array import Solution


def test_solution():
    solution = Solution()
    assert solution.shuffle([2, 5, 1, 3, 4, 7], 3) == [2, 3, 5, 4, 1, 7]
    assert solution.shuffle([1, 2, 3, 4, 4, 3, 2, 1], 4) == [1, 4, 2, 3, 3, 2, 4, 1]
    assert solution.shuffle([1, 1, 2, 2], 2) == [1, 2, 1, 2]
