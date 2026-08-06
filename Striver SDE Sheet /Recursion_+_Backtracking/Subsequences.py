class Solution:
    def r_ss_tail(self,s,l,t):
        if(len(s)==0):
            l.append(t)
            return
        self.r_ss_tail(s[1:],l,t+s[0])
        self.r_ss_tail(s[1:],l,t)
        return 
    
    def r_ss_head(self,s,l):
        if(len(s)==0):
            return l
        sa=self.r_ss_head(s[1:],l)
        a=s[0]
        l.extend([a+x for x in sa])
        return l
            
	def powerSet(self, s):
		# Code here
		l=[""]
		l=self.r_ss_head(s,l)
		l.sort()
		return l
		
