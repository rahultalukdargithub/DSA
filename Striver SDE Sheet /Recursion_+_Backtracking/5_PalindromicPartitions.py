class Solution:
    def isPalindrome(self,s):
        j=len(s)-1
        if(j==0): return True
        i=0
        while(i<=j):
            if(s[i]!=s[j]):
                return False
            i+=1
            j-=1
        return True        
    def fun(self,s,l,t):
        if(len(s)==0):
            l.append(t[:])
            return 
        for i in range(0,len(s)):
            if(self.isPalindrome(s[0:i+1])):
                t.append(s[0:i+1])
                self.fun(s[i+1:],l,t)
                t.pop()
        return         
    
    def palinParts(self, s):
        # code here
        l=list()
        self.fun(s,l,[])
        return l
        
