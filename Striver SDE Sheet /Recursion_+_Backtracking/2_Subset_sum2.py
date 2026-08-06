class Solution:
    def comb(self,arr,l,t):
        l.append(t[:])
        for i in range(len(arr)):
            if(i!=0 and arr[i]==arr[i-1]): 
                continue
            t.append(arr[i])
            self.comb(arr[i+1:],l,t)
            t.pop()
    def findSubsets(self, arr):
        # code here
        arr.sort()
        l=list()
        self.comb(arr,l,[])
        return l
