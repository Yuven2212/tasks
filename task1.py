def running_sum(arr):
    result = [] 
    current_sum = 0 

    for num in arr:
        current_sum += num 
        result.append(current_sum)

    return result


arr = [1, 2, 3, 4, 5]
output = running_sum(arr)
print(output) 
