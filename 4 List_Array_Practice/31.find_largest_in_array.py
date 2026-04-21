n = int(input("Enter length of array: "))
array = []

for i in range(n):
    i = int(input("Enter value: "))
    array.append(i)

print("Array: ", array)

if len(array) == 0:
    print("Array is Empty")
else:
    largest = array[0]
    
    for x in array:
        if x > largest:
            largest = x

print(f"The Largest number in this array {largest}")