number = 7
attempts = 0

while attempts < 3:
    guess = int(input("Guess a number between 1 and 20: "))
    attempts = attempts + 1

    if guess == number:
        print(attempts)
        break

if guess != number:
    print("The game is locked. Try again later!")