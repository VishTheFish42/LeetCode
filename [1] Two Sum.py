'''
PROBLEM 1 (EASY)
Two Sum

FOCUS
Array, Hash Table

DESCRIPTION
Given an array of integers "nums" and an integer "target", return indices of the two numbers such that they add up to "target".
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

CONSTRAINTS
[1] 2 <= nums.length <= 10^4
[2] -10^9 <= nums[i] <= 10^9
[3] -10^9 <= target <= 10^9
[4] Only one valid answer exists.
'''

# SOLUTION
def twoSum(nums, target):
    nums_hash = {}

    for index, num in enumerate(nums):
        num2 = target - num
        
        if (num2 in nums_hash):
            return [index, nums_hash[num2]]
        
        nums_hash[num] = index

'''
EXPLANATION
[1] We first create a hash table of each number mapped to its index.
[2] We iterate across each of these mappings and calculate the other number needed to create a sum. 
    If that number is in the hash table, we can return the current index being iterated on along with the mapping.
[3] Otherwise, we add the new number mapped to its index.

ANALYSIS
Time Complexity: O(n)
Space Complexity: O(n)
'''

'''
FOLLOW-UP
Can you come up with an algorithm that is less than O(n^2) time complexity?
'''
