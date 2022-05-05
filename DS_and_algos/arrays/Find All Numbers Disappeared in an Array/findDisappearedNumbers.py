class Solution:
    def findDisappearedNumbers(self, nums):
        store = []
        for i in nums:
            ind = abs(i)-1
            if nums[ind] > 0:
                nums[ind] *= -1
        for i in range(len(nums)):
            if nums[i] > 0:
                store.append(i+1)
                
        return store