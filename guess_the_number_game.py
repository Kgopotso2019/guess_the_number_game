"""The player must guess a random number between 1 and 10. The player have 5 chances to guess
the number."""

# Skills used: random module, variables, integers, print function, if else statement and while loop

import random

print("Hi")
player_name = input("What is your name? ")
print(f'Welcome {player_name}, hope you enjoy the Game')
computer_guess = random.randint(1, 10)
number_of_guesses = 0

while number_of_guesses < 5:
    try:
        player_guess = int(input("Guess a number between 1 and 10: "))
        number_of_guesses += 1
        if player_guess < computer_guess:
            print("Your number is too low")
        if player_guess > computer_guess:
            print("Your number is too high")
        if player_guess == computer_guess:
            print(f'Congratulations! {player_name}, you have guessed the correct number')
            break
    except ValueError:
        print("Enter a numeric value")
if computer_guess:
    print(f'You have guessed the number {number_of_guesses} times')
else:
    print(f'Sorry! you could not guess the correct number, which is {computer_guess}')
