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