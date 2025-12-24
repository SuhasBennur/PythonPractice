def exponential_search(arr, target):
    if arr[0] == target:
        return 0
    i = 1
    while i < len(arr) and arr[i] <= target:
        i *= 2
    return binary_search(arr[:min(i, len(arr))], target)

print(exponential_search([1, 2, 4, 8, 16, 32, 64], 16))  # Output: 4

# Useful for unbounded or infinite lists.
# Finds range using powers of 2, then applies binary search.
