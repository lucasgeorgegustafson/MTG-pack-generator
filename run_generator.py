import json
import sys
from set_dict import set_dict

def run_generator(filepath, expansion, num_packs=1):

    if expansion in set_dict:
        set_cards = get_set_cards(filepath, expansion)

        while num_packs > 0:
            gen = set_dict[expansion](set_cards)
            gen.generate_pack()
            num_packs -= 1

    else:
        print(f'Expansion {expansion} is unsupported.')

def get_set_cards(filepath, expansion):

    with open(filepath) as cards_json:
        cards = json.load(cards_json)

    set_cards = []

    for card in cards:

        if card['set'] == expansion.lower():
            set_cards.append(card)

    return set_cards

if __name__ == '__main__':
    try:
        run_generator(sys.argv[1], sys.argv[2], int(sys.argv[3]))
    except IndexError:
        run_generator(sys.argv[1], sys.argv[2])

