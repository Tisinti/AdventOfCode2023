
from math import prod


def race(pairs: list[tuple]): 
    race_wins = []
    for pair in pairs:
        race_wins.append(get_win_times(pair[0], pair[1]))
    return prod (race_wins)

def get_win_times(time, max_distance) -> int:
    count = 0
    
    for second in range(1,time):
        distance = second * (time - second)
        if distance > max_distance:
            count += 1

    return count

def get_pairs(input: list[str]):
    res = []
    for info in input:
        val = info.split(':')[1]
        res.extend([[int(item) for item in val.split(' ') if item != '']])
    return list(zip(res[0], res[1]))

def get_big_pairs(input):
    res = []
    for info in input:
        val = info.split(':')[1]
        res.append(int(val.replace(' ', '')))
    return [res]

def preprocess(inputfile: str) -> list[str]:
    """ Read in and 'clean' imput """
    with open(inputfile) as f:
        input = f.readlines()
    return [line.replace('\n', '') for line in input]

if __name__ == "__main__":
    input = preprocess('day6/input.txt')
    pairs = get_pairs(input)
    big_pairs = get_big_pairs(input)
    print(race(big_pairs))