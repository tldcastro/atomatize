import random
secretNumber = random.randint(1, 20)
print("I am thinking of a number between 1 and 20")

for guessesTaken in range(1, 7):  # Aqui é definido a quantd de tentativas (6)
    print("Take a Guess.")
    guess = int(input())

    if guess < secretNumber:
        print("Your guess is too low.")

    elif guess > secretNumber:
        print("Your guess is too high.")

    else:
        break
if guess == secretNumber:
    print("Good job! You guessed my number in " +
          str(guessesTaken) + " guesses!")
else:
    print("Nope. The number i was thinking of was " + str(secretNumber))
