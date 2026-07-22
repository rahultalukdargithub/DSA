class Solution:
    def findMajority(self, arr):
        # code here
        cnt1=0
        el1=0
        cnt2=0
        el2=0
        for i,val in enumerate(arr):
            if(cnt1==0 and el2!=val):
                cnt1=1
                el1=val
            elif(cnt2==0 and el1!=val):
                cnt2=1
                el2=val    
            elif(el1==val):
                cnt1+=1
            elif(el2==val):
                cnt2+=1    
            else:
                cnt1-=1
                cnt2-=1    
        n1=len(arr)//3
     
        cnt1=0
        cnt2=0
        ans=[]
        for val in arr:
            if(val==el1): cnt1+=1
            if(val==el2): cnt2+=1
        if(cnt1>n1): ans.append(el1)
        if(cnt2>n1 and el2!=el1): ans.append(el2)  
        ans.sort()
        return ans
