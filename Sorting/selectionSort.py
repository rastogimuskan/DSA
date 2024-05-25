# it does less memory writes comparing to other sorting algo
# in place sorting algo doesnot required extra space

# will find the minimum element and will put it at first location 

# Start with the entire list as the unsorted part.
# Find the smallest element in the unsorted part.
# Swap this smallest element with the first element of the unsorted part.
# Now, the first element is sorted, and the rest of the list is unsorted.
# Move the boundary one element to the right and repeat the process for the remaining unsorted part of the list.
# Continue until the entire list is sorted.

def selectionSort(arr):
    n = len(arr)
    
    for i in range(n):
        smallelement = arr[i]
        pos = i
        for j in range(i, n):
            if smallelement > arr[j]:
                smallelement = arr[j]
                pos = j
        print(smallelement, pos, arr)
        # if pos != -1:
        temp = arr[i]
        arr[i] = arr[pos]
        arr[pos] = temp
    return arr
            



arr = [1,2,3,4,5]
# arr = [1,4,5,9,8,1]
print(selectionSort(arr))