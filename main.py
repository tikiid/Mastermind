# --- Mastermind --- #

import random
import os

# --- Varaibles --- # 

list_of_colors = ['R', 'B', 'O', 'G', 'Y', 'P']

# --- Functions --- #

def create_secret_combination():
    secret_list = [random.choice(list_of_colors) for _ in range(4)]
    return ''.join(secret_list)


def enter_combination():
    while True: 
        guess_combination = str(input('enter a combination (exemple: RYBG): ')).upper()

        if(check_guess_combination(guess_combination)):
            break
    
    return guess_combination


def check_guess_combination(guess_combination):    
    if len(guess_combination) < 4:
        print("too short")
        return False
    elif len(guess_combination) > 4:
        print("too long")
        return False
    
    for element in guess_combination:
        if element not in list_of_colors:
            print("wrong caractere")
            return False

    return True


def check_right_place(caractere, index, secret_combination):
    if caractere == secret_combination[index]:
        return True

    return False


def check_existing_color(guess, secret_combination):
    exist_list = []
    for index, caractere in enumerate(guess) :
        if caractere in secret_combination:
            if check_right_place(caractere, index, secret_combination): 
                exist_list.append('!')
            else:
                exist_list.append('?')

        else: 
            exist_list.append('-')

    join_exist_list = ''.join(exist_list) 
    return join_exist_list


def display_board(list_of_attemps):
    print('Mastermind')
    print('___________')
    for elements in list_of_attemps:
        print('|', end='')
        if not elements:  
                for i in range (0,2):
                    print('____|', end='')
        else :
            for element in elements:
                    print(f'{element}|', end='')
        print()


def restart_game():
    for i in range (0, 3):
        restart = input('Do you want to paly again ? (Y/N) : ').strip().lower() 
        if restart == 'y':
            return True
        elif restart == 'n':
            return False
        else:
            print("Wrong input (Y for yes or N for no)")
    print('Too many try')


# --- Display the rules --- #

def start_messages():
    print('Start a game')
    print()
    print('Find the secret combination : R (red), B (blue), O (orange), G (green), Y (yellow), P (purple)')
    print('Hints : - (not in the secret combination), ? (wrong place), ! (right place)')
    print()
    start_the_game = input("Press enter to start the game ")
    os.system('cls')

restart = False

# --- The game --- #

while True:

    # --- Clear console --- # 

    os.system('cls')

    # --- Variables reset --- #
    
    attempts = 1
    secret_combination = ''
    guess = ''
    all_attemps_list = [[], [], [], [], [], [], [], [], [], []]


    # --- Create the secret combination --- #

    secret_combination = create_secret_combination()
    
    if not restart:
        start_messages()
    
    # --- Current game --- #

    while attempts < 11:
        
        if restart:
            print('Start a new game')
            print()
            restart = False

        display_board(all_attemps_list)

        # --- Check if the player won --- #

        if guess == secret_combination:
            print('you win')
            break
        
        # --- Display information and the input to the player --- #

        print(f'attempts left : {11 - attempts}')
        guess = enter_combination()
        exist = check_existing_color(guess, secret_combination)
        all_attemps_list[10-attempts] = [guess, exist]
        
        os.system('cls')
        
        attempts += 1
    
    os.system('cls')
    display_board(all_attemps_list)

    if attempts > 10:
        print('you loose')
    
    print(f'The secret code was : {secret_combination}')

    # --- Restart a game --- #

    restart = restart_game()
    if not restart:
        break
