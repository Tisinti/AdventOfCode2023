import re


def check_digit_symbol(input: list[str]) -> list[int]:
    found_nums = []
    for i, line in enumerate(input):
        for found in re.finditer("\d+", line):
            num = int(found.group())
            start, stop = found.span()[0]-1, found.span()[1]+1
            if start < 0:
                start = 0

            #if none-digit except dot is between start-stop span above digit
            if i > 0 and re.search("(?!\.)\D", input[i-1][start:stop]):
                found_nums.append(num)
            elif re.search("(?!\.)\D", line[start:stop]):
                found_nums.append(num)
            elif i < len(input)-1 and re.search("(?!\.)\D", input[i+1][start:stop]):
                found_nums.append(num)

    return found_nums

def get_gear_ratio(input: list[str]) -> list[int]:
    """ Get the Ratio of all gears """

    found_nums = []
    potentials = {}
    for i, line in enumerate(input):
        for found in re.finditer("\d+", line):
            num = int(found.group())
            start, stop = found.span()[0]-1, found.span()[1]+1
            if start < 0:
                start = 0

            #check if gear is around num and mark gear as X
            if i > 0 and re.search("\*", input[i-1][start:stop]):
                input[i-1], pos_X = replace_found_gear(start, stop, input[i-1])
                pos_X = pos_X + (i-1, )
                potentials.update({pos_X : num })
                continue
            elif re.search("\*", line[start:stop]):
                line, pos_X = replace_found_gear(start, stop, line)
                pos_X = pos_X + (i, )
                potentials.update({pos_X : num })
                continue
            elif i < len(input)-1 and re.search("\*", input[i+1][start:stop]):
                input[i+1], pos_X = replace_found_gear(start, stop, input[i+1])
                pos_X = pos_X + (i+1, )
                potentials.update({pos_X : num })
                continue
            
            #check for marked Xs and compute the ratio 
            if i > 0 and re.search("X", input[i-1][start:stop]):
                ratio = num * potentials[get_X_pos(start, i-1, input[i-1][start:stop])]
                found_nums.append(ratio)
            elif re.search("X", line[start:stop]):
                ratio = num * potentials[get_X_pos(start, i, line[start:stop])]
                found_nums.append(ratio)
            elif i < len(input)-1 and re.search("X", input[i+1][start:stop]):
                ratio = num * potentials[get_X_pos(start, i+1, input[i+1][start:stop])]
                found_nums.append(ratio)

        input[i] = line
    
    return found_nums

def replace_found_gear(start: int, stop: int, line: str) -> tuple[str, tuple]:
    """ Replace the found Gear with an X and save the Position"""

    first, midle, last = line[0:start], line[start:stop], line[stop:len(line)]
    pos_X = [pos.span() for pos in re.finditer("\*", midle)][0]
    pos_X = (pos_X[0] + start, pos_X[1] + start)
    changed = re.sub("\*", "X", midle)
    return first+changed+last, pos_X

def get_X_pos(start, i, substring) -> tuple[int, int, int]:
    """Get Postion of already marked gear (returns tuple (x,y,z))"""

    pos_X = [pos.span() for pos in re.finditer("X", substring)][0]
    pos_X = (pos_X[0] + start, pos_X[1] + start, i)
    return pos_X

def preprocess(inputfile: str) -> list[str]:
    """ Read in and 'clean' imput """
    with open(inputfile) as f:
        input = f.readlines()
    return [line.replace('\n', '') for line in input]

if __name__ == "__main__":
    input = preprocess('day3/input.txt')
    res_1 = check_digit_symbol(input)
    res_2 = get_gear_ratio(input)
    print(sum(res_1))
    print(sum(res_2))
