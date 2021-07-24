#time complexity o(logn)+space complexity0(1)

class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        total = lambda k: (1+k)*k//2
        #print(total)
        l=0
        r=n
        best = 0
    
    
        while l<=r:
            m = (l+r)//2
            s = total(m)
            print(s)
            
            if s<=n:
                best = m
                l = m + 1 #Check if bigger numbers also work
            else:
                r = m - 1 #m was too high
                
        return best
