import re 

spelled_out = {'one' : '1', 'two' : '2', 'three' : '3', 'four' : '4', 'five' : '5',
              'six' : '6', 'seven' : '7', 'eight' : '8', 'nine' : '9'}

def parseInt(code: str) -> int:
    num = []
    pos = []

    for found in re.finditer('\d', code):
        num.append(found.group()), pos.append(found.span()[1])

    for spelled, digit in spelled_out.items():
        num.extend([digit for found in re.finditer(spelled,code)])
        pos.extend([found.span()[1] for found in re.finditer(spelled,code)])
    
    num_spans = zip(num, pos)

    all_nums = sorted(num_spans, key = lambda x: x[1])
    res = list(map(list, zip(*all_nums)))[0]

    if len(res) == 1:
        res.extend(res)
    
    res = [res[0], res[-1]]
    
    return int(''.join(res))

if __name__ == "__main__":
    with open('day1/input.txt') as f:
        input = f.readlines()
    input = [line.replace('\n', '') for line in input]
    all_digits = [parseInt(line) for line in input]
    print(sum(all_digits))
    #print(parseInt("nine"))


