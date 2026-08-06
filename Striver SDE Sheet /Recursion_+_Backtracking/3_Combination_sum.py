class Solution:
    def comb(self,arr,target,l,t):
        if(target==0):
            l.append(t[:])
            return
        if not arr:
            return
        if(target>=arr[0]):
            t.append(arr[0])
            self.comb(arr,target-arr[0],l,t)
            t.pop()
        self.comb(arr[1:],target,l,t)
        return 
    def targetSumComb(self, arr: list[int], target: int) -> list[list[int]]:
        # code here
        l=list()
        t=list()
        self.comb(arr,target,l,t)
        return l
        
