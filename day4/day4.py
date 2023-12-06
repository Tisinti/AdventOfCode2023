from tqdm import tqdm

def split_values(line: str) -> list[list]:
    values = line.split(':')[1]
    values = [list(filter(None, val.split(" "))) for val in values.split('|')]
    return values

def preprocess(inputfile: str) -> list[str]:
    """ Read in and 'clean' input """
    with open(inputfile) as f:
        input = f.readlines()
    return [line.replace('\n', '') for line in input]

def sum_tickets(input: list[list]) -> int:
    res = []
    for i in tqdm(range(len(input))):
        res.append(recursive_win(input=input[i:len(input)], line=input[i]))
    return sum(res)

def recursive_win(input: list[list], line: list[list]):
    corr = get_correct_count(line[0], line[1])
    res = 0
    if corr == 0:
        return 1

    start = input.index(line)+1 
    stop = start+corr

    for line in input[start:stop]:
        res += recursive_win(input=input, line=line)
    res+=1
    return res

def get_correct_count(test, winners):
    correct = [check_if_match(num, winners) for num in test]
    return len(list(filter(None, correct)))


def count_winners(test: list[int], winners: list[int]) -> int:
    correct = [check_if_match(num, winners) for num in test]
    corr_count = len(list(filter(None, correct)))-1
    if corr_count < 0:
        return 0
    return pow(2, corr_count)

def check_if_match(num: int, winners: list) -> bool:
    if num in set(winners):
        return True


if __name__ == "__main__":
    #res_1 = [count_winners(line[0], line[1]) for line in split_input]
    input = [split_values(line) for line in preprocess('day4/input.txt')]

    res_1 = [count_winners(line[0], line[1]) for line in input]
    print(sum(res_1))
    #I dont really use recursion very often and it shows lol
    #The recursion needs to store the subtree results somewhere for better results...
    res_2 = sum_tickets(input=input)
    print(res_2)

