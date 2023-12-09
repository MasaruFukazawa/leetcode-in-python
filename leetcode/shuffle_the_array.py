# -*- coding:utf-8 -*-


class Solution:
    def shuffle(self, nums: list[int], n: int) -> list[int]:
        return_list: list[int] = []

        x: list[int] = nums[:n]
        y: list[int] = nums[n:]

        for i in zip(x, y):
            return_list.extend(i)

        return return_list
