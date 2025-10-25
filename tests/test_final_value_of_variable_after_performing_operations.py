# -*- coding:utf-8 -*-

from leetcode.final_value_of_variable_after_performing_operations import \
    Solution


def test_solution():
    solution = Solution()
    assert solution.finalValueAfterOperations(["--X", "X++", "X++"]) == 1
    assert solution.finalValueAfterOperations(["++X", "++X", "X++"]) == 3
