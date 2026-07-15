class Solution:
    def nextPermutation(self, arr):
        # code here
        n=len(arr)-1
        ind=-1
        for i in range(n,0,-1):
            if(arr[i]>arr[i-1]):
                ind=i-1
                break
        if (ind==-1): 
            arr.reverse() 
            return
        for i in range(n,ind,-1):
            if(arr[i]>arr[ind]):
                arr[i],arr[ind]=arr[ind],arr[i]
                break
        
        arr[ind+1:n+1]=arr[ind+1:n+1][::-1] 
        return 
