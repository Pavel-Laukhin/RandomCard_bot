# TODO: Внедрить два языка

from random import choice


class Language:
    ru = "ru"
    en = "en"


class LocalizedString:

    def __init__(self, language: Language):
        self._language = language
        self.strings = {
            Language.en: {
                "greeting": (
                    "Hello, stranger!\n\n"
                    "I will generate a random card, but I won't tell you which "
                    "one.\n"
                    "You should guess the card or its attribute.\n\n"
                    "What do you want to try to guess?\n\n"
                    "1. Color (red or black)\n"
                    "2. Suit (hearts, diamonds, clubs or spades)\n"
                    "3. Card value (e.g. \"2\", \"10\", \"J\", \"Q\", \"K\", "
                    "\"A\", etc.)\n"
                    "4. Card itself (e.g. 2H (two hearts) or KD (king diamonds)"
                    ")\n\n"
                    "Enter 1, 2, 3 or 4."
                ),
                "ask_game_mode": (
                    "\nYou should enter the number. Please, try again."
                ),
                "ask_game_mode_error": (
                    "\nInvalid game mode. Please, try again."
                ),
                "game_one_rules": (
                    "\nGuess the color: Red or Black?"
                ),
                "game_two_rules": (
                    "\nGuess the suit?"
                ),
                "game_three_rules": (
                    "\nGuess the value: "
                ),
                "game_four_rules": (
                    "\nGuess the card itself (like \"2H\" (two hearts) or "
                    "\"KD\" (king diamonds))?"
                ),
                "game_one_error": (
                    "\nSorry, but the acceptable answer is only \"Red\" or "
                    "\"Black\". Please, try again."
                ),
                "game_two_error": (
                    "\nSorry, but the acceptable answer shoud be one of "
                    "the following: "
                ),
                "game_three_error": (
                    "\nSorry, but the acceptable answer shoud be one of "
                    "the following: "
                ),
                "game_four_error": (
                    "\nSorry, but the acceptable answer should consist of the "
                    "value and the suit, no spaces, 2 or 3 letters. "
                    "For example, \"5C\" or \"10S\""
                ),
                "game_four_error_values": (
                    "\nSorry, but the acceptable values shoud be one of "
                    "the following: "
                ),
                "game_four_error_suits": (
                    "\nSorry, but the acceptable suits shoud be one of "
                    "the following: "
                ),
                "correct_answer": (
                    "Correct! The card was "
                ),
                "incorrect_answer": (
                    "Incorrect! The card was "
                ),
                "incorrect_attempts": (
                    "Oops! Incorrect! Attempts left: "
                ),
                "try_again": (
                    "Please, try again."
                ),
                "hint_guessed_suit": (
                    "Hint: You've guessed the suit!"
                ),
                "hint_guessed_value": (
                    "Hint: You have guessed the value of the card!"
                ),
                "hint_color_opposite": (
                    "Hint: The color is opposite!"
                ),
                "hint_color_same": (
                    "Hint: The color is same, but the suit is different!"
                ),
                "hint_value_higher": (
                    "Hint: The card value is higher!"
                ),
                "hint_value_lower": (
                    "Hint: The card value is lower!"
                ),
            },
            Language.ru: {
                "greeting": (
                    "Приветствую вас, незнакомец!\n\n"
                     "Я загадаю случайную карту, но не скажу вам, какую.\n"
                     "Вам нужно угадать эту карту или её аттрибут.\n\n"
                     "Что вы хотите попробовать угадать?\n\n"
                     "1. Цвет (красный или черный)\n"
                     "2. Масть (черви, бубны, крести или пики)\n"
                     "3. Значение (например, \"2\", \"10\", \"В\", \"Д\", \"К\","
                     "\"Т\" и т.п.)\n"
                     "4. Карту целиком (например, 2Ч (двойка черви) или КП "
                     "(король пики))\n\n"
                     "Введите 1, 2, 3 или 4."
                ),
                "ask_game_mode": (
                    "\nНужно ввести число. Пожалуйста, попробуйте снова."
                ),
                "ask_game_mode_error": (
                    "\nНет такого варианта. Пожалуйста, попробуйте ещё раз."
                ),
                "game_one_rules": (
                    "\nУгадайте цвет: Красный или Черный?"
                ),
                "game_two_rules": (
                    "\nУгадайте масть?"
                ),
                "game_three_rules": (
                    "\nУгадайте значение: "
                ),
                "game_four_rules": (
                    "\nУгадайте карту (например, \"2Ч\" (двойка черви) или "
                 "\"ТП\" (туз пики))?"
                ),
                "game_one_error": (
                    "\nИзвините, но допустимый ответ может быть только "
                 "\"Красный\" или \"Черный\". Пожалуйста, попробуйте снова."
                ),
                "game_two_error": (
                    "\nИзвините, но ответом должен быть один из следующих: "
                ),
                "game_three_error": (
                    "\nИзвините, но ответом должен быть один из следующих: "
                ),
                "game_four_error": (
                    "\nИзвините, но ответом должно быть значение и масть, "
                 "без пробелов, 2 или 3 буквы. "
                 "Например, \"5Б\" or \"10Т\""
                ),
                "game_four_error_values": (
                    "\nИзвините, но значение может быть одним из следующих: "
                ),
                "game_four_error_suits": (
                    "\nИзвините, но масть может быть одной из следующих: "
                ),
                "correct_answer": (
                    "Верно! Загаданная карта была "
                ),
                "incorrect_answer": (
                    "Неверно! Загаданная карта была "
                ),
                "incorrect_attempts": (
                    "Ой! Неверно... Осталось попыток: "
                 ),
                "try_again": (
                    "Пожалуйста, попробуйте снова."
                ),
                "hint_guessed_suit": (
                    "Подсказка: Вы угадали масть!"
                ),
                "hint_guessed_value": (
                    "Подсказка: Вы угадали значение карты!"
                ),
                "hint_color_opposite": (
                    "Подсказка: Цвет другой!"
                ),
                "hint_color_same": (
                    "Подсказка: Цвет этот, но масть другая!"
                ),
                "hint_value_higher": (
                    "Подсказка: Значение карты больше!"
                ),
                "hint_value_lower": (
                    "Подсказка: Значение карты меньше!"
                ),
            },
        }
        self._initialize_strings()

    def _initialize_strings(self):
        if self._language in self.strings:
            language_strings = self.strings[self._language]
            self.greeting = language_strings.get("greeting", None)
            self.goodbye = language_strings.get("goodbye", None)
            self.ask_game_mode = language_strings.get("ask_game_mode", None)
            self.ask_game_mode_error = language_strings.get(
                "ask_game_mode_error", 
                None
            )
            self.game_one_rules = language_strings.get("game_one_rules", None)
            self.game_two_rules = language_strings.get("game_two_rules", None)
            self.game_three_rules = language_strings.get(
                "game_three_rules", 
                None
            )
            self.game_four_rules = language_strings.get(
                "game_four_rules", 
                None
            )
            self.game_one_error = language_strings.get("game_one_error", None)
            self.game_two_error = language_strings.get("game_two_error", None)
            self.game_three_error = language_strings.get(
                "game_three_error", 
                None
            )
            self.game_four_error = language_strings.get(
                "game_four_error", 
                None
            )
            self.game_four_error_values = language_strings.get(
                "game_four_error_values", 
                None
            )
            self.game_four_error_suits = language_strings.get(
                "game_four_error_suits", 
                None
            )

            self.correct_answer = language_strings.get("correct_answer", None)
            self.incorrect_answer = language_strings.get(
                "incorrect_answer",
                None
            )
            self.incorrect_attempts = language_strings.get(
                "incorrect_attempts",
                None
            )
            self.try_again = language_strings.get("try_again", None)
            self.hint_guessed_suit = language_strings.get(
                "hint_guessed_suit", 
                None
            )
            self.hint_guessed_value = language_strings.get(
                "hint_guessed_value", 
                None
            )
            self.hint_color_opposite = language_strings.get(
                "hint_color_opposite", 
                None
            )
            self.hint_color_same = language_strings.get(
                "hint_color_same", 
                None
            )
            self.hint_value_higher = language_strings.get(
                "hint_value_higher", 
                None
            )
            self.hint_value_lower = language_strings.get(
                "hint_value_lower", 
                None
            )

        else:
            # The language is not supported
            self.greeting = None
            self.goodbye = None
            self.ask_game_mode = None
            self.ask_game_mode_error = None
            self.game_one_rules = None
            self.game_two_rules = None
            self.game_three_rules = None
            self.game_four_rules = None
            self.game_one_error = None
            self.game_two_error = None
            self.game_three_error = None
            self.game_four_error = None
            self.game_four_error_values = None
            self.game_four_error_suits = None

            self.correct_answer = None
            self.incorrect_answer = None
            self.incorrect_attempts = None
            self.try_again = None
            self.hint_guessed_suit = None
            self.self.hint_guessed_value = None
            self.hint_color_opposite = None
            self.hint_color_same = None
            self.hint_value_higher = None
            self.hint_value_lower = None

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


class CardGame:

    def __init__(self, language):
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


CardGame(Language.ru).start()
