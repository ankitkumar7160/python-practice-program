n = int(input("Enter the length of array: "))
array = []

for i in range(n):
    i = int(input("Enter value: "))
    array.append(i)
    
print("Array: ", array)

if len(array) == 0:
    print("The array is empty")
else:
    reversed_array = []
    for x in array[::-1]:
        reversed_array.append(x)
print(f"This is the Reversed array {reversed_array}")