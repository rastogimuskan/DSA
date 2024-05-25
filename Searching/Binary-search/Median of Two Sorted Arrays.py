class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        start = 0
        end = len(nums1)
        n1 = len(nums1)
        n2 = len(nums2)

        while(start <= end):
            i1 = (start+end)//2
            i2 = ((n1+n2+1)//2) - i1
            max1 = float('-inf') if i1 == 0 else nums1[i1 - 1]
            min1 = float('inf') if i1 == n1 else nums1[i1]
            max2 = float('-inf') if i2 == 0 else nums2[i2 - 1]
            min2 = float('inf') if i2 == n2 else nums2[i2]

            if (max2 <= min1 and max1 <= min2):
                if (n1+n2)%2 == 0:
                    return (max(max1,max2)+ min(min1,min2))/2.0
                else:
                    return max(max1, max2)
            elif max1 > min2:
                end = i1 - 1
            else:
                start = i1 + 1
        

# https://www.youtube.com/watch?v=F9c7LpRZWVQ

#  Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

# The overall run time complexity should be O(log (m+n))

# Example 1:

# Input: nums1 = [1,3], nums2 = [2]
# Output: 2.00000
# Explanation: merged array = [1,2,3] and median is 2.
# Example 2:

# Input: nums1 = [1,2], nums2 = [3,4]
# Output: 2.50000
# Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
 
