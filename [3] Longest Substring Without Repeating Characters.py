'''
PROBLEM 3 (MEDIUM)
Longest Substring Without Repeating Characters

FOCUS
Hash Table, String, Sliding Window

DESCRIPTION
Given a string "s", find the length of the longest substring without duplicate characters.

DEFINITIONS
A substring is a contiguous non-empty sequence of characters within a string.

CONSTRAINTS
[1] 0 <= s.length <= 5 * 10^4
[2] s consists of English letters, digits, symbols and spaces.
'''

# SOLUTION
def lengthOfLongestSubstring(s):
   if (len(s) <= 1):
       return len(s)
  
   start = 0
   end = 0
   max_length = 1
   s_last_seen_hash = {s[0]: 0}


   for i in range(1, len(s)):
       if (s[i] not in s_last_seen_hash):
           end = i
       else:
           if (start >= (s_last_seen_hash[s[i]] + 1)):
               end = i
           else:
               start = s_last_seen_hash[s[i]] + 1


       if (end - start + 1 > max_length):
           max_length = end - start + 1

       s_last_seen_hash[s[i]] = i
  
   return max_length

'''
EXPLANATION
[1] We simply return the length of s if it is 0 or 1 (since that substring must be the longest with no duplicate characters).
[2] Otherwise, we initialize two pointers start and end, max_length as 1, and a hash table with the first letter mapped to index 0 
    (this hash table tracks the last index we see a certain character).
[3] We iterate across each character in the string starting from the second. If the letter is not in the hash table, end is set to the current index.
[4] Otherwise, we have seen the letter before. If start is greater than one more than the last seen index of that letter, end is set to the current index. 
    Otherwise, start is set to the the last index of the letter + 1.
[5] If the current length of the substring (given by start and end) is greater than max_length, we set max_length to the new length.
[6] We set the last seen index of the current letter to the current index.
[7] Outside of the loop, we return max_length.

ANALYSIS
Time Complexity: O(n)
Space Complexity: O(n)
'''
