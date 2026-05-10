def find_largest_number(numbers):

    if len(numbers) == 0:
        return "Empty List"

    largest = numbers[0]

    for num in numbers:
        if num > largest:
            largest = num

    return largest


lists = input("Enter the list (space separated): ")

n_list = [int(x) for x in lists.split()]

result = find_largest_number(n_list)

print(f"Largest number: {result}")