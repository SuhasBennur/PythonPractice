def interpolation_search(arr, target):
    low, high = 0, len(arr)-1

    while low <= high and target >= arr[low] and target <= arr[high]:
        pos = low + ((target - arr[low]) * (high - low) //
                     (arr[high] - arr[low]))

        if arr[pos] == target:
            return pos
        if arr[pos] < target:
            low = pos + 1
        else:
            high = pos - 1
    return -1

print(interpolation_search([10, 20, 30, 40, 50], 40))  # Output: 3

# Works on uniformly distributed sorted arrays.
# Estimates position using interpolation formula.
