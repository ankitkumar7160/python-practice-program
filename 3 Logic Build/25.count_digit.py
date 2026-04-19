num = int(input("Enter the Number: "))

count = 0

if num == 0:
    count = 1
else:
    temp_num = abs(num)
    while temp_num > 0:
        temp_num //= 10
        count += 1
        
print(f"The number of digits in {num} is: {count}")