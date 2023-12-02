import re
import numpy as np


cols = ['red', 'green', 'blue']
game_rules = [12, 13, 14]

def count_color(game: list[str]):
    game_num = game.pop(0)
    #extend list with match rounds
    #and yes i know i use to many list comprehensions
    rounds = [match for match in game for match in match.replace(" ", "").split(",")]
    color_count = []
    for col in cols: 
        #extract all occurences of specific color
        count = [re.findall(f"\d*{col}", round)[0] for round in rounds if re.findall(f"\d*{col}", round)]
        #extract the numbers
        count = [int(''.join(re.findall("\d*", round))) for round in count]
        #sum them up
        color_count.append(max(count))

    return color_count, game_num

def check_size(color_count: list, game_num: str):
    game_num = int(''.join(re.findall("\d*", game_num)))
    for i in range(len(color_count)):
        if color_count[i] > game_rules[i]:
            return 0
    return game_num

def get_min_power(color_count:list):
    return np.prod(color_count)


if __name__ == "__main__":
    
    with open('day2/input.txt') as f:
        input = f.readlines()
    input = [line.replace('\n', '') for line in input]
    input = [line.replace(":", ";").split(";") for line in input]
    result_1, result_2 = [], []
    for game in input:
        count, game_num = count_color(game)
        result_1.append(check_size(count, game_num))
        result_2.append(get_min_power(count))

    print(sum(result_1))
    print(sum(result_2))

