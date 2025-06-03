
import random
import ipywidgets as widgets
from IPython.display import display, clear_output


game_score = {'user': 0, 'computer': 0, 'ties': 0, 'rounds': 0}


user_choice_widget = widgets.Dropdown(
    options=['rock', 'paper', 'scissors'],
    value='rock',
    description='Your move:',
    disabled=False,
)


play_button = widgets.Button(
    description='Play!',
    button_style='success',
    tooltip='Play your move'
)


output = widgets.Output()

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return 'tie'
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return 'user'
    else:
        return 'computer'

def on_play_button_clicked(b):
    user_choice = user_choice_widget.value
    computer_choice = get_computer_choice()
    winner = determine_winner(user_choice, computer_choice)
    game_score['rounds'] += 1
    if winner == 'user':
        game_score['user'] += 1
    elif winner == 'computer':
        game_score['computer'] += 1
    else:
        game_score['ties'] += 1
    with output:
        clear_output(wait=True)
        print('Round', game_score['rounds'])
        print('You chose:', user_choice.capitalize())
        print('Computer chose:', computer_choice.capitalize())
        if winner == 'tie':
            print("It's a tie!")
        elif winner == 'user':
            print('You win!')
        else:
            print('Computer wins!')
        print('-' * 40)
        print('Score - You:', game_score['user'], '| Computer:', game_score['computer'], '| Ties:', game_score['ties'])

play_button.on_click(on_play_button_clicked)

display(user_choice_widget, play_button, output)
print('Select your move and click Play! The score will update after each round.')
