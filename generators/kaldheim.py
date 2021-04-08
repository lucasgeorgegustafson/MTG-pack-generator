import random
from generators.base import BaseGenerator

class KaldheimGenerator(BaseGenerator):

    def __init__(self, set_cards):
        super().__init__(set_cards)

    def fix_lands(self):

        self.lands = ['Snow-Covered Mountain', 'Snow-Covered Plains', 'Snow-Covered Forest', 'Snow-Covered Swamp', 'Snow-Covered Island']
        self.lands = self.lands * 7

        for card in self.commons:

            if 'Land' in card['type_line'] and card['name'] != 'Shimmerdrift Vale':
                self.lands.extend(5 * [card['name']])

