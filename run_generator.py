import json
import sys
from set_dict import set_dict

def run_generator(filepath, expansion, num_packs=1):

    if expansion in set_dict:
        gen = set_dict[expansion](get_set_cards(filepath, expansion))

        while num_packs > 0:
            gen.generate_pack()
            num_packs -= 1

        return 'Hope these will do!'
    else:
        return f'Expansion {expansion} is unsupported.'

def get_set_cards(filepath, expansion):

    with open(filepath) as cards_json:
        cards = json.load(cards_json)

    set_cards = []

    for card in cards:
        if card['set'] == expansion.lower() and 'Basic' not in card['type_line']:
            set_cards.append(card)

    return set_cards

if __name__ == '__main__':
    try:
        run_generator(sys.argv[1], sys.argv[2], int(sys.argv[3]))
    except IndexError:
        run_generator(sys.argv[1], sys.argv[2])

