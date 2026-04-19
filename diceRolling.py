#Dice rolling game project
''' Output: 
- Question with y/n to roll the dice, anything else is invalid.
- everytime the user puts 'y' the game keeps going, however, if they insert 'n' then it stops
- at each roll of the dice, it sorts two numbers: (x,y)
'''
import random 
a = 0 
while a==0: #the while is useful so the program runs over and over again until the user doesn't want to play anymore. 
    answer = str(input('Roll the dice? (y/n): '))
    if answer.lower() == 'n': 
        print('Thanks for playing!')
        break #as previously said, the game will keep running until the player types 'n'
    elif answer.lower() == 'y':
        dice = [1, 3, 5] #two lists to avoid the same number falling twice
        dice2 = [2, 4, 6]
        firstNumber = random.choice(dice) 
        secondNumber = random.choice(dice2)
        print(f'({firstNumber}, {secondNumber})')
    else: 
        print('invalid input, please try again.')
