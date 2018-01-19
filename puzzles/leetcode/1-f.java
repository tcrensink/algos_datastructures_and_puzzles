/*
https://leetcode.com/problems/two-sum/description/

Given an array of integers, return indices of the two numbers such that they add 
up to a specific target.

You may assume that each input would have exactly one solution, and you may not use 
the same element twice.
*/

import java.util.Hashtable;

class Solution {
    public int[] twoSum(int[] nums, int target) {
        Hashtable<Integer,Integer> table = new Hashtable<Integer,Integer>();
        
        for(int i = 0; i < nums.length; i++){
            table.put(nums[i], i);  // key = array value (so we can search on it), value = array index (so we can return it)
        }
        
        int x,y;
        
        for(int i = 0; i < nums.length; i++){
            x = nums[i];
            
            try {
                y = table.get(target - x);
                if (y != 0){
                    return new int[]{i,y};
                }
            }catch(NullPointerException e){}
            
            
        }
        
        return null;
        
    }
}