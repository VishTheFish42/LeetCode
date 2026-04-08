'''
PROBLEM 1
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

def twoSum(nums, target):
    nums_hash = {}

    for index, num in enumerate(nums):
        num2 = target - num
        
        if (num2 in nums_hash):
            return [index, nums_hash[num2]]
        
        nums_hash[num] = index
