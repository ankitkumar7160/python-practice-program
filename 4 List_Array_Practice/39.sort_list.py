n = int(input("Enter the length of array: "))
array = []

for i in range(n):
    i = int(input("Enter value: "))
    array.append(i)
    
if len(array) == 0:
    print("The array is list")
else:
    for i in range(len(array)):
        for j in range(0, len(array)-1 - i):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j +1], array[j]
                
print(f"Sorted Array: {array}")