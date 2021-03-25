import json
import sys
import random

def generate_pack(filepath, expansion, num_packs=1):

    with open(filepath) as cards_json:
        cards = json.load(cards_json)

    set_cards = []
    commons = []
    uncommons = []
    rares = []
    mythics = []
    pack = []

    LANDS = ['Swamp', 'Island', 'Plains', 'Mountain', 'Forest']

    for card in cards:
        if card['set'] == expansion.lower() and 'Basic' not in card['type_line']:
            set_cards.append(card)

    for card in set_cards:
        if card['rarity'] == 'common':
            commons.append(card)
        elif card['rarity'] == 'uncommon':
            uncommons.append(card)
        elif card['rarity'] == 'rare':
            rares.append(card)
        elif card['rarity'] == 'mythic':
            mythics.append(card)
        else:
            raise Exception('Unknown card rarity"' + card['rarity'] + '" for card "' + card['name'] + '"')

    number_of_mythics = 0
    number_of_rares = 1
    number_of_uncommons = 3
    number_of_commons = 10

    if roll_for_mythic() and len(mythics) > 0:
        number_of_mythics, number_of_rares = 1, 0

    while num_packs > 0:
        pack.extend([card['name'] for card in random.choices(mythics, k=number_of_mythics)])
        pack.extend([card['name'] for card in random.choices(rares, k=number_of_rares)])
        pack.extend([card['name'] for card in random.choices(uncommons, k=number_of_uncommons)])
        pack.extend([card['name'] for card in random.choices(commons, k=number_of_commons)])

        pack.append(random.choice(LANDS))

        for card in pack:
            print(card)

        print()

        num_packs -= 1
        pack = []

def roll_for_mythic():
    """Randomly check if a pack should have a mythic instead of a rare (12.5%)"""
    return random.randint(1,1000) <= 125

if __name__ == '__main__':
    try:
        generate_pack(sys.argv[1], sys.argv[2], int(sys.argv[3]))
    except IndexError:
        generate_pack(sys.argv[1], sys.argv[2])

