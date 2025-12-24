def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

print(linear_search([10, 20, 30, 40], 30))  # Output: 2

# Works on unsorted arrays.
# Checks each element one by one.
# Time Complexity:
# Best case: O(1) (target is the first element).
# Worst case: O(n) (target is last or not present).
