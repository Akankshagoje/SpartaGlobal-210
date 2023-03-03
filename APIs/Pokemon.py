import requests
import random

names_stats_dict = {}
player_1_dict = {}
player_2_dict = {}

player_1 = input('Please enter Player 1 name: ')
player_1 = player_1.upper()
player_2 = input('Please enter Player 2 name: ')
player_2 = player_2.upper()


def random_pokemon_generator():
    response = requests.get('https://pokeapi.co/api/v2/pokemon?limit=5000')
    data = response.json()
    random_pokemon = random.choices(data['results'], k=3)
    for i in range(3):
        stats_list = []
        stats_count = 0
        p_name = random_pokemon[i]['name']
        stats_response = requests.get(random_pokemon[i]['url'])
        stats_data = stats_response.json()
        for j in range(6):
            stat = stats_data['stats'][j]['stat']['name'] + ' ' + str(stats_data['stats'][j]['base_stat'])
            stats_count += int(stats_data['stats'][j]['base_stat'])
            stats_list.append(stat)
        names_stats_dict[i + 1] = [p_name, stats_list, stats_count]
    # print(names_stats_dict)
    return names_stats_dict


def player_one():
    while True:
        try:
            names_stats = random_pokemon_generator()
            player1_pick = input(
                'Hi ' + player_1 + '! Please pick any number for that particular pokemon: 1: {}, 2: {}, 3: {} '.format(
                    names_stats[1][0], names_stats[2][0], names_stats[3][0]))
            if int(player1_pick) == 1:
                player_1_dict[player_1] = names_stats_dict[1]
                print(player_1 + ' you picked: ' + player_1_dict[player_1][0])
                return player_1_dict[player_1][-1]
            elif int(player1_pick) == 2:
                player_1_dict[player_1] = names_stats_dict[2]
                print(player_1 + ' you picked: ' + player_1_dict[player_1][0])
                return player_1_dict[player_1][-1]
            elif int(player1_pick) == 3:
                player_1_dict[player_1] = names_stats_dict[3]
                print(player_1 + ' you picked: ' + player_1_dict[player_1][0])
                return player_1_dict[player_1][-1]
            else:
                print('Please enter the number from the given list')
        except:
            print('Please enter the number from the given list')


def player_two():
    while True:
        try:
            names_stats = random_pokemon_generator()
            player2_pick = input(
                'Hi ' + player_2 + '! Please pick any number for that particular pokemon: 1: {}, 2: {}, 3: {} '.format(
                    names_stats[1][0], names_stats[2][0], names_stats[3][0]))
            if int(player2_pick) == 1:
                player_2_dict[player_2] = names_stats[1]
                print(player_2 + ' you picked: ' + player_2_dict[player_2][0])
                return player_2_dict[player_2][-1]
            elif int(player2_pick) == 2:
                player_2_dict[player_2] = names_stats[2]
                print(player_2 + ' you picked: ' + player_2_dict[player_2][0])
                return player_2_dict[player_2][-1]
            elif int(player2_pick) == 3:
                player_2_dict[player_2] = names_stats[3]
                print(player_2 + ' you picked: ' + player_2_dict[player_2][0])
                return player_2_dict[player_2][-1]
            else:
                print('Please enter the number from the given list')
        except:
            print('Please enter the number from the given list')


player_1_score = player_one()
player_2_score = player_two()

if player_1_score > player_2_score:
    print(player_1 + ' score is ' + str(player_1_score))
    print(player_2 + ' score is ' + str(player_2_score))
    print(player_1.upper() + ' wins!')
else:
    print(player_1 + ' score is ' + str(player_1_score))
    print(player_2 + ' score is ' + str(player_2_score))
    print(player_2.upper() + ' wins!')
