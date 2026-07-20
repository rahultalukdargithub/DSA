class Solution:
    
    def merge(self,arr,start,mid,end):
        c=0
        i=start
        j=mid+1
        l=[]
        while(i<=mid and j<=end):
            if(arr[i]<=arr[j]):
                l.append(arr[i])
                i+=1
            elif(arr[i]>arr[j]):
                c+=mid-i+1
                l.append(arr[j])
                j+=1
        while(i<=mid):
            l.append(arr[i])
            i+=1
        while(j<=end):
            l.append(arr[j])
            j+=1
        b=0
        a=start
        n=len(l)
        while(b<n):
            arr[a]=l[b]
            a+=1
            b+=1
        return c    
    
    def mergesorthelper(self,arr,start,end):
        cnt=0
        if(start>=end):
            return cnt
        mid=(start+end)//2
        cnt+=self.mergesorthelper(arr,start,mid)
        cnt+=self.mergesorthelper(arr,mid+1,end)                            
        cnt+=self.merge(arr,start,mid,end)
        return cnt
    
    def inversionCount(self, arr):
        # code here
        return self.mergesorthelper(arr,0,len(arr)-1)
        
