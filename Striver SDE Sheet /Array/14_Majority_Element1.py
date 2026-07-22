class Solution:
    def majorityElement(self, arr):
        #code here
        cnt=0
        el=0
        for i,val in enumerate(arr):
            if(cnt==0):
                cnt=1
                el=val
            elif(el==val):
                cnt+=1
            elif(el!=val):
                cnt-=1
        n=len(arr)//2
        for val in arr:
            if(val==el):
                n-=1
        return el if(n<0) else -1        
