class Solution:
    def comb(self,arr,target,l,t):
        if(target==0):
            l.append(t[:])
            return 
        for i in range(len(arr)):
            if(i!=0 and arr[i]==arr[i-1]): continue
            if(target>=arr[i]):
                t.append(arr[i])
                self.comb(arr[i+1:],target-arr[i],l,t)
                t.pop()
        return    
    def uniqueCombinations(self, arr, target):
        # code here
        arr.sort()
        l=list()
        self.comb(arr,target,l,[])
        return l
        
