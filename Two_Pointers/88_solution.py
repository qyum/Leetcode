class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        
        
        """
        
        #num1=[ nums1.pop(ele) if ele==0 else ele for ele in nums1]
        
        #num1=[]
        #for ele in range(0,len(nums1)-1):
            #print(ele)
            #if nums1[ele]==0:
                #nums1.pop(nums1[ele])
            #print(ele)
            #else:
                #print(num3[ele])
                #num1.append(nums1[ele])
         
        #num3=num1+nums2
        #num3=sorted(num3)
        #print(num3)
        #return num3
        
        nums1[m:]= nums2[:n]
        print(nums1[m:])
        nums1.sort()
