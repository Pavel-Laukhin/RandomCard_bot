# TODO: Внедрить количество раундов (3 попытки с подсказками)

from random import choice


class RandomCard:
    VALUES = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    SUITS = ["H", "D", "C", "S"]
    SUIT_SYMBOLS = {"H": "♡", "D": "♢", "C": "♣︎", "S": "♠︎"}

    def __init__(self):
        self.random_value = choice(self.VALUES)
        self.random_suit = choice(self.SUITS)

        self.suits_list = "\n".join(
            [f"{suit}. {self.SUIT_SYMBOLS[suit]}" for suit in self.SUITS])
        self.suit_symbol = self.SUIT_SYMBOLS[self.random_suit]
        self.prettyfied = self.random_value + self.suit_symbol


class CardGame:
    GAME_MODES = [1, 2, 3, 4]
    game_mode = 1

    def start(self):
        self.greeting()
        self.ask_game_mode()
        self.play()

    def greeting(self):
        print(
            "Hello, stranger!\n\n"
            "I will generate a random card, but I won't tell you which one.\n"
            "You should guess the card or its attribute.\n\n"
            "What do you want to try to guess?\n\n"
            "1. Color (red or black)\n"
            "2. Suit (hearts, diamonds, clubs or spades)\n"
            "3. Card value (e.g. \"2\", \"10\", \"J\", \"Q\", \"K\", \"A\", etc.)\n"
            "4. Card itself (e.g. 2H (two hearts) or KD (king diamonds))\n\n"
            "Enter 1, 2, 3 or 4.")

    def ask_game_mode(self):
        mode = int(input())
        if mode not in self.GAME_MODES:
            print("\nInvalid game mode. Sorry, try again.")
            self.ask_game_mode()
            return
        self.game_mode = mode

    def play(self):
        card = RandomCard()

        if self.game_mode == 1:
            print("Guess the color: Red or Black?")
            self.play_game_one(card)

        elif self.game_mode == 2:
            print(f"Guess the suit?\n{card.suits_list}")
            self.play_game_two(card)

        elif self.game_mode == 3:
            print(f"Guess the value: {', '.join(card.VALUES)}?")
            self.play_game_three(card)

        else:
            print("Guess the card itself (like \"2H\" (two hearts) or \"KD\" "
                  "(king diamonds))?")
            self.play_game_four(card)

    def play_game_one(self, card):
        player_answer = input()
        ACCEPTABLE_ANSWERS = ["Red", "Black"]
        if player_answer not in ACCEPTABLE_ANSWERS:
            print("\nSorry, but the acceptable answer is only \"Red\" or "
                  "\"Black\". Please, try again.")
            self.play_game_one(card)
            return

        if player_answer == "Red" and card.random_suit in ["H", "D"]:
            print("Correct! The card was: " + card.prettyfied)
        elif player_answer == "Black" and card.random_suit in ["S", "C"]:
            print("Correct! The card was: " + card.prettyfied)
        else:
            print("Incorrect! The card was: " + card.prettyfied)

    def play_game_two(self, card):
        player_answer = input()
        if player_answer not in card.SUITS:
            print(
                "\nSorry, but the acceptable answer shoud be one of "
                f"the following: {', '.join(card.SUITS)}. Please, try again.")
            self.play_game_two(card)
            return

        if player_answer == card.random_suit:
            print("Correct! The card was: " + card.prettyfied)
        else:
            print("Incorrect! The card was: " + card.prettyfied)

    def play_game_three(self, card):
        player_answer = input()
        if player_answer not in card.VALUES:
            print(
                "\nSorry, but the acceptable answer shoud be one of "
                f"the following: {', '.join(card.VALUES)}. Please, try again.")
            self.play_game_three(card)
            return

        if player_answer == card.random_value:
            print("Correct! The card was: " + card.prettyfied)
        else:
            print("Incorrect! The card was: " + card.prettyfied)

    def play_game_four(self, card):
        player_answer = input()

        if ((len(player_answer) == 3 and player_answer[:2] != "10")
                or (len(player_answer) not in [2, 3])):
            print(
                "Sorry, but the acceptable answer should consist of the value "
                "and the suit, no spaces, 2 or 3 letters. For example, \"5C\" "
                "or \"10S\"")
            self.play_game_four(card)
            return

        value = player_answer[:2] if len(
            player_answer) == 3 else player_answer[0]
        if value not in card.VALUES:
            print("Sorry, but the the value of the card should be one of the "
                  f"followings: {', '.join(card.VALUES)}")
            self.play_game_four(card)
            return

        suit = player_answer[2] if len(
            player_answer) == 3 else player_answer[1]
        if suit not in card.SUITS:
            print("\nSorry, but the suit should be the one of the followings: "
                  f"{', '.join(card.SUITS)}. Please, try again.")
            self.play_game_four(card)
            return

        if value == card.random_value and suit == card.random_suit:
            print("Correct! The card was: " + card.prettyfied)
        else:
            print("Incorrect! The card was: " + card.prettyfied)


CardGame().start()
