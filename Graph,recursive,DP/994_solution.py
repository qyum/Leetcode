class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
         
        m=len(grid)
        n=len(grid[0])
        l=0
        
        rot=[]
        for i in range(m):
            for j in range(n):
                if grid[i][j]==2:    
                    rot.append([i,j,l])
                    
        def convert(c,d,l):
            nonlocal rot
            if c<0 or c>=m or d<0 or d>=n or grid[c][d]==0:
                return
            if grid[c][d]==1:
                rot.append([c,d,l+1])
                grid[c][d]=0
    
                    
        while rot:  
            a,b,l = rot.pop(0)
            grid[a][b] = 0
           
            convert(a-1,b,l) #top
            convert(a+1,b,l) #bottom
            convert(a,b-1,l) #left
            convert(a,b+1,l)  #right
            
        # Checking any 1 exist in grid
        for r in grid:
            if 1 in r:
                return -1

        return l
