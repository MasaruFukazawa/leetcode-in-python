# -*- coding:utf-8 -*-

from leetcode.defanging_an_ip_address import Solution


def test_solution():
    solution = Solution()
    assert solution.defangIPaddr("1.1.1.1") == "1[.]1[.]1[.]1"
    assert solution.defangIPaddr("255.100.50.0") == "255[.]100[.]50[.]0"
