class Solution:
    def comb(self,arr,l,t):
        # if we do l.append(t) then the reference goes so next time when we are poping out the value will get disturbed so we have to send a copy of t 
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
