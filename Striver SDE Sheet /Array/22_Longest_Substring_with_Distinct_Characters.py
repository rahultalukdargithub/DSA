class Solution:
    def longestUniqueSubstr(self, s):
        # code her\
        dic=dict()
        l=0
        r=0
        n=len(s)
        ans=-1
        while(r<n):
            if(dic.get(s[r],-1)==-1):
                dic[s[r]]=r
            else:
                ans=max(ans,r-l)
                l=max(dic[s[r]]+1,l)
                dic[s[r]]=r
            r+=1
        return max(ans,r-l)    
