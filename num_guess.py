import random
lower_limit = int(input("Enter the lower limit: "))
upper = int(input('Enter the upper limit: '))
guess = 0

while (guess < 9):
    guess = guess + 1

    n = random.randint(lower_limit, upper)

    user = int(input("Enter a guess: "))

    if (user < lower_limit) or (user > upper):
        print("You exceeded the limit!\nGame Over!")
        break

    if user == n:
        print("Congratulations you have guessed the correct number!")
        break

    elif user > n:
        print('Please guess a little lower')

    else:
        print('Please guess a little higher')

    print(9-guess, 'no. of guesses left')

    if guess >= 9:
        print(f"You lose the number was {n}")
