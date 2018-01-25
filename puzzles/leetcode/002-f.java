/*
https://leetcode.com/problems/add-two-numbers/description/

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of 
heir nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.
*/

/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        if( l1 == null || l2 == null){
            if (l1 == null) return l2;
            else return l1;
        }
        
        ListNode sum = new ListNode(10000); // obvious head indication value
        ListNode curr = sum;
        int digitSum = 0;
        int carry = 0;
        
        // continue summing while valid carry or l1,l2
        do{
            digitSum = sumNull(l1, l2, carry);
            carry = 0;
            
            // determine carry
            if ( digitSum >= 10){
                carry = 1;
                digitSum = digitSum % 10;
            }
            
            curr.next = new ListNode(digitSum);
            
            //prep for next sum
            l1 = (l1==null) ? null : l1.next;
            l2 = (l2==null) ? null : l2.next;
            curr = curr.next;
            
        }while(carry == 1 || (l1 != null && l2 != null));
        
        // no more carry bouncing, just determine end
        curr.next = (l1==null) ? l2 : l1; 
                                
        return sum.next;
    }
    
    // handle summing logic given potential for null ListNode Values
    private int sumNull(ListNode a, ListNode b, int carry){
        if(a == null){
            if(b == null) return carry;
            else return carry + b.val;
        } else {
            if(b == null) return carry + a.val;
            else return a.val + b.val + carry;
        }
    }
}