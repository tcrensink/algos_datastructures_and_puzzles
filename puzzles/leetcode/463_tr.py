class Solution:
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
        # count all land squares
        count_val = 4*sum(val for row in grid for val in row)
        
        #count adjacencies, subtract two edges for each:
        for j, row in enumerate(grid):
            for k, val in enumerate(row):
                
                if j > 0 and grid[j][k] == 1 and grid[j-1][k] == 1:
                        count_val -= 2 
                if k > 0 and grid[j][k] == 1 and grid[j][k-1] == 1:
                        count_val -= 2 
                        
        return count_val