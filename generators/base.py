from generators.abstract import AbstractGenerator
import random

class BaseGenerator(AbstractGenerator):

    def __init__(self, set_cards):

        self.set_cards = set_cards
        self.pack = []
        self.number_of_commons = 10
        self.number_of_uncommons = 3
        self.number_of_rares = 1
        self.number_of_mythics = 0
        self.number_of_lands = 1
        self.commons = []
        self.uncommons = []
        self.rares = []
        self.mythics = []
        self.lands = []

    def sort_by_rarity(self):

        for card in self.set_cards:
            if card['rarity'] == 'common':
                self.commons.append(card)
            elif card['rarity'] == 'uncommon':
                self.uncommons.append(card)
            elif card['rarity'] == 'rare':
                self.rares.append(card)
            elif card['rarity'] == 'mythic':
                self.mythics.append(card)
            else:
                raise Exception('Unknown card rarity"' + card['rarity'] + '" for card "' + card['name'] + '"')

    def roll_for_mythic(self):
        """Randomly check if a pack should have a mythic instead of a rare (12.5%)"""
        return random.randint(1,1000) <= 125

    def fix_sort(self):
        pass

    def print_pack(self):

        for card in self.pack:
            print(card)

        print()

    def generate_pack(self):

        self.sort_by_rarity()
        self.fix_sort()

        if self.roll_for_mythic() and len(self.mythics) > 0:
            self.number_of_mythics, self.number_of_rares = 1, 0

        self.pack.extend([card['name'] for card in random.choices(self.mythics, k=self.number_of_mythics)])
        self.pack.extend([card['name'] for card in random.choices(self.rares, k=self.number_of_rares)])
        self.pack.extend([card['name'] for card in random.choices(self.uncommons, k=self.number_of_uncommons)])
        self.pack.extend([card['name'] for card in random.choices(self.commons, k=self.number_of_commons)])
        self.pack.extend([card['name'] for card in random.choices(self.lands, k=self.number_of_lands)])

        self.print_pack()

        self.pack = []

