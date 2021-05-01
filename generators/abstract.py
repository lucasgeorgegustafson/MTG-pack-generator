from abc import ABC, abstractmethod

class AbstractGenerator(ABC):

    @abstractmethod
    def sort_by_rarity(self):
        pass

    @abstractmethod
    def roll_for_mythic(self):
        pass

    @abstractmethod
    def fix_sort(self):
        pass

    @abstractmethod
    def print_pack(self):
        pass

    @abstractmethod
    def generate_pack(self):
        pass

