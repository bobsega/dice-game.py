import random

while True:
    choice = input('Roll the dice? (y/n): ').lower()
    if choice == 'y':
        dice_roll1 = random.randint(1, 6)
        dice_roll2 = random.randint(1, 6)
        print(f'You rolled a {dice_roll1} and a {dice_roll2}')
    elif choice == 'n':
        print('Thanks for playing!')
        break   
    else:
        print('Invalid input. Please enter "y" or "n".')