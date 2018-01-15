/*
https://leetcode.com/problems/maximum-binary-tree/description/

Given an integer array with no duplicates. A maximum tree building on this array is defined as follow:

The root is the maximum number in the array.
The left subtree is the maximum tree constructed from left part subarray divided by the maximum number.
The right subtree is the maximum tree constructed from right part subarray divided by the maximum number.
Construct the maximum tree by the given array and output the root node of this tree.
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
    public TreeNode constructMaximumBinaryTree(int[] nums) {
        TreeNode root = new TreeNode(nums[0]);
        
        for(int i = 1; i < nums.length; i++ ){        // O(n) n = nums.length
            TreeNode curr = new TreeNode(nums[i]);
            if( curr.val > root.val){    // if new biggest
                // old root becomes new root left child
                curr.left = root;
                root = curr;
            }
            else { // not new biggest, add to right and resolve right tree
                root.right = resolve(root.right, curr);
            }
            
        }

        // O(n) * O(n) WORST = O(n^2) O(n) * O(logn) AVERAGE = O(nlogn)
        
        return root;
    }
    
    public TreeNode resolve(TreeNode root, TreeNode node){  // O(n) WORST CASE O(logn) average case
        // base case for right traversal
        if (root == null) {
            return node;
        }
        else if(root.val > node.val){   // no replace, keep going down
            root.right = resolve(root.right, node);
            return root;
        }
        else { // new biggest, old root becomes left child
            node.left = root;
            root = null;
            return node;
        }
    }
    
}