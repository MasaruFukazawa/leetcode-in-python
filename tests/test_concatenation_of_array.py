# -*- coding:utf-8 -*-

from leetcode.concatenation_of_array import Solution


def test_solution():
    solution = Solution()

    solution.getConcatenation([1, 2, 1])
    assert solution.getConcatenation([1, 2, 1]) == [1, 2, 1, 1, 2, 1]

    solution.getConcatenation([1, 3, 2, 1])
    assert solution.getConcatenation([1, 3, 2, 1]) == [1, 3, 2, 1, 1, 3, 2, 1]
