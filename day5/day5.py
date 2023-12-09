def preprocess(inputfile: str) -> list[str]:
    """ Read in and 'clean' imput """
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


def decode_almanac_less_memory(almanac: list[list]) -> int:
    
    maps = clean_maps(almanac_maps=almanac)
    return run_throug_maps(79, maps)

def decode_almanac(almanac: list[list]) -> list[int]:
    seeds = get_seeds(almanac[0])
    maps = clean_maps(almanac_maps=almanac)
    
    return [run_throug_maps(seed, maps) for seed in seeds]

def run_throug_maps(seed: int, maps: list[list]) -> int:
    location = seed
    for map in maps:
        for instruction in map:
            get_shifts(instruction)
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

def get_shifts(instruction: str):
    instruction = instruction.split(' ')

    dest_start = int(instruction[0])
    source_start = int(instruction[1])
    shift = dest_start - source_start
    
    left_border, right_border = source_start, source_start + int(instruction[2]) - 1

    return [shift, left_border, right_border]

def clean_maps(almanac_maps: list[list]) -> list[list]:
    return [map[1:len(map)] for map in almanac_maps]

def get_seeds(seed_input: str) -> list[int]:
    seed_vals = seed_input[0].split(':')[1]
    return [int(seed) for seed in seed_vals.split(' ') if seed != '']

if __name__ == "__main__":
    input = preprocess('day5/input.txt')
    almanac = split_maps(input=input)
    print(decode_almanac_less_memory(almanac=almanac))
    