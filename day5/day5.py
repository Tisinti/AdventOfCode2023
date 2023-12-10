from tqdm import tqdm

def preprocess(inputfile: str) -> list[str]:
    """ Read in and 'clean' input """
    with open(inputfile) as f:
        input = f.readlines()
    return [line.replace('\n', '') for line in input]

def split_maps(input: list) -> list[list]:
    res = []
    full = []
    for item in input:
        if item == '':
            full.extend([res])
            res = []
            continue
        res.append(item)
    full.extend([res])
    return full

def decode_almanac_big(almanac: list[list]) -> int:
    maps = clean_maps(almanac_maps=almanac)

    minimum = min(get_seeds(almanac[0]))
    maxximum = max([sum(pair) for pair in get_seed_pairs(get_seeds(almanac[0]))])
    
    low = run_throug_maps(minimum, maps)

    for seed in tqdm(range(minimum, maxximum)):
        location = run_throug_maps(seed, maps)
        if location < low:
            low = location
    return low

def decode_almanac(almanac: list[list]) -> list[int]:
    seeds = get_seeds(almanac[0])
    maps = clean_maps(almanac_maps=almanac)
    
    return [run_throug_maps(seed, maps) for seed in seeds]

def run_throug_maps(seed: int, maps: list[list]) -> int:
    location = seed
    for map in maps:
        for instruction in map:
            if location != get_range(instruction, location):
                location = get_range(instruction, location)
                break
            else:
                location = get_range(instruction, location)
    return location

def get_range(instruction: str, source_num) -> dict:
    instruction = instruction.split(' ')

    dest_start = int(instruction[0])
    source_start = int(instruction[1])
    map_length = int(instruction[2])


    if source_num >= source_start and source_num < (source_start + map_length):
        shift = source_start - dest_start
        return abs(source_num - shift)
    return source_num

def clean_maps(almanac_maps: list[list]) -> list[list]:
    return [map[1:len(map)] for map in almanac_maps]

def get_seeds(seed_input: str) -> list[int]:
    seed_vals = seed_input[0].split(':')[1]
    return [int(seed) for seed in seed_vals.split(' ') if seed != '']

def get_seed_pairs(seeds: str) -> list[list]:
    res = []
    pair = []
    for i, seed in enumerate(seeds): 
        pair.append(seed)
        if i%2 != 0:
            res.extend([pair])
            pair = []
    return res

if __name__ == "__main__":
    input = preprocess('day5/input.txt')
    almanac = split_maps(input=input)
    print(decode_almanac_big(almanac))
    #I WILL COME BACK: YOU CAN SHRINK THE MAPS TOGETHER AND ITERATE OVER THE BORDERS
    