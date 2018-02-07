class Solution:
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        """
        - if current square is a '1', recursively explore adjacent squares
        - first, verify that current j,k values are in bounds
        - here, stop condition is moved to end of recursive function for brevity
        """
        jmax = len(grid)
        kmax = len(grid[0])
        max_area = 0
        
        def explore(j,k):
            
            if 0 <= j < jmax and 0 <= k < kmax and grid[j][k] == 1:
        
                grid[j][k] = 0
                return  1 + explore(j+1,k) + explore(j-1,k) + explore(j,k+1) + explore(j,k-1)
            
            return 0
        
         
        for j in range(jmax):
            for k in range(kmax):                
                max_area = max(max_area, explore(j,k))
        
        return max_area
            