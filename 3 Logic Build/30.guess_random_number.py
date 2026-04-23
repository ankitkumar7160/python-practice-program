import random

# Computer ek random number generate karega 1 se 100 ke beech
computer = random.randint(1, 100)

# User ke attempts count karne ke liye variable
attempts = 1

print("Random Number Guessing Game")

# Infinite loop jab tak user sahi guess na kare
while True:
    
    user = int(input(f"Guess the number between 1 and 100 attempts {attempts}: "))
    
    # Har guess ke baad attempt increase hoga
    attempts += 1
    
    if user < computer:
        print("Too Low! Try again")

    elif user > computer:
        print("Too High! Try again")
    
    elif user == computer:
        print("Congratulation: You Win🎉")
        break
    
    else:
        print("You Loss!🥺")

# Total attempts dekhne ke liye niche wali line use kar sakte ho
print(f"Your number of attempts {attempts}")