n = int(input("Enter the Length of array: "))
array = []

for i in range(n):
    i = int(input("Enter Value: "))
    array.append(i)

print(f"Array: {array}")

if len(array) == 0:
    print("Array is Empty")   
else:
    lowest = array[0]
    
    for x in array:
        if x < lowest:
            lowest = x

print(f"The Lowest number in this array {lowest}")