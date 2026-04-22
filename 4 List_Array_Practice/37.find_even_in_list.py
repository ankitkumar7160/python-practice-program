n = int(input("Enter the Length of array: "))
array = []

for i in range(n):
    i = int(input("Enter value: "))
    array.append(i)

print(f"Array: {array}")

if len(array) == 0:
    print("The array is empty")
else:
    even = []
    for x in array:
        if x % 2 == 0:
            even.append(x)
print(f"Even Number: {even}")