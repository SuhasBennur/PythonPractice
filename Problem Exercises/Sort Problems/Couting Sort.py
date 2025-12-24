def counting_sort(arr):
    max_val = max(arr)
    count = [0] * (max_val + 1)

    # Count occurrences
    for num in arr:
        count[num] += 1

    # Build sorted array
    output = []
    for i in range(len(count)):
        output.extend([i] * count[i])

    return output

print(counting_sort([4, 2, 2, 8, 3, 3, 1]))