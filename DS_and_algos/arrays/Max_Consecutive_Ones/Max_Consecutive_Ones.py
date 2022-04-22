def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        lis = ''.join(str(num) for num in nums)
        return len(max(lis.split('0')))