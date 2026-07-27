class Solution:
    def longestConsecutive(self, arr):
        # code here
        s=set(arr)
        ans=0
        for val in s:
            if val-1 not in s:
                cnt=1
                n=val
                while(n+1 in s):
                    cnt+=1
                    n=n+1
                ans=max(ans,cnt)
                
        return ans
