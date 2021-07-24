class Solution(object):
    def circularArrayLoop(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
         
        n=len(nums)
        visited=set()
        
        for i in range(n):
            
            #if nums is not visited,then start traverse
            if i not in visited:
                local_s = set()
                #print(local_s)
                while True:
                    #if revisted in index then return true
                    if i in local_s: 
                        return True
                    #print(i)
                    visited.add(i)
                    local_s.add(i)
                    
                    prev, i = i, (i + nums[i]) % n
                    print(i)
                    if prev == i or (nums[i] > 0) != (nums[prev] > 0) : 
                        break
        #print(visited)
        return False
