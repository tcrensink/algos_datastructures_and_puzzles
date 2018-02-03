/*
https://leetcode.com/problems/partition-labels/description/

A string S of lowercase letters is given. We want to partition this string into as many parts as possible so 
that each letter appears in at most one part, and return a list of integers representing the size of these parts. 
*/

class Solution {
    public List<Integer> partitionLabels(String S) {
        // last indicies of each character that occurs
        int[] map = new int[26];

        
        // set end index to current index of the occurring letter
        for(int i = 0; i < S.length(); i++){
            map[S.charAt(i) - 'a'] = i;
            
        }
        
        // Now we know every character in S's last occurrence
        
        // parameters for partitions
        int currStart = 0, currEnd = 0;
        // iterator letter
        char currLet;
        // parameters of currLet
        int letEnd;
        // return array of partitions
        List<Integer> ret = new ArrayList<Integer>();
        
        for(int j = 0; j < S.length(); j++){
            // set iterator params
            currLet = S.charAt(j);
            // need to set new end?
            currEnd = Math.max(map[currLet - 'a'], currEnd);
            
            // reached end of partition, add to ret and start new partition
            if (j >= currEnd){
                ret.add(currEnd - currStart + 1);
                currStart = currEnd + 1;
            }
        }
        
        return ret;
    }
}