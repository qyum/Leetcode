class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        
        i=0
        s=set()
        while i<len(nums1):
            if nums1[i] in nums2:
                s.add(nums1[i])
            i+=1

        return list(s)
