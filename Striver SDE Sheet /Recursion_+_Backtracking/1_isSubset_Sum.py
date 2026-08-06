
# For generating subsequences the process is same

class Solution:
    def r_ss(self,arr,su):
        if(su==0):
            return True
        if not arr:
            return False
        if(arr[0]<=su and self.r_ss(arr[1:],su-arr[0])):    
            return True
        if(self.r_ss(arr[1:],su)):
            return True
        return False    
    def isSubsetSum(self, arr: list[int], su: int) -> bool:
        # code here
        return self.r_ss(arr,su)
        
