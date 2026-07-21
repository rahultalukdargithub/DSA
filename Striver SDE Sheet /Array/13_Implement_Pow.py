class Solution:
    def poww(self,b,e):
        if(e==0):
            return 1
        if(e==1):
            return b
        if(e%2==0):
            return self.poww(b*b,e//2)
        return b*self.poww(b,e-1)    
    def power(self, b: float, e: int) -> float:
        # Code Here
        if(e<0):
            return 1.0/self.poww(b,-e)
        return self.poww(b,e)
