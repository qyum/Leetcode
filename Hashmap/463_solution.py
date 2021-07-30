class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        h=len(grid)
        w=len(grid[0])
        
        def dfs(r,c):
            if r<0 or r>=h or c<0 or c>=w or grid[r][c]==0:
                return 1
            if grid[r][c]==1:
                grid[r][c]=2
                return dfs(r-1,c)+ dfs(r+1,c)+dfs(r,c-1)+dfs(r,c+1)
            
            return 0
        
        pm=0
        for r in range(h):
            for c in range(w):
                if grid[r][c]==1:
                    pm+=dfs(r,c)
                
        return pm  
