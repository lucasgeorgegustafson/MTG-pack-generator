import json
import sys
from set_dict import set_dict

def run_generator(filepath, expansion, num_packs=1):
    """
    gen's initialization method is passed an empty
    set for its set_cards parameter, which we can
    then reassign after reading and parsing the bulk
    data. This way, if we try to instantiate a generator
    class which doesn't conform to our interface, the
    program will exit without needlessly constructing
    the set_cards list.
    """

    if expansion not in set_dict:
        print(f'Expansion {expansion} is unsupported')
    else:
        gen = set_dict[expansion]([])
        set_cards = get_set_cards(filepath, expansion)
        gen.set_cards = set_cards

        while num_packs > 0:
            gen.generate_pack()
            num_packs -= 1

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

