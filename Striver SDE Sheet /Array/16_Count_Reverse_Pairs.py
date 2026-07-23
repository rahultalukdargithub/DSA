class Solution:
    def merge(self,arr, low, mid, high):
        temp = []  # temporary array
        left = low  # starting index of left half of arr
        right = mid + 1  # starting index of right half of arr
    
        # storing elements in the temporary array in a sorted manner
        while left <= mid and right <= high:
            if arr[left] <= arr[right]:
                temp.append(arr[left])
                left += 1
            else:
                temp.append(arr[right])
                right += 1
    
        # if elements on the left half are still left
        while left <= mid:
            temp.append(arr[left])
            left += 1
    
        # if elements on the right half are still left
        while right <= high:
            temp.append(arr[right])
            right += 1
    
        # transferring all elements from temporary to arr
        for i in range(low, high + 1):
            arr[i] = temp[i - low]
    
    def countPairs(self,arr, low, mid, high):
        right = mid + 1
        rightend=high
        cnt = 0
        left=low
        leftend=mid
        for i in range(right,rightend+1):
            while(left<=leftend and arr[left]<=(2*arr[i])):
                left+=1
            cnt+=mid-left+1   
        return cnt
    
    def mergeSort(self,arr, low, high):
        cnt = 0
        if low >= high:
            return cnt
        mid = (low + high) // 2
        cnt += self.mergeSort(arr, low, mid)  # left half
        cnt += self.mergeSort(arr, mid + 1, high)  # right half
        cnt += self.countPairs(arr, low, mid, high)  # Modification
        self.merge(arr, low, mid, high)  # merging sorted halves
        return cnt

    def countRevPairs(self, arr):
        # Code here
        return self.mergeSort(arr,0,len(arr)-1)
        
