import json
import sys
import random

def generate_pack(filepath, expansion):

    with open(filepath) as cards_json:

        cards = json.load(cards_json)

    set_cards = []
    commons = []
    uncommons = []
    rares_and_mythics = []
    pack = []

    LANDS = ['Swamp', 'Island', 'Plains', 'Mountain', 'Forest']

    for card in cards:

        if card['set'] == expansion and 'Basic' not in card['type_line']:
            set_cards.append(card)

    for card in set_cards:

        if card['rarity'] == 'common':
            commons.append(card)
        elif card['rarity'] == 'uncommon':
            uncommons.append(card)
        else:
            rares_and_mythics.append(card)

    pack.append(random.choice(rares_and_mythics)['name'])

    pack.extend([card['name'] for card in random.choices(uncommons, k=3)])

    pack.extend([card['name'] for card in random.choices(commons, k=10)])

    pack.append(random.choice(LANDS))

    for card in pack:
        print(card)

if __name__ == '__main__':
    generate_pack(sys.argv[1], sys.argv[2])

