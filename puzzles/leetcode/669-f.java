/*
https://leetcode.com/problems/trim-a-binary-search-tree/description/

Given a binary search tree and the lowest and highest boundaries as L and R, trim 
the tree so that all its elements lies in [L, R] (R >= L). You might need to change 
the root of the tree, so the result should return the new root of the trimmed binary 
search tree.
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
    public TreeNode trimBST(TreeNode root, int L, int R) {
        if( root == null) return null;
        
        int val = root.val;
        
        if( val < L ){  // Know nothing to the left will satisfy
            return trimBST(root.right, L, R);
        } else if (val > R) {
            return trimBST(root.left, L, R);
            
        } else {
            root.left = trimBST(root.left, L, R);
            root.right = trimBST(root.right, L, R);
            return root;
        }
        
    }
}