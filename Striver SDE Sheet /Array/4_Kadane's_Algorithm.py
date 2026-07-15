class Solution:
    def maxSubarraySum(self, arr):
        # Code here
        sum1=0
        ans=float('-inf')
        for i in range(len(arr)):
            sum1+=arr[i]
            ans=max(ans,sum1)
            if(sum1<=0): sum1=0
        return ans    
