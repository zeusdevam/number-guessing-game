import random
play = str(input('Type NO to quit the game: '))
guess = 1

while (guess <= 9):
    if play.lower() == 'no':
        break
    else:
        pass

        lower_limit = int(input("Enter the lower limit: "))
        upper = int(input('Enter the upper limit: '))
        
        n = random.randint(lower_limit, upper)

        print('You have total 9 guesses available')

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
        
        guess = guess + 1

        if guess > 9:
            print(f"You lose the number was {n}")
