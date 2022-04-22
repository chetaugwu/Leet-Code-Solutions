class Solution:
    def checkIfExist(self, arr):
        for i in range(len(arr)):
            if arr[i] == 0:
                if arr[i] in arr[:i] or arr[i] in arr[i+1:]:
                    return True
            elif arr[i]*2 in arr:
                return True
        return False