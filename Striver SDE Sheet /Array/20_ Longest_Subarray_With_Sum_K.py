# All Positive (most optimal)
def longestSubarrayWithSumK(a: [int], k: int) -> int:
    # Write your code here
    l=0
    r=0
    s=0
    ans=-1
    n=len(a)
    while(r<n):
        s+=a[r]
        while(l<=r and s>k):
            s-=a[l]
            l+=1
        if(s==k):
            ans=max(ans,r-l+1)
        r+=1
    return ans        

# Positive + negative number (most optimal for positive + negative and better approch for all positive) ,( k=0 )
class Solution:
    def longestSubarray(self, arr, k):  
        # code here
        dic=dict()
        s=0
        ans=-1
        for key,val in enumerate(arr):
            s+=val
            if(s==k):
                ans=max(ans,key+1)
            if(dic.get((s-k),-1)!=-1):
                ans=max(ans,key-dic[s-k])
            if(dic.get(s,-1)==-1):
                dic[s]=key
                
        return 0 if (ans==-1) else ans        

# Count the number of subarrays
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        dic=dict()
        s=0

        cnt=0
        for key,val in enumerate(nums):
            s+=val
            if(s==k):
                cnt+=1
            if(dic.get(s-k,-1)!=-1):
                cnt+=dic[s-k]
            if(dic.get(s,-1)==-1):
                dic[s]=1
            else:
                dic[s]+=1
        return cnt




        
