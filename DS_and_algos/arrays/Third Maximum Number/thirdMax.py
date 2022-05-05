class Solution:
    def thirdMax(self, nums):
        new_nums = set(nums)
        if len(new_nums)<3:
            return max(new_nums)
        new_nums = sorted(new_nums)
        return new_nums[-3]