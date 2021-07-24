class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        #..........two pointer solution.............
        
        left=0
        res=0
        product=1
        
        for right in range(len(nums)):
            product*=nums[right]
            
            #if product greater than k or equal, then move left pointer to right to decrease product
            if product>=k:
                while product>=k  and left<=right:
                    product/=nums[left]
                    left+=1
            res+=right-left+1
        return res
