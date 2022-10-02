n = 17
guess = 1
print('You have total 9 guesses available')
while(guess<=9):
    user = int(input("Enter a guess: "))
    if user == n:
        print("Congratulations you have guessed the correct number!")
        break

    elif user > n:
        print('Please guess a little lower')

    else:
        print('Please guess a little higher')
    print(9-guess, 'no. of guesses left')
    guess = guess + 1

    if guess > 9:
        print("You lose")