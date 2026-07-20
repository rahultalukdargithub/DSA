class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        freq={}
        for i,val in enumerate(nums):
            freq[val]=freq.get(val,0)+1
        ans =0
        for key,val in freq.items():
            if val>1 : 
                ans= key  
                break
        return ans          
        # slow=0
        # fast=0
        # while(True):
        #     slow=nums[slow]
        #     fast=nums[nums[fast]]
        #     if(slow==fast): break

        # slow=0
        # while(slow!=fast):
        #     slow=nums[slow]
        #     fast=nums[fast]
        # return slow        
        
