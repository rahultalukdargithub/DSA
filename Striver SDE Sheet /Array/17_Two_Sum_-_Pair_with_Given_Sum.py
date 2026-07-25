class Solution:
    def twoSum(self, nums, target):
        # code here
        nums.sort()
        start=0
        end=len(nums)-1
        ans=False
        while(start<end):
            s=nums[start]+nums[end]
            if(s==target):
                ans=True
                break
            elif(s>target):
                end-=1
            else:
                start+=1
        return ans        
