def findStudent(low, arr):
    # print(low)
    s = 1
    pages = 0
    for i in range(len(arr)):
        if pages + arr[i] <= low:
            pages += arr[i]
        else:
            s = s + 1
            pages = arr[i]
    return s

def allocate_minimum_pages_binarySearch():
    arr = [12,34,67,90]
    k = 2
    start = max(arr)
    end = sum(arr)
    while(start <= end):
        mid = (start+end)//2
        # print(mid)
        students = findStudent(mid, arr)
        # print(students)
        if students == k:
            return mid
        if students < k:
            end = mid - 1
        else:
            start = mid + 1
# print(findPages( 2))

def allocate_minimum_pages():
    arr = [25,46,28,49,24]
    k = 4
    low = max(arr)
    high = sum(arr)
    # print(low, high)
    while(low <= high):
        # print(low, high)
        numberStudent = findStudent(low, arr)
        # print(numberStudent)
        if numberStudent == k:
            return low
        low = low + 1

print(allocate_minimum_pages_binarySearch())

# O(low-high)*O(n)

# https://www.youtube.com/watch?v=Z0hwjftStI4