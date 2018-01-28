class Solution:
    def anagramMappings(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        dictB = {B[j]:j for j in range(0,len(B))}
        return [dictB[j] for j in A]