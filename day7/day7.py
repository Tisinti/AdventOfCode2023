def rank_bids(players: list[list]):
    hands, bids = zip(*players)
    hand_rank ={hand : evaluate_hand(hand) for hand, bid in zip(hands, bids)}

    sorted_ranks  = dict(sorted(hand_rank.items(), key=lambda x: x[1]))

    return sorted_ranks


def sort_intern(players: list[list]):
    player_sort = rank_bids(players=players)

    sorted = []
    for x in range(7):
        hands = [key for key, value in player_sort.items() if value == x]
        if not hands:
            continue
        
        sorted.extend(compare_equal_num(hands=hands))
    return sorted

def calc_winning(players: list[list]):
    sorted = sort_intern(players=players)
    print(sorted)
    hands, bids = zip(*players)
    ranking = {hand : i+1 for i, hand in enumerate(sorted)}
    bidding = {hand : int(bid) for hand, bid in zip(hands, bids)}

    winning = 0
    for hand in hands:
        winning += ranking[hand] * bidding[hand]

    return winning

def compare_equal_num(hands: list[str]):
    sorted = []
    start = hands.pop(0)
    sorted.append(start)
    for hand in hands:
        sorted = comp_hands(hand, sorted)
    return sorted

def comp_hands(hand: str, sorted: list[str]) -> list[str]:
    for pos, stack in enumerate(sorted):
            for i, card in enumerate(hand):
                card, start_card= card_to_value(card), card_to_value(stack[i])
                if card < start_card:
                    sorted.insert(pos,hand)
                    return sorted
                if card > start_card:
                    break
    sorted.append(hand)
    return sorted


def card_to_value(card: str):
    value_dict = {'A': 14, 'K': 13, 'Q': 12, 'J': 11, 'T': 10, 'J':1}
    
    try:
        return int(card)
    except Exception:
        return value_dict[card]


def evaluate_hand(hand: str) -> int:
    """One of a Kind: 0, One Pair: 1, Two Pair: 2, Three of a Kind: 3
    Full House: 4, Four of a Kind: 5, Five of a Kind: 6"""
    cards = [card_to_value(card) for card in list(hand)]
    unique_cards = list(set(cards))
    joker = 0
    occ = []

    for unique in unique_cards:
        c = 0
        for card in cards:
            if card == 1 and unique == 1:
                joker += 1
                continue
            if card == unique:
                c += 1
        occ.append(c)
    
    occ[occ.index(max(occ))] += joker
    if joker > 0 and joker < 5:
        occ.remove(0)

    if len(occ) == 5:
        return 0
    elif len(occ) == 1:
        return 6
    elif len(occ) == 4:
        return 1
    elif len(occ) == 3:
        if 3 in occ: return 3
        else: return 2
    elif len(occ) == 2:
        if 4 in occ: return 5
        else: return 4


def preprocess(inputfile: str) -> list[str]:
    """ Read in and 'clean' input """
    with open(inputfile) as f:
        input = f.readlines()
    return [line.replace('\n', '') for line in input]


def split_hand_bid(input: list[str]) -> list[list]:
    return [player.split(" ") for player in input]


if __name__ == "__main__":
    input = preprocess('day7/input.txt')
    players = split_hand_bid(input)
    print(calc_winning(players))
   
    