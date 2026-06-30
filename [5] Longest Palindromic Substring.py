'''
PROBLEM 5 (MEDIUM)
Longest Palindromic Substring

FOCUS
Two Pointers, String, Dynamic Programming

DESCRIPTION
Given a string "s", return the longest palindromic substring in "s".

DEFINITIONS
A substring is a contiguous non-empty sequence of characters within a string.
A string is palindromic if it reads the same forward and backward.

CONSTRAINTS
[1] 1 <= s.length <= 1000
[2] s consist of only digits and English letters.
'''

# SOLUTION
def longestPalindrome(self, s):
   if (len(s) <= 1):
       return s
  
   def determine_palindrome(left, right):
       while (left >= 0 and right < len(s) and s[left] == s[right]):
           left -= 1
           right += 1
      
       return s[(left + 1):right]


   longest = ''


   for i in range(len(s)):
       odd_palindrome = determine_palindrome(i, i)
       even_palindrome = determine_palindrome(i, i + 1)


       longest = max(longest, odd_palindrome, even_palindrome, key=len)


   return longest

'''
ANALYSIS
Time Complexity: O(n^2)
Space Complexity: O(n)
'''
