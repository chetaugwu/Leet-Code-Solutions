class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3: return False
        #determine start of the mountain
        if arr[0]>=arr[1]:
            return False
        dir = "incr"
        for i in range(1,len(arr)-1):
            if arr[i] == arr[i+1]: return False
            
            if dir == "incr":
                if arr[i] > arr[i+1]:
                    dir = "dec"
            else:
                if arr[i] < arr[i+1]:
                    return False
        
        if dir == "incr": return False
        
        return True