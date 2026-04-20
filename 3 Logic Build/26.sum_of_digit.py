num = int(input("Enter the Number: "))

total = 0
count = 0

if num == 0:
    count = 1
    total = 0
else:
    temp_num = abs(num)
    while temp_num > 0:
        digit = temp_num % 10
        total += digit
        
        temp_num //= 10
        count += 1
print(f"The sum of the digits in {num} is: {total}")