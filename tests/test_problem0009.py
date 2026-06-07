# -*- coding:utf-8 -*-

from leetcode.problem0009 import Solution


def test_solution():
    solution = Solution()
    assert solution.isPalindrome(121) is True
    assert solution.isPalindrome(-121) is False
    assert solution.isPalindrome(10) is False
