/*
https://leetcode.com/problems/partition-labels/description/

A string S of lowercase letters is given. We want to partition this string into as many parts as possible so 
that each letter appears in at most one part, and return a list of integers representing the size of these parts. 
*/

import java.util.*;

class Solution {
    public List<Integer> partitionLabels(String S) {
        // K = the letter, V = Letter data object
        Map<Character, Letter> map = new HashMap<Character, Letter>();
        // track the order each character was added in
        List<Letter> order = new ArrayList<Letter>();
        
        
        for(int i = 0; i < S.length(); i++){
            // haven't seen this letter yet, map it, add to order
            char si = S.charAt(i);
            if( !map.containsKey(si) ){
                // assume this is only letter until proven otherwise (thus start and end are here)
                Letter newLetter = new Letter(si, i, i);
                map.put(si, newLetter);
                order.add(newLetter);
                
            }   
            // Have seen, therefore new end index
            else {
                map.get(si).setEnd(i);
            }
        }
        
        // Now we know every character in S and its first and last occurrence
        
        // parameters for partitions
        int currStart = 0, currEnd = 0;
        // iterator letter
        Letter currLet;
        // return array of partitions
        List<Integer> ret = new ArrayList<Integer>();
        // parameters of currLet
        int letStart, letEnd;
        
        for(int j = 0; j < order.size(); j++){
            // set iterator params
            currLet = order.get(j);
            letStart = currLet.getStart();
            letEnd = currLet.getEnd();
            
            // still within current partition?
            if(letStart <= currEnd){
                // need to extend partition end?
                if(letEnd > currEnd){
                    currEnd = letEnd;
                }  
            // reached end of partition, add to ret and start new partition
            } else if (letStart > currEnd){
                ret.add(currEnd - currStart + 1);
                currStart = letStart;
                currEnd = letEnd;
            }
        }
        ret.add(currEnd - currStart + 1);
        
        return ret;
    }
    // easily store all relevant information about letters to this problem
    private class Letter{
            private char letter;
            private int startI;
            private int endI;
            
            public Letter(char letter, int start, int end){
                this.letter = letter;
                this.startI = start;
                this.endI = end;
            }
            
            public boolean equals(Letter b){
                return (this.letter == b.getLetter());
            }
            
            public char getLetter(){
                return this.letter;
            }
            
            public int getStart(){
                return this.startI;
            }
            
            public int getEnd(){
                return this.endI;
            }
            
            public void setEnd(int e){
                this.endI = e;
            }
        }
}