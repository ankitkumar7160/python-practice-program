print("Calculate Average of 1 to N")

num = int(input("Enter the Number: "))
sum = 0

for i in range(1, num + 1):
    sum += i

average = sum / num

print(f"Average of num {average}")