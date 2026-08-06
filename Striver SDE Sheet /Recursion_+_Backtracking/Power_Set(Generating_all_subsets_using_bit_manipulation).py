class Solution:
    def powerSet(self, s):
       #code here
        l=list()
        n=len(s)
        num_subsets=pow(2,n)
        for i in range(num_subsets):
            st=""
            for j in range(n):
                if(i & (1<<j)):
                    st=s[n-1-j]+st
            l.append(st)
        return l    
