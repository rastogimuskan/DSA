
class Solution:
    def subArraySum(self,arr, n, s):
        start = 0
        arsum = 0
        for i in range(n):
            arsum += arr[i]
            while arsum > s and start < i:
                arsum -= arr[start]
                start += 1
            
            if arsum == s:
                return [start + 1, i + 1]  # Return 1-based index
        return [-1] 

# sliding window algorithm