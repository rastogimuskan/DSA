# Starting at the beginning of the list, compare the first two elements.
# If the first element is greater than the second, swap them.
# Move to the next pair of elements and repeat the comparison and swap if necessary.
# Continue this process until the end of the list is reached. This completes one pass.
# Repeat the entire process for the remaining list (ignoring the last element of the previous pass, as it is already sorted).
# Continue until no swaps are needed in a pass, indicating that the list is sorted.

def bubblSort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(n-1):
            if arr[j] > arr[j+1]:
                temp  = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
    print(arr)
    


arr = [5,3,1,6,7]
arr = [1,2,3,4,5]
print(bubblSort(arr))