#
# problems : minimum-operations-to-make-array-sum-divisible-by-k
#


class Solution:
    def minOperations(self, nums: list[int], k: int) -> int:

        return sum(nums) % k

        # if sum(nums) % k == 0:
        #    return 0
        # elif sum(nums) < k:
        #    return sum(nums)
        # count: int = 0
        # for i in range(len(nums)):
        #    while True:
        #        nums[i] = nums[i] - 1
        #        count += 1
        #        if sum(nums) % k == 0:
        #            return count
        #        if nums[i] == 0:
        #            break
