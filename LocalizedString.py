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
                    "I'm a bot made by Pavel Laukhin."
                    "I've got one card in mind, but I won't tell you which "
                    "one.\n"
                    "You need to guess the card or its attribute.\n\n"
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
                    "Я бот, созданный Павлом Лаухиным."
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