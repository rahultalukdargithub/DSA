class Solution:
    def mergeOverlap(self, arr):
        # Code here
        arr.sort()
        current_start=arr[0][0]
        current_end=arr[0][1]
        n=len(arr)
        ans=[]
        for i in range(1,n):
            a=arr[i][0]
            b=arr[i][1]
            if(current_end>=a and current_end<b):
                current_end=b
            elif(current_end>=a and current_end>=b):
                continue
            elif(current_end<a and current_end<b):
                ans.append([current_start,current_end])
                current_start=a
                current_end=b
         
        if(len(ans)==0 or current_start!=ans[len(ans)-1][0] and current_end!=ans[len(ans)-1][1]):
            ans.append([current_start,current_end])
             
         
        return ans    
                
        
