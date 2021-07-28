class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
      
        left=bisect.bisect_left(nums,target)
        right=bisect.bisect_right(nums,target)
        
        print(left,right)
        if left<right:
            return [left,right-1]
        else:
            return [-1,-1]  
