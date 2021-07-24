class Solution(object):
    def longestMountain(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        
        maxlength=0
        
        i = 1
        while(i<len(arr)-1):
            peak = arr[i]>arr[i-1] and arr[i]>arr[i+1]
            if not peak:
                i += 1
                continue

            leftidx = i-2
            #print(arr[leftidx],arr[leftidx+1])
            
            while(leftidx >= 0 and arr[leftidx]<arr[leftidx+1]):
                leftidx -= 1

            #print(leftidx)
            rightidx = i+2
            
            #print(arr[rightidx],arr[rightidx-1])
            
            while(rightidx < len(arr) and arr[rightidx]<arr[rightidx-1]):
                rightidx += 1
            #print(rightidx)
            
            length = rightidx-leftidx-1
            if(length>maxlength):
                maxlength = length
            i = rightidx
        return maxlength
