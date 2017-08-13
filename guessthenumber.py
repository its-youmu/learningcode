# library to be able to generate a random number
import random

# setting the initial variable to be used
guessesTaken = 0
inputError = False

print("Hello! What is your name?")
myName = input()

# generate a random number between 1 and 100
number = random.randint(1, 100)
print("Well, " + myName + ", I am thinking of a number between 1 and 100.")


# in the while loop, have a total number of 10 guesses to correctly guess the number
# once 10 is hit, while no longer is true and continues on to the if statements
# below that
while guessesTaken <= 10:

# try will ask for the user to input a number that is an integer
# if that fails, it will raise "ValueError" and ask for re-input
    try:
        guess = 0
        guess = int(input("Take a guess:"))
        if guess > 100 or guess < 1:
            raise ValueError
    except ValueError:
        print("Please enter in a valid option.")
        # input error set to true to ignore the next if statement (not valid
        # input otherwise)
        inputError = True

    # increment the number of guesses every time it is incorrect and it was a
    # valid number input
    if inputError == False:
        guessesTaken += 1

        if guess < number:
            print('Your guess is too low.')

        if guess > number:
            print('Your guess is too high.')

        if guess == number:
            break

    # This sets the inputError value back to false before going through the
    # while loop again so the user isn't perpetually stuck
    inputError = False

# correctly guessing the number in the while fxn will break the while loop and
# cause this to be true
if guess == number:
    print("Good job, " + myName + "! You guessed the number in " + str(guessesTaken) + " guesses!")

#failure to guess in under 10 turns will yield this result
if guess != number:
    print("Nope, the number I was thinking of was " + str(number))
