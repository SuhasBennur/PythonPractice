def ternary_search(arr, target, left, right):
    if right >= left:
        mid1 = left + (right-left)//3
        mid2 = right - (right-left)//3

        if arr[mid1] == target:
            return mid1
        if arr[mid2] == target:
            return mid2

        if target < arr[mid1]:
            return ternary_search(arr, target, left, mid1-1)
        elif target > arr[mid2]:
            return ternary_search(arr, target, mid2+1, right)
        else:
            return ternary_search(arr, target, mid1+1, mid2-1)
    return -1

print(ternary_search([1, 2, 3, 4, 5, 6, 7], 5, 0, 6))  # Output: 4

#  Works on sorted arrays.
#  Divides array into three parts instead of two.
