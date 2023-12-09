# -*- coding:utf-8 -*-

from leetcode.find_words_containing_character import Solution


def test_solution():
    solution = Solution()
    assert solution.findWordsContaining(["leet", "code"], "e") == [0, 1]
    assert solution.findWordsContaining(["abc", "bcd", "aaaa", "cbc"], "a") == [0, 2]
    assert solution.findWordsContaining(["abc", "bcd", "aaaa", "cbc"], "z") == []
