# n = int(input("Enter the length of array: "))
# array = []

# for i in range(n):
#     i = int(input("Enter value: "))
#     array.append(i)
    
# if len(array) == 0:
#     print("The array is list")
# else:
#     for i in range(len(array)):
#         for j in range(0, len(array)-1 - i):
#             if array[j] > array[j+1]:
#                 array[j], array[j+1] = array[j +1], array[j]
                
# print(f"Sorted Array: {array}")

# Function for Bubble Sort
def bubble_sort(array):
    n = len(array)
    for i in range(n):
        for j in range(0, n-i-1):
            if array[j] > array[j+1]:
                temp = array[j]
                array[j] = array[j+1]
                array[j+1] = temp
    return array

# Function for Selection Sort
def selection_sort(array):
    n = len(array)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if array[j] < min_index:
                min_index = j
        array[i], array[min_index] = array[min_index], array[i]
    return array

# Main Program
n = int(input("Enter the Length of array: "))
original_array =[]

for x in range(n):
    original_array.append(int(input(f"Values {x+1}: ")))
    
print(f"Original array {original_array} ")
print("1. Bubble sort")
print("2. Selection Sort")

choice = int(input("Choose the algorithms. {1/2}: "))

temp_array = original_array.copy()
if choice == 1:
    result = bubble_sort(temp_array)
    print(f"Sorted array using bubble sort algorithm: {result}")
elif choice == 2:
    result = selection_sort(temp_array)
    print(f"Sorted array using Selection sort algorithm: {result}")
else:
    print("Invalit choice.")