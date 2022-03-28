import random

print("Welcome to the number guessing game!")
print("Guess a number between 1 and 9: ")

number = random.randint(1, 9)
guess = int(input("Guess a number: "))

for i in range(5):
    if guess == number:
        print("You guessed the number!")
        break
    elif guess > number:
        print("Your guess is too high!")
    else:
        print("Your guess is too low!")
    guess = int(input("Guess again: "))

if guess != number:
    print("You lose! The number was", number)


