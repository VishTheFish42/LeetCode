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
ANALYSIS
Time Complexity: O(n)
Space Complexity: O(n)
where n is the length of s
'''
