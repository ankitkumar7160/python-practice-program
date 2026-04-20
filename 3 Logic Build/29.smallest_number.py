num = int(input("Enter the Number: "))

temp = num
smallest_digit = 9

while temp > 0:
    digit = temp % 10
    if digit < smallest_digit:
        smallest_digit =  digit
    temp //= 10

print(f"The Smallest digit in {num} is: {smallest_digit}")