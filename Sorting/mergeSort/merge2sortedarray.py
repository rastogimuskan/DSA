def mergeSortedArray(arr1, arr2):
    temp = []
    m = len(arr1)-1
    n = len(arr2)-1
    i, j  = 0, 0
    while(i <= m and j <= n):
        if arr1[i] <= arr2[j]:
            temp.append(arr1[i])
            i = i + 1
        else:
            temp.append(arr2[j])
            j = j + 1
            
    while(i <=m):
        temp.append(arr1[i])
        i = i +1
    while(j<=m ):
        temp.append(arr2[j])
    return temp  
  


arr1 = [1,15,15,20]
arr2 = [5,6,6,7]
print(mergeSortedArray(arr1, arr2))