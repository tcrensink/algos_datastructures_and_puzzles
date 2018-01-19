/*
https://leetcode.com/problems/merge-two-binary-trees/description/

Given two binary trees and imagine that when you put one of them to cover the other, 
some nodes of the two trees are overlapped while the others are not.

You need to merge them into a new binary tree. The merge rule is that if two nodes 
overlap, then sum node values up as the new value of the merged node. Otherwise, 
the NOT null node will be used as the node of new tree.
*/

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
    public TreeNode mergeTrees(TreeNode t1, TreeNode t2) {
        // One or both of the trees has no more children, return the subtree that exists or null
        if( t1 == null || t2 == null){
            if(t1 != null) return t1;
            
            else if (t2 != null) return t2;
            
            else return null;                
        }
        TreeNode root = new TreeNode(t1.val + t2.val);
        root.left = mergeTrees(t1.left, t2.left);
        root.right = mergeTrees(t1.right, t2.right);
        return root;
    }
}