import random

# Generate a random number between 1 and 100
number = random.randint(1, 100)

# Set the initial number of guesses to 0
guesses = 0

# Loop until the user guesses the correct number
while True:
    # Get the user's guess
    guess = int(input('Guess a number between 1 and 100: '))

    # Increment the number of guesses
    guesses += 1

    # Check if the guess is correct
    if guess == number:
        print(f'Congratulations, you guessed the number in {guesses} guesses!')
        break

    # Provide a hint if the guess is too low or too high
    if guess < number:
        print('Your guess is too low, try again.')
    else:
        print('Your guess is too high, try again.')