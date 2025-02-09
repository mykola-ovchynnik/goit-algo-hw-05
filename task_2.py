def binary_search(arr, target):
    iterations = 0
    upper_bound = None

    for num in arr:
        iterations += 1
        if num >= target:
            upper_bound = num
            break

    return iterations, upper_bound


sorted_array = [0.1, 0.5, 1.2, 3.8, 4.6, 5.9, 7.3]
target_value = 4.0
print(binary_search(sorted_array, target_value))
