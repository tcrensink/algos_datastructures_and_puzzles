class Solution:
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        
        - loop over list
        - if left, right sets are distinct, add cut point to list
        - move start index to next
        
        Q: give a closer look to the indices in this problem
        """
        l = []
        j1 = 0
        for j2 in range(1, len(S) + 1):
            set1 = set(S[j1:j2])
            set2 = set(S[j2::])
            if set.intersection(set1, set2) == set():
                l.append(j2 -j1)
                j1 = j2
        return l
        