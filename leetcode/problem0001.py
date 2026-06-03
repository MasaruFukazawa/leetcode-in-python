# -*- coding:utf-8 -*-

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        for idx1 in range(len(nums)):
            for idx2 in range(idx1 + 1, len(nums)):
                if (nums[idx1] + nums[idx2]) == target:
                    return [idx1, idx2]
                    