from random import randint

userName = str(input("Hello! What is your name? "))

print("Well, {}, I am thinking of a number between 1 and 20.".format(userName))
print("You have 5 guesses.")

randNum = randint(1, 20)
guessCount = 1

for i in range(5):
    userGuess = int(input("Take a guess: "))

    if userGuess == randNum:
        print("Good job, {}! You guessed my number in {} guesses!".format(userName, guessCount))
        exit()
    elif userGuess > randNum:
        print("Your guess is too high.")
        guessCount += 1
    else:
        print("Your guess is too low.")
        guessCount += 1

print("Nope. The number I was thinking of was {}.".format(randNum))