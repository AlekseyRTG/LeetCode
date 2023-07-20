# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

# The overall run time complexity should be O(log (m+n)).

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        nums = nums1 + nums2
        nums.sort()
        if len(nums) % 2 == 0:
            index = len(nums) / 2
            median = (nums[index] + nums[index - 1]) / 2.0
        else: median = nums[len(nums) / 2]
        return median
    