def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    operations = 0  # Count operations
    while left <= right:
        operations += 1  # Increment for comparison and mid calculation
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return mid, operations
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1, operations

def linear_search(arr, target):
    operations = 0  # Count operations
    for index, val in enumerate(arr):
        operations += 1  # Increment for each comparison
        if target == val:
            return index, operations
    return -1, operations

# Example usage
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 14
index, operations = binary_search(arr, target)
print(f"Binary search found the target at index {index} with {operations} operations.")

index, operations = linear_search(arr, target)
print(f"Linear search found the target at index {index} with {operations} operations.")
