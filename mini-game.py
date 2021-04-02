from sys import exit

# Def main is code that's planned for the future to be added.
def main():
    print('Mini Game Selector')
    print('1. Rock, Paper and scissors')
    print('2. Heads or tails')
    print('3. Exit enter nothing to exit')

def my_function():
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

    print('I think you may have entered a name wrong? try running the program again')

my_function()