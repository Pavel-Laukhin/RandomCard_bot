# TODO: Внедрить два языка

from random import choice


class RandomCard:
    VALUES = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    SUITS = ["H", "D", "C", "S"]
    SUIT_SYMBOLS = {"H": "♡", "D": "♢", "C": "♣︎", "S": "♠︎"}

    def __init__(self):
        self.random_value = choice(self.VALUES).lower()
        self.random_suit = choice(self.SUITS).lower()

        self.suits_list = "\n".join(
            [f"{suit}. {self.SUIT_SYMBOLS[suit]}" for suit in self.SUITS])
        self.suit_symbol = self.SUIT_SYMBOLS[self.random_suit.upper()]
        self.prettyfied = self.random_value.upper() + self.suit_symbol


class CardGame:
    GAME_MODES = [1, 2, 3, 4]
    game_mode = None
    attempts = None

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
            self.attempts = 2
            self.play_game_two(card)

        elif self.game_mode == 3:
            print(f"Guess the value: {', '.join(card.VALUES)}?")
            self.attempts = 3
            self.play_game_three(card)

        else:
            print("Guess the card itself (like \"2H\" (two hearts) or \"KD\" "
                  "(king diamonds))?")
            self.attempts = 3
            self.play_game_four(card)

    def play_game_one(self, card):
        player_answer = input().lower()
        ACCEPTABLE_ANSWERS = ["red", "black"]
        if player_answer not in ACCEPTABLE_ANSWERS:
            print("\nSorry, but the acceptable answer is only \"Red\" or "
                  "\"Black\". Please, try again.")
            self.play_game_one(card)
            return

        if player_answer == "red" and card.random_suit in ["h", "d"]:
            print("Correct! The card was: " + card.prettyfied)
        elif player_answer == "black" and card.random_suit in ["s", "c"]:
            print("Correct! The card was: " + card.prettyfied)
        else:
            print("Incorrect! The card was: " + card.prettyfied)

    def play_game_two(self, card):
        player_answer = input().lower()
        lowercase_suits = [suit.lower() for suit in card.SUITS]
        if player_answer not in lowercase_suits:
            print(
                "\nSorry, but the acceptable answer shoud be one of "
                f"the following: {', '.join(card.SUITS)}. Please, try again.")
            self.play_game_two(card)
            return

        if player_answer == card.random_suit:
            print("Correct! The card was: " + card.prettyfied)
        else:
            self.attempts -= 1
            if self.attempts > 0:
                print(f"Oops! Incorrect! You have {self.attempts} more tryes. "
                      "Try again :)")
                self.show_hint_for_game_two(card, player_answer)
                self.play_game_two(card)
            else:
                print("Incorrect! The card was: " + card.prettyfied)

    def play_game_three(self, card):
        player_answer = input().lower()
        lowercase_values = [value.lower() for value in card.VALUES]
        if player_answer not in lowercase_values:
            print(
                "\nSorry, but the acceptable answer shoud be one of "
                f"the following: {', '.join(card.VALUES)}. Please, try again.")
            self.play_game_three(card)
            return

        if player_answer == card.random_value:
            print("Correct! The card was: " + card.prettyfied)
        else:
            self.attempts -= 1
            if self.attempts > 0:
                print(f"Oops! Incorrect! You have {self.attempts} more tryes. "
                      "Try again :)")
                self.show_hint_for_game_three(card, player_answer)
                self.play_game_three(card)
            else:
                print("Incorrect! The card was: " + card.prettyfied)

    def play_game_four(self, card):
        player_answer = input().lower()

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
        lowercase_values = [value.lower() for value in card.VALUES]
        if value not in lowercase_values:
            print("Sorry, but the the value of the card should be one of the "
                  f"followings: {', '.join(card.VALUES)}")
            self.play_game_four(card)
            return

        suit = player_answer[2] if len(
            player_answer) == 3 else player_answer[1]
        lowercase_suits = [suit.lower() for suit in card.SUITS]
        if suit not in lowercase_suits:
            print("\nSorry, but the suit should be the one of the followings: "
                  f"{', '.join(card.SUITS)}. Please, try again.")
            self.play_game_four(card)
            return

        if value == card.random_value and suit == card.random_suit:
            print("Correct! The card was: " + card.prettyfied)
        else:
            self.attempts -= 1
            if self.attempts > 0:
                print(f"Oops! Incorrect! You have {self.attempts} more tryes. "
                      "Try again :)")
                self.show_hint_for_game_four(card, value, suit)
                self.play_game_four(card)
            else:
                print("Incorrect! The card was: " + card.prettyfied)
    
    # Hints

    def show_hint_for_game_two(self, card, player_answer):
        RED = ["h", "d"]
        BLACK = ["c", "s"]
        if card.random_suit == player_answer:
            print("Hint: You've guessed the suit!")
        elif ((card.random_suit in RED and player_answer not in RED)
                or (card.random_suit in BLACK
                    and player_answer not in BLACK)):
            print(f"Hint: The color is opposite!")
        else:
            print(f"Hint: The color is same, but the suit is different!")
            
    def show_hint_for_game_three(self, card, player_answer):
        lowercase_values = [value.lower() for value in card.VALUES]
        card_index = lowercase_values.index(card.random_value)
        player_answer_card_index = lowercase_values.index(player_answer)
        if card_index > player_answer_card_index:
            print("Hint: The card value is higher!")
        else:
            print("Hint: The card value is lower!")

    def show_hint_for_game_four(self, card, player_answer_value, player_answer_suit):
        lowercase_values = [value.lower() for value in card.VALUES]
        card_value_index = lowercase_values.index(card.random_value)
        player_answer_value_index = lowercase_values.index(player_answer_value)
        if card_value_index > player_answer_value_index:
            print("Hint: The card value is higher!")
        elif card_value_index == player_answer_value_index:
            print("Hint: You have guessed the value of the card!")
        else:
            print("Hint: The card value is lower!")
        self.show_hint_for_game_two(card, player_answer_suit)

CardGame().start()
