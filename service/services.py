import random

def get_random_answer() -> str:
    return random.choice(['Rock', 'Scissors', 'Paper'])

def get_winner(user_choice: str, bot_choice: str) -> str:
    rules = {'Rock' : 'Scissors',
             'Scissors' :'Paper',
             'Paper' : 'Rock'}
    if user_choice == bot_choice:
        return 'Draw!'
    elif rules[user_choice] == bot_choice:
        return 'You won!'
    return 'Bot won!'