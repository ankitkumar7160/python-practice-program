n = int(input("Enter the Length of array: "))
array = []

for i in range(n):
    i = int(input("Enter Value: "))
    array.append(i)
    
print(f"Array: {array}")

if len(array) == 0:
    print("The array is Empty")
else:
    odd = []
    for x in array:
        if x % 2 != 0:
            odd.append(x)
print(f"Odd Number: {odd}")