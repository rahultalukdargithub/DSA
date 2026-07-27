class Solution:
    def subarrayXor(self, arr, m):
        # code here
        dic=dict()
        x=0
        cnt=0
        for key,val in enumerate(arr):
            x^=val
            if x==m:
                cnt+=1
            if(dic.get(x^m,-1)!=-1):
                cnt+=dic[x^m]
            if(dic.get(x,-1)==-1):
                dic[x]=1
            else:
                dic[x]+=1
        return cnt        
