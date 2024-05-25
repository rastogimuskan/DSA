#{ 
 # Driver Code Starts
#Initial Template for Python 3


# Python3 implementation of the approach 


# } Driver Code Ends
#User function Template for python3

class Solution:
    
    #Function to return the maximum water that can be stored.
    def maxWater(self, arr, n): 
        
        left = 0
        right = n - 1
        maxw = -1
        while(left < right):
            if arr[left] >= arr[right]:
                area = arr[right] *((right - left) -1)
                right -= 1
            else:
                area = arr[left]*((right - left) -1)
                left += 1
            if area > maxw:
                maxw= area
        return maxw
            
        # mxw = -1
        # wh = 0
        # for i in range(n):
        #     for j in range(i+1, n):
        #         if (j - i) - 1 > 0:
        #             if arr[j] <= arr[i]:
        #                 wh = arr[j]*((j - i) - 1)
        #                 if wh > mxw:((j - i) - 1)
        #                     mxw = wh
        #             else:
        #                 wh = arr[i]*((j - i) - 1)
        #                 if wh > mxw:
        #                     mxw = wh
                        
        # if mxw == -1:
        #     return 0
        # return mxw
                        
                
        #Your code here
     

#{ 
 # Driver Code Starts.


def main():
    t=int(input())
    while(t>0):
        n=int(input())
        height=[int(x) for x in input().strip().split()]
        ob=Solution()
        print (ob.maxWater(height, n));
        t-=1

if __name__ == "__main__":
    main()
# } Driver Code Ends

# https://www.google.com/search?q=Maximum+Water+Between+Two+Buildings&rlz=1C1GCCO_enIN1108IN1108&oq=Maximum+Water+Between+Two+Buildings&gs_lcrp=EgZjaHJvbWUyBggAEEUYOTIGCAEQRRg80gEHMjMwajBqN6gCALACAA&sourceid=chrome&ie=UTF-8#fpstate=ive&vld=cid:a7db7124,vid:w7ftYsZtIbs,st:0


# N = 6
# height[] = {2,1,3,4,6,5}
# Output: 8
# Explanation: The heights are 2 1 3 4 6 5.
# So we choose the following buildings
# 2,5  and remove others. Now gap between 
# two buildings is equal to 4, and the
# height of smaller one is 2. So answer is
# 2 * gap = 2*4 = 8. There is
# no answer greater than this.

#   |
#8  |
#7  |
#6  |
#5  |
#4  |
#3  |        |
#2  |  |     |
#1  |  |     |
#0  |__|__|__|_________________________________________
#   0  1  2  3  4  5 6  7  8  9
