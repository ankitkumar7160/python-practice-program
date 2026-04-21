n = int(input("Enter the Length of array: "))
array = []

for i in range(n):
    i = int(input("Enter Value: "))
    array.append(i)
print("Array: ", array)

total = 0

if len(array) == 0:
    print("The array is empty.")
else:
    for x in array:
        total = total + x
print(f"The Total sum of this array: {total}")