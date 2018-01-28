class Solution:
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        # create a dict with key: ncol - nrow
        # if value exists, should be same, else return False 
        diagonal_value = dict()
        for j, row in enumerate(matrix):
            for k, value in enumerate(row):
                key = k - j
                if key not in diagonal_value:
                    diagonal_value[key] = value    
                else:
                    if diagonal_value[key] != value:
                        return False        
        return True