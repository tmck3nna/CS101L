print('Welcome to the Flarsheim Guesser!')
t = 1

while t == 1:
    print('\nPlease think of a number between 1-100.')
    rem_three = int(input('\nWhat is the value when your number is divided by 3?'))
    while rem_three < 0 or rem_three >= 3:
        if rem_three < 0:
            print('Your number must be greater than 0')
        elif rem_three >= 3:
            print('Your number must be less than 3')
        rem_three = int(input('\nWhat is the value when your number is divided by 3?'))
    rem_five = int(input('What is the value when your number is divided by 5?'))
    while rem_five < 0 or rem_five >= 5:
        if rem_five < 0:
            print('Your number must be greater than 0')
        elif rem_three >= 5:
            print('Your number must be less than 5')
        rem_five = int(input('\nWhat is the value when your number is divided by 5?'))
    rem_seven = int(input('What is the value when your number is divided by 7?'))
    while rem_seven < 0 or rem_seven >= 7:
        if rem_seven < 0:
            print('Your number must be greater than 0')
        elif rem_seven >= 7:
            print('Your number must be less than 7')
        rem_seven = int(input('\nWhat is the value when your number is divided by 7?'))
    for i in range(1, 101):
        num3 = i % 3
        num5 = i % 5
        num7 = i % 7
        if (num3 == rem_three) and (num5 == rem_five) and (num7 == rem_seven):
                print('Your number was', i)
    print('How amazing was that?')

    while True:
        repeat = input('Do you want to play again? Y for yes or N for no')
        if repeat == 'Y' or repeat == 'y':
            break
        elif repeat == 'N' or repeat == 'n':
            t = 0
            break
    

                
