class Solution:
    def searchMatrix(self, mat, x): 
        # code here 
        n=len(mat[0])
        start=0
        end=(len(mat)*len(mat[0]))-1
        while(start<=end):
            mid=(start+end)//2
            r=mid//n
            c=mid%n
            if(mat[r][c]==x):
                return True
            elif(mat[r][c]>x):
                end=mid-1
            elif(mat[r][c]<x): 
                start=mid+1
        return False        
