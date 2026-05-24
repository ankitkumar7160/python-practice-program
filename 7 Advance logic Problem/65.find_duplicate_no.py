# Duplicate Number in Array
n = int(input("Enter the length of array: "))
array = []

for i in range(n):
    i = int(input(f"Enter Value {i+1}: "))
    array.append(i)
print(f"Array: {array}")

if len(array) == 0:
    print("Array is Empty")

else:
    duplicate = []
    for x in range(len(array)):
        for j in range(x+1, len(array)):
            if array[x] == array[j]:
                duplicate.append(array[x])

print(f"Duplicate Number in array: {duplicate}")