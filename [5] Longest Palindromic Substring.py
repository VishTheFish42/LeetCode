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
EXPLANATION
[1] We can simply return the string if it has one character or less.
[2] We define a function determine_palindrome() that starts from indices left and right and extends out to obtain the longest possible palindrome. 
    The indices left and right are the same for an odd number of characters and one apart for an even number of characters.
[3] We iterate across each character in the string. We initialize longest to a blank string.
[4] We calculate the longest odd-length palindrome (centered at the current character) and the longest even-length palindrome (centered at the current character and the next). 
    We set longest to be the max length string out of the current value of longest and the discovered odd and even palindrome.
[5] Once the loop ends, we return longest.

ANALYSIS
Time Complexity: O(n^2)
Space Complexity: O(n)
'''
