class Solution:
    def moveZeroes(self, nums):
        if 0 not in nums:
            return nums
        
        zeros = 0
        i  = 0
        while nums[i] != 0:
            i+=1
        zeros = i
        i += 1
        while i < len(nums):
            if nums[i] != 0:
                nums[zeros] = nums[i]
                nums[i] = 0
                i+=1
                zeros+=1
            else:
                i += 1