#Dice rolling game project
''' Output: 
- Question with y/n to roll the dice, anything else is invalid.
- everytime the user puts 'y' the game keeps going, however, if they insert 'n' then it stops
- at each roll of the dice, it sorts two numbers: (x,y)
'''
import random
a = 0
while a==0: 
    answer = str(input('Roll the dice? (y/n): '))
    if answer.lower() == 'n':
        print('Thanks for playing!')
        break
    elif answer.lower() == 'y':
        dice = [1, 2, 3, 4, 5, 6]
        firstNumber = random.choice(dice)
        secondNumber = random.choice(dice)
        print(f'something, ({firstNumber}, {secondNumber})')
    else: 
        print('invalid input, please try again.')
    
