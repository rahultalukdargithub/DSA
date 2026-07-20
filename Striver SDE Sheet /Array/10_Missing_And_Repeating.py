class Solution:
    def findTwoElement(self, arr):
        # code here
        xr=0
        for i,val in enumerate(arr):
            xr= xr^(i+1)^val
        
        number= xr & ~(xr-1)
        club0=0
        club1=0
        for i,val in enumerate(arr):
            if((val & number) ==0):
                club0^=val
            else:
                club1^=val
            if(((i+1) & number) ==0):
                club0^=(i+1)
            else:
                club1^=(i+1)
        
        count=0
        for i,val in enumerate(arr):
            if(val == club0):
                count+=1
        if count==2:
            return [club0,club1]
        return [club1,club0]    
