# -*- coding:utf-8 -*-

from typing import Dict


class Solution:
    def sumDivisibleByK(self, nums: List[int], k: int) -> int:
        return_value: int = 0
        nums_counter: Dict[int, int] = {}

        for i in nums:
            nums_counter[i] = nums_counter.get(i, 0) + 1

        for key, value in nums_counter.items():
            if 0 == (value % k):
                return_value += key * value

        return return_value
