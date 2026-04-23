num = int(input("Enter the number: "))

# Count number of digits
order = len(str(num))

temp_num = num
total = 0

# Calculate sum of digits raised to power of order
while temp_num > 0:
    digit = temp_num % 10
    total += digit ** order
    temp_num //= 10

# Check Armstrong condition
if num == total:
    print(f"{num} is armstrong number.")
else:
    print(f"{num} is not armstrong number.")