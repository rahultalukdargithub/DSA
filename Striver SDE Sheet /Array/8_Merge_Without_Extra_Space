
class Solution:
    def swap(self,l1,l2,i,j):
        if(l1[i]>l2[j]):
            l1[i],l2[j]=l2[j],l1[i]
    def mergeArrays(self, a, b):
        n = len(a)
        m = len(b)
        gap = (n+m)//2 + (n+m)%2 
        while(gap>0):
            i=0
            j=gap
            while(j<n+m):
                if(i<n and j<n):
                    self.swap(a,a,i,j)
                elif(i<n and (j>=n and j<n+m)):
                    self.swap(a,b,i,j-n)
                elif((i>=n and i<n+m) and (j>=n and j<n+m)):
                    self.swap(b,b,i-n,j-n)
                i+=1
                j+=1
            if(gap==1): break
            gap=gap//2 + (gap%2)
    # def mergeArrays(self, a, b):
    #     # code here
    #     n = len(a)
    #     m = len(b)
    #     i=n-1
    #     j=0
    #     while(i>=0 and j<m):
    #         if(a[i]>b[j]):
    #             a[i],b[j]=b[j],a[i]
    #         else:
    #             break
    #         i=i-1
    #         j=j+1
    #     a.sort()
    #     b.sort()
