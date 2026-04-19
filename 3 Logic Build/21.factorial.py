num = int(input("Enter the number: "))

fact = 1

print("Calculate the Factorial.")

for i in range(1, num + 1):
    if num == 0 or num == 1:
        print("Factorial of 0 and 1 is 1.")
    else:
        fact = fact * i
        print(f"{i}! = {fact}")

print(f"Factorial of {num} is {fact}.")