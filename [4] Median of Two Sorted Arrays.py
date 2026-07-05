'''
PROBLEM 4 (HARD)
Median of Two Sorted Arrays

FOCUS
Array, Binary Search, Divide and Conquer
 
DESCRIPTION
Given two sorted arrays "nums1" and "nums2" of size "m" and "n" respectively, return the median of the two sorted arrays.
The overall run time complexity should be O(log (m+n)).

CONSTRAINTS
[1] nums1.length == m
[2] nums2.length == n
[3] 0 <= m <= 1000
[4] 0 <= n <= 1000
[5] 1 <= m + n <= 2000
[6] -10^6 <= nums1[i], nums2[i] <= 10^6
'''

# SOLUTION
def findMedianSortedArrays(nums1, nums2):
    if (len(nums1) > len(nums2)):
        temp = nums2
        nums2 = nums1
        nums1 = temp

    m = len(nums1)
    n = len(nums2)

    left = 0
    right = len(nums1)
    i = (left + right) / 2

    j = ((m + n + 1) / 2) - i

    max_left1 = nums1[i - 1]  if i > 0 else float('-inf')
    min_right1 = nums1[i]     if i < m else float('inf')
    max_left2  = nums2[j - 1] if j > 0 else float('-inf')
    min_right2 = nums2[j]     if j < n else float('inf')

    while ((max_left1 > min_right2) or (max_left2 > min_right1)):
        if (max_left1 > min_right2):
            right = i - 1
        else:
            left = i + 1

        i = (left + right) // 2
        j = ((m + n + 1) // 2) - i

        max_left1 = nums1[i - 1]  if i > 0 else float('-inf')
        min_right1 = nums1[i]     if i < m else float('inf')
        max_left2 = nums2[j - 1]  if j > 0 else float('-inf')
        min_right2 = nums2[j]     if j < n else float('inf')

    if ((m + n) % 2 == 1):
        return max(max_left1, max_left2)
    else:
        return (max(max_left1, max_left2) + min(min_right1, min_right2)) / 2.0

'''
EXPLANATION
[1] First, we ensure that the shorter array is stored in nums1. 
[2] We have two pointers left and right to traverse nums1. We also have partitions i and j to split nums1 and nums2, respectively. 
    The elements at indices i and j are included in the right side of each array.
[3] We set the maximum of the left and the minimum of the right of each array to respective variables. We know we have the correct partition, 
    when the minimum of the right of one array is greater than the maximum of the left of the other array in both ways.
[4] Until this is reached, we move right to i - 1 if the maximum of the left of nums1 is greater than minimum of the right of nums1, 
    and we move left to i + 1 if the opposite condition is true.
[5] We then recalculate i and j and the maximum of right and minimum of left for each array.
[6] Outside of the loop, if there are an odd number of elements total, the median is simply the higher of the maximums of left. 
    Otherwise, it is the sum of the higher of the maximums of left and the lower of the minimums of right, all divided by 2.

ANALYSIS
Time Complexity: O(log(min(m, n)))
Space Complexity: O(1)
'''
