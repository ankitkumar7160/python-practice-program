import random

computer = random.randint(1, 100)
attempts = 1

print("Random Number Guessing Game")

while True:
    user = int(input(f"Guess the number between 1 and 100 attempts {attempts}: "))
    attempts += 1
    
    if user < computer:
        print(f"Too Low! Try again")
        
    elif user > computer:
        print(f"Too High! Try again")
    
    elif user == computer:
        print(f"Congratulation: You Win🎉")
        break
    else:
        print(f"You Loss!🥺")
        
    # print(f"Your number of attempts {attempts}")