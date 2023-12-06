# -*- coding:utf-8 -*-

from leetcode.number_of_good_pairs import Solution


def test_solution():
    solution = Solution()
    assert solution.numIdenticalPairs([1, 2, 3, 1, 1, 3]) == 4
    assert solution.numIdenticalPairs([1, 1, 1, 1]) == 6
    assert solution.numIdenticalPairs([1, 2, 3]) == 0
