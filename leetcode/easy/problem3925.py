#
# problems : concatenate-array-with-reverse
#


class Solution:
    def concatWithReverse(self, nums: list[int]) -> list[int]:
        return nums + list(reversed(nums))
