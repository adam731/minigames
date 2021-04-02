import random

def display_menu():
    print('''Mini Game Selector\n
    1. Rock, Paper and scissors
    2. Heads or tails
    3. Exit enter nothing to exit''')


def rock_paper_scissors():
    print('Welcome to rock paper scissors')
    name_one = input('First player enter your name: ')
    player_one = input('Enter your move: ').lower()
    name_two = input('Second player enter your name: ')
    player_two = input('Enter your move: ').lower()
    if player_one == player_two:
        print(f"Both players selected {name_one}. It's a tie!")
        exit()
    elif player_one == "rock":
        if player_two == "scissors":
            print(f"Rock smashes scissors! {name_one} win!")
            exit()
        else:
            print(f"Paper covers rock! {name_two} wins.")
            exit()
    elif player_one == "paper":
        if player_two == "rock":
            print(f"Paper covers rock! {name_one} wins.")
            exit()
        else:
            print(f"Scissors cuts paper! {name_two} wins.")
            exit()
    elif player_one == "scissors":
        if player_two == "paper":
            print(f"Scissors cuts paper! {name_one} wins")
            exit()
        else:
            print(f"Rock smashes scissors! {name_two} wins.")
            exit()

    print('')
    print('I think you may have entered a name wrong? try running the program again')
    print('')



def coin_flip():
    user_input = input('Type start to flip a coin: ').lower()
    if user_input == 'start':
        n = random.random()
        if n > 0.50:
            print('')
            print('Heads')
            print('')
        if n < 0.50:
            print('')
            print('Tails')
            print('')

def main():
    while True:
        display_menu()
        print('')
        picking_number = input('Enter a number for a minigame: ')
        if picking_number == '1':
            rock_paper_scissors()
        if picking_number == '2':
            coin_flip()
        if picking_number == '3':
            exit()


if __name__ == '__main__':
    main()
