num = int(input("Enter the Number: "))

sum = 0

for i in range(1, num + 1):
    print(i, end=" ")
    sum += i
    
print(f"\nSum of 1 to {num} is: {sum}")