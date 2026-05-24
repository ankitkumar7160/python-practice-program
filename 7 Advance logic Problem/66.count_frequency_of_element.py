n = int(input("Enter the length of array: "))

array = []

# Input array elements
for i in range(n):
    value = int(input(f"Enter Value {i+1}: "))
    array.append(value)

print(f"\nArray: {array}")

frequency = {}

# Count frequency
for element in array:

    if element in frequency:
        frequency[element] += 1

    else:
        frequency[element] = 1

# Print frequency
print("\nElement : Frequency")

for key, value in frequency.items():
    print(f"{key} : {value}")