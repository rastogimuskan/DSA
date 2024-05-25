# Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

# There is only one repeated number in nums, return this repeated number.

# You must solve the problem without modifying the array nums and uses only constant extra space.

 
# Example 1:

# Input: nums = [1,3,4,2,2]
# Output: 2
# Example 2:

# Input: nums = [3,1,3,4,2]
# Output: 3
# Example 3:

# Input: nums = [3,3,3,3,3]
# Output: 3
 
#  Constraints:

# 1 <= n <= 105
# nums.length == n + 1
# 1 <= nums[i] <= n
# All the integers in nums appear only once except for precisely one integer which appears two or more times.
 

#brutforce approach
# def repeating_elements():
#     arr = [1,3,3,3,4,5]
#     n = len(arr)
#     validate = [False for i in range(n)]
#     for i in range(len(arr)):
#         if validate[arr[i]] == True:
#             return arr[i]
#         else:
#             validate[arr[i]] = True
# print(repeating_elements())

# O(n) time complexity and O(n) space complexity


####################### optimal solution ######################
# To solve this problem, we can use Floyd's Tortoise and Hare algorithm (also known as the cycle detection algorithm). This approach works by interpreting the array as a linked list and finding the cycle within it. Here's how you can apply it to find the repeated number:

# Phase 1: Finding the intersection point of the two runners:

# Use two pointers, the tortoise and the hare. The tortoise moves one step at a time, while the hare moves two steps at a time.
# Since there is a duplicate number, the two pointers will eventually meet inside the cycle.
# Phase 2: Finding the entrance to the cycle:

# Once the two pointers meet, we start a new pointer from the start of the array.
# Move both pointers one step at a time. The point where they meet is the entrance to the cycle, which is the duplicate number.

class Solution(object):
    def findDuplicate(self, nums):
        slow = 0
        fast = 0


        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if (slow == fast):

                break
        print(fast)
        slow = 0
        while(slow != fast):
            slow = nums[slow]
            fast = nums[fast]
        return slow

s1 = Solution()
s1.findDuplicate([3,1,3,4,2])