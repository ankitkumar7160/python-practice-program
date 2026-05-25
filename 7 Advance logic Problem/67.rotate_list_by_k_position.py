def rotate_list(my_array, k):
    n = len(my_array)
    
    if n == 0:
        return my_array
    
    k = k % n

    if k == 0:
        return my_array
    
    else:
        part1 = my_array[n-k:]
        
        part2 = my_array[:n-k]
        
        rotated_result = part1 + part2
        return rotated_result

my_input = input("Enter values of array separated by space: ")
k_input = int(input("Enter value of k: "))

new_array = [int(x) for x in my_input.split()]

result = rotate_list(new_array, k_input)

print(f"Rotated List: {result}")