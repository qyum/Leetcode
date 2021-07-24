class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums=sorted(nums)
        l=0
        r=len(nums)-1
        
        if len(nums)<2:
            out=[str(i) for i in nums]
            out=''.join(out)
            return out
        elif len(nums)>1 and len(nums)<3:
            if nums[l]<nums[r]:
                return nums[l]
        else:
            while r>=l:
                mid=l+(r-l)//2

                if nums[mid]>nums[l] :
                    return nums[l]
                r=mid-1
