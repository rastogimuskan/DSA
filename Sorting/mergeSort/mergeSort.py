def mergeSortedArray(arr1, arr2):
    temp = []
    m = len(arr1)-1
    n = len(arr2)-1
    i, j  = 0, 0
    while(i <= j and j <= m):
        if arr1[i] <= arr2[j]:
            temp.append(arr1[i])
            i = i + 1
        else:
            temp.append(arr2[j])
            j = j + 1
            
    print(temp)


arr1 = [10,15,20]
arr2 = [5,6,6]
print(mergeSortedArray(arr1, arr2))




# def checkCookiesPossible(cookies, arr1, arr2, k, n):
#     i = 0
#     while (i <=n ):
#         if arr1[i]*mid <= arr2[b] or 
    

# def returnCookies(arr1, arr2, k, n):
#     start = 0
#     end = 2000
#     while(start <= end):
#         mid = (start + end) //2
#         if checkCookiesPossible(mid, arr1, arr2, k, n):
#             ans = mid
#             start = mid + 1
#         else:
#             end = mid -1
#     return ans