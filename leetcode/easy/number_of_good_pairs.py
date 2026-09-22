# -*- coding:utf-8 -*-


class Solution:
    def numIdenticalPairs(self, nums: list[int]) -> int:
        nums_len: int = len(nums)
        nums_set_len: int = len(set(nums))

        if nums_len == nums_set_len:
            return 0

        match_count: int = 0

        for i in range(nums_len - 1):
            for j in range(i + 1, nums_len):
                if nums[i] == nums[j]:
                    match_count += 1

        return match_count
