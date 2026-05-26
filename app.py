import random

emojis = { 'r' : '🪨', 'p' : '📄', 's' : '✂️' }
choices = ( 'r', 'p', 's' )

while True:
    user_choice = input( 'Enter your choice (r, p, s): ' )
    if user_choice not in choices:
        print( 'Invalid choice. Please try again.' )
        continue

    computer_choice = random.choice( choices )

    print( f'You chose: {emojis[user_choice]} | Computer chose: {emojis[computer_choice]}' )

    if user_choice == computer_choice:
        print( 'It\'s a tie!' )
    elif (user_choice == 'r' and computer_choice == 's') or (user_choice == 'p' and computer_choice == 'r') or (user_choice == 's' and computer_choice == 'p'):
        print( 'You win!' )
    else:
        print( 'Computer wins!' )
    play_again = input( 'Do you want to play again? (y/n): ' )
    if play_again.lower() != 'y':
        print( 'Thanks for playing!' )
        break
    