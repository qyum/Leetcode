class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        stack = []
        mapping = defaultdict(lambda: -1)

        for index, element in enumerate(nums2):
            while stack:
                top_element = stack[-1]
                #print(top_element)
                
                if element < top_element:
                    break

                mapping[top_element] = element
                #print(mapping)
                stack.pop()
                
            stack.append(element)

        #print(mapping)
        
        out = []
        for element in nums1:
            out.append(mapping[element])
        return out
