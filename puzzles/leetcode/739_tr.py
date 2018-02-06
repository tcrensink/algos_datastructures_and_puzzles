class Solution:
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        """
        simple first:
        - double for loop, look for higher value, else return zero:
        """
#         # slow solution:
#         next_higher = [0]*len(temperatures)
#         for j in range(len(temperatures)):
#             for k in range(j, len(temperatures)):                
#                 if temperatures[k] > temperatures[j]:    
#                     next_higher[j] = k-j
#                     break
#         return next_higher        
        """
        1) loop through array, adding dict entry pool_dict[temp] = index.
        2) with each new element, split off all entries for which temp < temp[j]:
            - create tmp dict on above condition, k, v -> j: (j - j_init)
        3) convert tmp dict to array, return
        """
        from collections import defaultdict
        pool_dict = defaultdict(list)
        soln_dict = dict()
        soln_list = [0]*len(temperatures)
        tmp_dict = dict()
        
        for j, temp in enumerate(temperatures):
            
            pool_dict[temp].append(j)
            
            j_inits = [v for k, v in pool_dict.items() if k < temp]
            j_inits = [j for sublist in j_inits for j in sublist]
            n_days = [j - j_init for j_init in j_inits]            
            soln_dict = {**soln_dict, **dict(zip(j_inits, n_days))}
            pool_dict = defaultdict(list,{k:v for k, v in pool_dict.items() if k >= temp})
                 
        for k, v in soln_dict.items():    
            soln_list[k] = v
            
        return soln_list
                
            
            