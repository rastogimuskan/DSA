#https://www.youtube.com/watch?v=nP_ns3uSh80

# Boyer-Moore Voting Algorithm
# Phase 1: Find a Candidate

# Initialize candidate and count to None and 0, respectively.
# Iterate through the array:
# If count is 0, set the candidate to the current element and count to 1.
# If the current element is the same as candidate, increment count by 1.
# Otherwise, decrement count by 1.
# Phase 2: Verify the Candidate

# After identifying a candidate, count its occurrences in the array to verify if it is indeed the majority element.

#User function template for Python 3

class Solution:
    def majorityElement(self, arr, N):
        candidate, count = None, 0
        
        for num in arr:
            if count == 0:
                candidate = num
                count = 1
            elif num == candidate:
                count += 1
            else:
                count -= 1
        
        # Phase 2: Verify the candidate
        count = sum(1 for num in arr if num == candidate)
        
        if count > len(arr) // 2:
            return candidate
        else:
            return -1
            