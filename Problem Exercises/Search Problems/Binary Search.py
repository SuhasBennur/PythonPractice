def binary_search(arr, target):
    low, high = 0, len(arr)-1
    while low <= high:
        mid = (low+high)//2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid+1
        else:
            high = mid-1
    return -1

print(binary_search([1,2,3,4,5,6,7], 5))

# Works only on sorted arrays.
# Divides the search space in half each time.
# Time Complexity:
# Best case: O(1) (target is the middle element).
# Worst case: O(\log n).
