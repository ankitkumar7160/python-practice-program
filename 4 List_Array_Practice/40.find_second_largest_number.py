def find_second_largest(array):
    if len(array) < 2:
        return "This array is less than 2 values."
    
    largest = second_largest = float("-inf")
    
    for i in array:
        if i > largest:
            second_largest = largest
            largest = i
        
        elif i > second_largest and i != largest:
            second_largest = i
    return second_largest

n = int(input("Enter the Length of array: "))
array = []

for i in range(n):
    i = int(input(f"Enter value {i+1}: "))
    array.append(i)

print(f"Your original array {array}")
print(f"Second largest number: {find_second_largest(array)}")