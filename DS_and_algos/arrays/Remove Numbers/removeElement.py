class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        j = len(nums)-1
        i = 0
        while i<=j:
            if nums[i]==val:
                temp = nums[i]
                nums[i] = nums[j]
                nums[j] = "x"
                del nums[j]
                j-=1
            else:
                i+=1
        