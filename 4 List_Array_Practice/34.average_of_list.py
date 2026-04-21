n = int(input("Enter the Length of array: "))
array = []

for i in range(n):
    i = int(input("Enter Value: "))
    array.append(i)
print("Array:  ", array)

total = 0

if len(array) == 0:
    print("The Array is Empty")
else:
    for x in array:
        total += x
    
avg = total/n
print(f"The Average of this array {avg}")