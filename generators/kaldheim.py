import random
from generators.base import BaseGenerator

class KaldheimGenerator(BaseGenerator):

    def __init__(self, set_cards):
        super().__init__(set_cards)
        self.snow_covered_lands = []
        self.dual_lands = []

    def fix_sort(self):

        for card in self.commons:

            if 'Land' in card['type_line'] and card['name'] != 'Shimmerdrift Vale':
                self.lands.append(card)

        for card in self.lands:

            self.commons.remove(card)

            if 'Basic' in card['type_line'] and 'Snow-Covered' in card['name']:
                self.snow_covered_lands.append(card)
            elif 'Basic' not in card['type_line']:
                self.dual_lands.append(card)

        self.lands = self.dual_lands * 5 + self.snow_covered_lands * 7

