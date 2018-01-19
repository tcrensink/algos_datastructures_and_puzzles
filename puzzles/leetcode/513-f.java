/*
https://leetcode.com/problems/find-bottom-left-tree-value/description/

Given a binary tree, find the leftmost value in the last row of the tree.
*/

import java.util.LinkedList;

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
    public int findBottomLeftValue(TreeNode root) {
        LinkedList<TreeNode> q = new LinkedList<TreeNode>();
        q.add(root);
        return fbl(q).val;
    }
    /**
    * BFS from right to left (so left is always added last)
    */
    public TreeNode fbl(LinkedList<TreeNode> q) {
        TreeNode node = q.pop();
        if(node.right != null){
            q.add(node.right);
        }
        if(node.left != null){
            q.add(node.left);
        }
        if(q.isEmpty()){
            return node;
        }
        
        return fbl(q);
        
    }
}