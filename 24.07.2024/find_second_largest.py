def find_second_largest(arr):
    first, second = float('-inf'), float('-inf')
    for num in arr:
        if num > first:
            second = first
            first = num
        elif first > num > second:
            second = num
    return second

arr = [12, 35, 1, 10, 34, 1]
result = find_second_largest(arr)
print("Second largest element is", result if result != float('-inf') else "None")
