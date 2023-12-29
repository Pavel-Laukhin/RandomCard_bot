from LocalizedString import LocalizedString
from RandomCard import RandomCard

class CardGame:
    
    def __init__(self, language: str):
        self._GAME_MODES = [1, 2, 3, 4]
        self._game_mode = None
        self._attempts = None
        self._language = language
        self._localizedString = LocalizedString(language)
    
    def start(self):
        self._greeting()
        self._ask_game_mode()
        self._play()
    
    def _greeting(self):
        print(self._localizedString.greeting)
    
    def _ask_game_mode(self):
        try:
            mode = int(input())
        except ValueError:
            print(self._localizedString.ask_game_mode)
            self._ask_game_mode()
            return
    
        if mode not in self._GAME_MODES:
            print(self._localizedString.ask_game_mode_error)
            self._ask_game_mode()
            return
        self._game_mode = mode
    
    def _play(self):
        card = RandomCard(self._language)
    
        if self._game_mode == 1:
            print(self._localizedString.game_one_rules)
            self._play_game_one(card)
    
        elif self._game_mode == 2:
            print(self._localizedString.game_two_rules)
            print(card.suits_list)
            self._attempts = 2
            self._play_game_two(card)
    
        elif self._game_mode == 3:
            print(self._localizedString.game_three_rules, end="")
            print(', '.join(card.VALUES))
            self._attempts = 3
            self._play_game_three(card)
    
        else:
            print(self._localizedString.game_four_rules)
            self._attempts = 3
            self._play_game_four(card)
    
    def _play_game_one(self, card: RandomCard):
        player_answer: str = input().lower()
        acceptable_answers = [color.lower() for color in card.COLORS]
        if player_answer not in acceptable_answers:
            print(self._localizedString.game_one_error)
            self._play_game_one(card)
            return
    
        red_color = card.RED.lower()
        red_suits = [suit.lower() for suit in card.RED_SUITS]
        black_color = card.BLACK.lower()
        black_suits = [suit.lower() for suit in card.BLACK_SUITS]
        if ((player_answer == red_color and card.random_suit in red_suits)
                or (player_answer == black_color
                    and card.random_suit in black_suits)):
            print(self._localizedString.correct_answer + card.prettyfied)
        else:
            print(self._localizedString.incorrect_answer + card.prettyfied)
    
    def _play_game_two(self, card: RandomCard):
        player_answer: str = input().lower()
        lowercase_suits = [suit.lower() for suit in card.SUITS]
        if player_answer not in lowercase_suits:
            print(self._localizedString.game_two_error, end="")
            print(', '.join(card.SUITS))
            print(self._localizedString.try_again)
            self._play_game_two(card)
            return
    
        if player_answer == card.random_suit:
            print(self._localizedString.correct_answer + card.prettyfied)
        else:
            self._attempts -= 1
            if self._attempts > 0:
                print(self._localizedString.incorrect_attempts, end="")
                print(self._attempts)
                print(self._localizedString.try_again)
                self._show_hint_for_game_two(card, player_answer)
                self._play_game_two(card)
            else:
                print(self._localizedString.incorrect_answer + card.prettyfied)
    
    def _play_game_three(self, card: RandomCard):
        player_answer: str = input().lower()
        lowercase_values = [value.lower() for value in card.VALUES]
        if player_answer not in lowercase_values:
            print(self._localizedString.game_three_error, end="")
            print(', '.join(card.VALUES))
            print(self._localizedString.try_again)
            self._play_game_three(card)
            return
    
        if player_answer == card.random_value:
            print(self._localizedString.correct_answer + card.prettyfied)
        else:
            self._attempts -= 1
            if self._attempts > 0:
                print(self._localizedString.incorrect_attempts, end="")
                print(self._attempts)
                print(self._localizedString.try_again)
                self._show_hint_for_game_three(card, player_answer)
                self._play_game_three(card)
            else:
                print(self._localizedString.incorrect_answer + card.prettyfied)
    
    def _play_game_four(self, card: RandomCard):
        player_answer: str = input().lower()
    
        if ((len(player_answer) == 3 and player_answer[:2] != "10")
                or (len(player_answer) not in [2, 3])):
            print(self._localizedString.game_four_error)
            print(self._localizedString.try_again)
            self._play_game_four(card)
            return
    
        value = player_answer[:2] if len(
            player_answer) == 3 else player_answer[0]
        lowercase_values = [value.lower() for value in card.VALUES]
        if value not in lowercase_values:
            print(self._localizedString.game_four_error_values, end="")
            print(', '.join(card.VALUES))
            print(self._localizedString.try_again)
            self._play_game_four(card)
            return
    
        suit = player_answer[2] if len(
            player_answer) == 3 else player_answer[1]
        lowercase_suits = [suit.lower() for suit in card.SUITS]
        if suit not in lowercase_suits:
            print(self._localizedString.game_four_error_suits, end="")
            print(', '.join(card.SUITS))
            print(self._localizedString.try_again)
            self._play_game_four(card)
            return
    
        if value == card.random_value and suit == card.random_suit:
            print(self._localizedString.correct_answer + card.prettyfied)
        else:
            self._attempts -= 1
            if self._attempts > 0:
                print(self._localizedString.incorrect_attempts, end="")
                print(self._attempts)
                print(self._localizedString.try_again)
                self._show_hint_for_game_four(card, value, suit)
                self._play_game_four(card)
            else:
                print(self._localizedString.incorrect_answer + card.prettyfied)
    
    # Hints
    
    def _show_hint_for_game_two(self, card: RandomCard, player_answer):
        RED = [suit.lower() for suit in card.RED_SUITS]
        BLACK = [suit.lower() for suit in card.BLACK_SUITS]
        if card.random_suit == player_answer:
            print(self._localizedString.hint_guessed_suit)
        elif ((card.random_suit in RED and player_answer not in RED)
              or (card.random_suit in BLACK and player_answer not in BLACK)):
            print(self._localizedString.hint_color_opposite)
        else:
            print(self._localizedString.hint_color_same)
    
    def _show_hint_for_game_three(self, card, player_answer):
        lowercase_values = [value.lower() for value in card.VALUES]
        card_index = lowercase_values.index(card.random_value)
        player_answer_card_index = lowercase_values.index(player_answer)
        if card_index > player_answer_card_index:
            print(self._localizedString.hint_value_higher)
        else:
            print(self._localizedString.hint_value_lower)
    
    def _show_hint_for_game_four(self, card, player_answer_value,
                                 player_answer_suit):
        lowercase_values = [value.lower() for value in card.VALUES]
        card_value_index = lowercase_values.index(card.random_value)
        player_answer_value_index = lowercase_values.index(player_answer_value)
        if card_value_index > player_answer_value_index:
            print(self._localizedString.hint_value_higher)
        elif card_value_index == player_answer_value_index:
            print(self._localizedString.hint_guessed_value)
        else:
            print(self._localizedString.hint_value_lower)
        self._show_hint_for_game_two(card, player_answer_suit)
    