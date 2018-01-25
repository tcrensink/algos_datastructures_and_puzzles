import java.util.ArrayList;
import java.util.Stack;

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
    public List<Integer> inorderTraversal(TreeNode root) {
        if(root == null) return new ArrayList<Integer>();
        
        ArrayList<Integer> result = new ArrayList<Integer>(); 
        Stack<TreeNode> stack = new Stack<TreeNode>();
        
        TreeNode curr = root;
        
        while(curr != null || !stack.isEmpty()){
            // find left most of this branch
            while(curr != null){
                stack.push(curr);
                curr = curr.left;
            }
            
            // curr is now null, left is at top of stack
            curr = stack.pop();
            result.add(curr.val);   // visit
            curr = curr.right;    // go right
            
        }
        
        return result;
        
        
    }
    
   
}