# time complexity o(log n)

def bs(arr,l,r,target):
    
    while r>=l:
        mid=l+(r-l)//2
        
        #target is found in nums
        if arr[mid]==target:
            return mid
        #traverse right
        elif arr[mid]<arr[r]:
            if arr[mid]<target<=arr[r]:
                l=mid+1
            else:
                r=mid-1
        #traverse left
        else:
            if arr[l]<=target<arr[mid]:
                r=mid-1
            else:
                l=mid+1
                
    #target is not found in nums     
    else:
        return -1
            
        
            
            
        

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # 0(n) complexity
        
        #if target in nums:
            #return nums.index(target)
        #else:
            #return -1
        
        #..............binery search solution....................
        #nums=sorted(nums)
        #print(nums)
        out=bs(nums,0,len(nums)-1,target)
        print(out)
        return out
        
