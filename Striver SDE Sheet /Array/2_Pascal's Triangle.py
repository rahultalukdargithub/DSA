class Solution:
    def generate(self, n: int) -> List[List[int]]:
        ans=list()
        for i in range(0,n):
            s=[1]
            sa=1
            l=1
            for j in range(0,i):
                sa*=(i-j)
                l*=(1+j)
                s.append(sa//l)
            ans.append(s)
        return ans
