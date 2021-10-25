#dynamic programming problem
#recursive memoization solution

class Solution:
    def numTrees(self, n: int) -> int:
        memo={}
        
        def uniqueBinaryTreeHelper(start,end):
            #base case
            if start>=end or start <1:
                return 1
            
            
            count=0
            if (start,end) in memo:
                return memo[(start,end)]
            else:
                for idx in range(start,end+1):
                    count+=uniqueBinaryTreeHelper(start,idx-1)\
                    *uniqueBinaryTreeHelper(idx+1,end)
                memo[(start,end)]=count   
                return count
        
        return uniqueBinaryTreeHelper(1,n)

    
