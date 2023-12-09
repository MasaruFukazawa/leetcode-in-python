# -*- coding:utf-8 -*-

from leetcode.convert_the_temperature import Solution


def test_solution():
    solution = Solution()
    assert solution.convertTemperature(36.50) == [309.65000, 97.70000]
    assert solution.convertTemperature(122.11) == [395.26000, 251.79800]
