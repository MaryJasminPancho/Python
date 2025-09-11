import random

print("Welcome to the Guessing Game!")
print("You have 5 chances to guess the correct number. Let's begin!")

try:
    lowerBound = int(input("Enter the lower bound of the range: "))
    upperBound = int(input("Enter the upper bound of the range: "))

    numberToGuess = random.randint(lowerBound, upperBound)
    chances = 5
    attempts = 0

    while attempts < chances:
        attempts += 1
        guess = int (input(f"Attempt {attempts}: Enter your guess between {lowerBound} and {upperBound}: "))
        if guess < lowerBound or guess > upperBound:
            print(f"Please guess a number within the range {lowerBound} to {upperBound}.")
            attempts -= 1
        elif guess < numberToGuess:
            print("Too low!")
        elif guess > numberToGuess:
            print("Too high!")
        elif guess == numberToGuess:
            print(f"Congratulations! You've guessed the correct number in {attempts} attempts.")
            break
        else:
            print(f"Sorry you've used all your chances. The correct number was {numberToGuess}.")
            break

except:
    print("Invalid input.")

