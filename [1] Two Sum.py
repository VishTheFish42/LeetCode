'''
Problem 1 - Two Sum
'''

def twoSum(nums, target):
    nums_hash = {}

    for index, num in enumerate(nums):
        num2 = target - num
        if num2 in nums_hash:
            return [index, nums_hash[num2]]
        nums_hash[num] = index
