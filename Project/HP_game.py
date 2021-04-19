import random
import csv
import colorama
from colorama import Fore
colorama.init(autoreset=True)
# If not downloaded, install ' pip install colorama ' in terminal

player_score = 0
computer_score = 0


print('Welcome to the Wizarding World of Hogwarts! ')
print('Let the Duel commence! ')
print('https://www.youtube.com/watch?v=Htaj3o3JD8I&ab_channel=Yume')
player_name = input('Enter your name: ')
round = int(input('How many rounds would you like to play? '))


player_house = input('Choose a house: Gryffindor (G), Hufflepuff (H), Ravenclaw (R), Slytherin (S) ')
if player_house == 'G' or player_house == 'g':
    player_colour = Fore.RED
    player_house = 'Gryffindor'
elif player_house == 'H' or player_house == 'h':
    player_colour = Fore.YELLOW
    player_house = "Hufflepuff"
elif player_house == 'R' or player_house == 'r':
    player_colour = Fore.BLUE
    player_house = 'Ravenclaw'
else:
    player_colour = Fore.GREEN
    player_house = 'Slytherin'

print(player_colour + 'You are playing for {}!'.format(player_house))


houses = ['Gryffindor', 'Hufflepuff', 'Ravenclaw', 'Slytherin']
opponent_house = random.choice(houses)

if opponent_house == 'Gryffindor':
    opponent_colour = Fore.RED
elif opponent_house == 'Hufflepuff':
    opponent_colour = Fore.YELLOW
elif opponent_house == 'Ravenclaw':
    opponent_colour = Fore.BLUE
elif opponent_house == 'Slytherin':
    opponent_colour = Fore.GREEN
print(opponent_colour + 'Your opponent is playing for {}.'.format(opponent_house))

def begin_round(player_score, computer_score):
    round_winner = 'None'

    print(player_colour + 'Your character is: ')
    with open('./HP_Stats.csv', 'r') as HP_stats:
        spreadsheet = csv.DictReader(HP_stats)
        chosen_row = random.choice(list(spreadsheet))

    with open('./HP_Stats.csv', 'r') as HP_stats:
        spreadsheet = csv.DictReader(HP_stats)
        opponent_row = random.choice(list(spreadsheet))

    print(player_colour +'Full Name: {}'.format(chosen_row['Full Name']))
    print(player_colour +'Popularity: {}'.format(chosen_row['Popularity']))
    print(player_colour +'Height: {}cm'.format(chosen_row['Height']))
    print(player_colour +'Year of Birth: {}'.format(chosen_row['Year of birth']))
    print(player_colour +'Wand Length: {} in'.format(chosen_row['Wand length']))
    print(player_colour +'Top Trumps Rating: {}'.format(chosen_row['Top Trumps Rating']))

    player_characteristic = input(player_colour + 'Which characteristic would you like to play with? ')
    if player_characteristic == 'Popularity' or player_characteristic == 'popularity':
        opponent_characteristic = int(opponent_row['Popularity'])
        print(player_colour + '{}\'s {} is {}.'.format(chosen_row['Name'], player_characteristic,chosen_row['Popularity']))
        print(opponent_colour + 'Your opponent has {}. Their {} is {}.'.format(opponent_row['Full Name'], player_characteristic,opponent_row['Popularity']))
        player_characteristic = int(chosen_row['Popularity'])
    if player_characteristic == 'Height' or player_characteristic == 'height':
        opponent_characteristic = int(opponent_row['Height'])
        print(player_colour + '{}\'s {} is {}cm.'.format(chosen_row['Name'], player_characteristic,chosen_row['Height']))
        print(opponent_colour + 'Your opponent has {}. Their {} is {}cm.'.format(opponent_row['Full Name'], player_characteristic, opponent_row['Height']))
        player_characteristic = int(chosen_row['Height'])
    if player_characteristic == 'Year of birth' or player_characteristic == 'year of birth':
        opponent_characteristic = int(opponent_row['Year of birth'])
        print(player_colour + '{}\'s {} is {}.'.format(chosen_row['Name'], player_characteristic,chosen_row['Year of birth']))
        print(opponent_colour + 'Your opponent has {}. Their {} is {}.'.format(opponent_row['Full Name'], player_characteristic, opponent_row['Year of birth']))
        player_characteristic = int(chosen_row['Year of birth'])
    if player_characteristic == 'Wand length' or player_characteristic == 'wand length':
        opponent_characteristic = int(opponent_row['Wand length'])
        print(player_colour + '{}\'s {} is {} inches.'.format(chosen_row['Name'], player_characteristic,chosen_row['Wand length']))
        if opponent_characteristic == 0:
            print(opponent_colour + 'Your opponent has {}. {} does not own a wand.'.format(opponent_row['Full Name'],opponent_row['Name']))
        else:
            print(opponent_colour + 'Your opponent has {}. Their {} is {} inches.'.format(opponent_row['Full Name'], player_characteristic, opponent_row['Wand length']))
        player_characteristic = int(chosen_row['Wand length'])
    if player_characteristic == 'Top Trumps Rating' or player_characteristic == 'top trumps rating':
        opponent_characteristic = int(opponent_row['Top Trumps Rating'])
        print(player_colour + '{}\'s {} is {}.'.format(chosen_row['Name'], player_characteristic,chosen_row['Top Trumps Rating']))
        print(opponent_colour +'Your opponent has {}. Their {} is {}.'.format(opponent_row['Full Name'], player_characteristic, opponent_row['Top Trumps Rating']))
        player_characteristic = int(chosen_row['Top Trumps Rating'])
    if player_characteristic > opponent_characteristic:
        print(player_colour + 'Congratulations {}, you won!'.format(player_name))
        round_winner = 'player'
        print(player_colour + "One point to {}!".format(player_house))
    if player_characteristic < opponent_characteristic:
        print(opponent_colour + 'Oh no, you lost :\'( !')
        round_winner = 'opponent'
        print(player_colour + "One point to {}!".format(opponent_house))
    if player_characteristic == opponent_characteristic:
        print('Its a draw!')
        round_winner = 'both'

    next_round = input('Press enter to continue! ')

    return round_winner


for rounds in range(round):
    round_winner = begin_round(player_score,computer_score)
    if round_winner == 'player':
        player_score = player_score + 1
    if round_winner == 'opponent':
        computer_score = computer_score + 1

    print(player_colour + 'Your score: {}'.format(player_score))
    print(opponent_colour + 'Opponent\'s score: {}'.format(computer_score))


play_again = input('Do you want to play again or exit? ')

if play_again == 'exit' or play_again == 'Exit':
    print(player_colour + "Play again soon :) ".format(player_score, player_house))
else:
    begin_round(player_score, computer_score)