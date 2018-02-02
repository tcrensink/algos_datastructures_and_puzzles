/*
Given the root of a tree, you are asked to find the most frequent subtree sum. The subtree sum of a node is defined 
as the sum of all the node values formed by the subtree rooted at that node (including the node itself). So what 
is the most frequent subtree sum value? If there is a tie, return all the values with the highest frequency in 
any order.
*/

import java.util.*;

/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class Solution {
    int count = 0;  // count of occurrences of max freq
    int maxFreq = 0;    // current max freq
    public int[] findFrequentTreeSum(TreeNode root) {
        // K = sum V = freq
        Map<Integer, Integer> map = new HashMap<Integer, Integer>();// base        

        // traverse tree
        findFrequentTreeSum(root, map);
        
        // return int[]
        int[] ret = new int[count];
        int freq, sum;
        
        // find all max sum freqs
        for(Map.Entry<Integer, Integer> entry : map.entrySet()){
            freq = entry.getValue();
            sum = entry.getKey();
            if(freq == maxFreq){
                ret[--count] = sum;
            }
        }
        
        return ret;
    }
    
    public int findFrequentTreeSum(TreeNode root, Map<Integer, Integer> map){
        if(root == null) return 0;
        int sum = root.val + findFrequentTreeSum(root.left, map) + findFrequentTreeSum(root.right, map);
        int currFreq = map.getOrDefault(sum,0) + 1;
        
        // New maxFreq
        if(currFreq > maxFreq){
            count = 1;
            maxFreq = currFreq;
        } 
        // Same freq, so update count
        else if (currFreq == maxFreq){
            count++;
        }
        
        map.put(sum, currFreq);
        return sum;
    }
}