from collections import Counter

class Solution:
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        """
        create a set J (hash table)
        create a dict of occurences in C (hash table/ dict)
        loop over items in c
        """
        s = set(J)
        c = Counter(S)
        n = 0
        
        for k, v in c.items():
            if k in s:
                n += v   
        return n