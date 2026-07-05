class Solution(object):
    def bubblesortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n=len(nums)-1
        for i in range(n):
            for j in range(n-i):
                if (nums[j]>nums[j+1]):
                    nums[j],nums[j+1]=nums[j+1],nums[j]

        return nums   

    def selectionsortArray(self, nums):
        n=len(nums)
        for i in range(1,n):
            curr_min=i-1
            for j in range(i,n):
                if (nums[j]<nums[curr_min]):
                    curr_min=j
            nums[i-1],nums[curr_min]=nums[curr_min],nums[i-1]        

        return nums 
        
    def insertionsortArray(self, nums):
        n=len(nums)
        for i in range(1,n):
            j=i
            while(j!=0 and nums[j]<=nums[j-1]):
                nums[j],nums[j-1]=nums[j-1],nums[j]
                j=j-1

        return nums 
    
    def merge(self,start,mid,end,nums):
        i=start
        j=mid
        k=mid+1
        l=end
        res=[]
        while(i<=j and k<=l):
            if(nums[i]<nums[k]):
                res.append(nums[i])
                i=i+1
            elif(nums[i]>nums[k]):
                res.append(nums[k])
                k=k+1
            else: 
                res.append(nums[i])
                res.append(nums[k])
                i=i+1
                k=k+1
        while(i<=j):
            res.append(nums[i])
            i=i+1
        while(k<=l):
            res.append(nums[k])
            k=k+1
        n=len(res)  
        a=0  
        while(start<=end):
            nums[start]=res[a]
            a=a+1
            start=start+1
        return            


    def mergesorthelper(self, start,end,nums):
        if(start>=end):
            return 
        mid=(start+end)//2
        self.mergesorthelper(start,mid,nums)     
        self.mergesorthelper(mid+1,end,nums)
        self.merge(start,mid,end,nums)
        return 
    
    def pivot_element_index_finder(self,start,end,nums):
        pivotelemnt=nums[end]
        i=start
        j=end-1
        while(i<=j):
            if(nums[i]<pivotelemnt):
                i=i+1
            if(nums[j]>pivotelemnt):
                j=j-1
            if( (nums[i]>pivotelemnt)and(nums[j]<pivotelemnt)):
                nums[i],nums[j]=nums[j],nums[i]
                i=i+1
                j=j-1  
        nums[i],nums[end]=nums[end],nums[i]
        return i          
    def quicksorthelper(self,start,end,nums):
        if(start>end):
            return
        pivot_element_index=self.pivot_element_index_finder(start,end,nums)
        self.quicksorthelper(start,pivot_element_index-1,nums)
        self.quicksorthelper(pivot_element_index+1,end,nums)
        return 
    def sortArray(self, nums):
        self.quicksorthelper(0,len(nums)-1,nums)
        return nums                       


        
