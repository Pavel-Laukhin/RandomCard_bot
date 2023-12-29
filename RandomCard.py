from random import choice
from LocalizedString import Language


class RandomCard:

    def __init__(self, language: Language):
        if language == Language.en:
            self.VALUES = [
                "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K",
                "A"
            ]
            self.SUITS = ["H", "D", "C", "S"]
            self.RED = "Red"
            self.BLACK = "Black"
            self.COLORS = ["Red", "Black"]
            self.RED_SUITS = ["H", "D"]
            self.BLACK_SUITS = ["C", "S"]
            SUIT_SYMBOLS = {"H": "♡", "D": "♢", "C": "♣︎", "S": "♠︎"}
        else:
            self.VALUES = [
                "2", "3", "4", "5", "6", "7", "8", "9", "10", "В", "Д", "К",
                "Т"
            ]
            self.SUITS = ["Ч", "Б", "К", "П"]
            self.RED = "Красный"
            self.BLACK = "Черный"
            self.COLORS = ["Красный", "Черный"]
            self.RED_SUITS = ["Ч", "Б"]
            self.BLACK_SUITS = ["К", "П"]
            SUIT_SYMBOLS = {"Ч": "♡", "Б": "♢", "К": "♣︎", "П": "♠︎"}
    
        self.random_value = choice(self.VALUES).lower()
        self.random_suit = choice(self.SUITS).lower()
    
        self.suits_list = "\n".join(
            [f"{suit}. {SUIT_SYMBOLS[suit]}" for suit in self.SUITS])
        suit_symbol = SUIT_SYMBOLS[self.random_suit.upper()]
        self.prettyfied = self.random_value.upper() + suit_symbol
    