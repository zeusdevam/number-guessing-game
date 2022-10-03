import random
lower_limit = int(input("\n\nEnter the lower limit: "))
upper = int(input('Enter the upper limit: '))
guess = 10
n = random.randint(lower_limit, upper)

while (guess > 0):
    guess -= 1

    user = int(input("\nEnter a guess: "))

    if (user < lower_limit) or (user > upper):
        print("You exceeded the limit!\nGame Over!")
        break

    elif user == n:
        print(
            f"Congratulations you have guessed the correct number in {guess} tries!")
        break

    elif user > n:
        print('Please guess a little lower\n')

    elif user < n:
        print('Please guess a little higher\n')

    print(guess, 'no. of guesses left')

    if guess == 0:
        print("You Lose! Better Luck nexr time\n")
        break
