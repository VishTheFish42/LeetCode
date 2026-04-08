'''
PROBLEM 3
Longest Substring Without Repeating Characters

FOCUS
Hash Table, String, Sliding Window

DESCRIPTION
Given a string "s", find the length of the longest substring without duplicate characters.

CONSTRAINTS
[1] 0 <= s.length <= 5 * 10^4
[2] s consists of English letters, digits, symbols and spaces.
'''

def lengthOfLongestSubstring(s):
    if (len(s) <= 1):
        return len(s)
    
    start = 0
    end = 0
    max_length = 1
    s_letter_list = [s[0]]
    s_index_hash = {s[0]: 0}

    for i in range(1, len(s)):
        if (s[i] not in s_letter_list):
            s_letter_list.append(s[i])
            s_index_hash[s[i]] = i
            end = i

            if (end - start + 1 > max_length):
                max_length = end - start + 1

        else:
            if (s_letter_list.index(s[i]) == (len(s_letter_list) - 1)):
                start = i
                s_letter_list = []
                s_index_hash = {}
            else:
                start = s_index_hash[s[i]] + 1
                s_letter_list = s_letter_list[(s_letter_list.index(s[i]) + 1):]
            
            s_letter_list.append(s[i])
            s_index_hash[s[i]] = i

    return max_length
