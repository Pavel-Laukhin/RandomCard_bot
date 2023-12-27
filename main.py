# print("Hello, world!")
# Решетка - Это комментарий

# 'строка' "тоже строка"
# True/False
# [1, 1.5, True, "String"] - list внутри списка можно помещать всё, что угодно, причём одновременно

# Пишем бота
# 1. Приветствие
# 2. Мануал
# 3. Сгенерировать случайную карту
# 4. Вопрос пользователю: красная карта или черная
# 5. Получить ответ пользователя
# 6. Сравнить ответы: 
# 6.1. Если угадал, то программа хвалит и раскрывает карту, 
# 6.2. Eсли нет, то не печалит пользователя и всё равно раскрывает карту

# Домашнее задание
# 1. Проверка на дурака
# 2. Разные уровни сложности (угадать масть или карту, или же дать возможность человеку выбрать изначально уровень сложности)
# 3. Внедрить количество раундов (через цикл while)

from random import choice

# 1.
print("Hello, stranger!")

# 2.
print("""
I will generate a random card.
You should guess the card suit color or the card itself.
What do you want to try to guess?
1. Suit only
2. Card
""")

def ask_game_mode():
  return input("Enter 1 or 2\n")
  
game_mode = ask_game_mode()
while game_mode not in ["1", "2"]:
  print("\nSorry, try again.")
  game_mode = ask_game_mode()

#3. 
CARD_NUMBER = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "К", "A"]
CARD_SUIT = ["H", "D", "C", "S"]
CARD_SUIT_SYMBOL = {"H": "♡", "D": "♢", "C": "♣︎", "S": "♠︎"}

random_card_number = choice(CARD_NUMBER)
random_card_suit = choice(CARD_SUIT)
random_card_suit_symbol = CARD_SUIT_SYMBOL[random_card_suit]

pretty_card = random_card_number + random_card_suit_symbol

#4. -> #5. -> #6.
def ask_color():
  return input("Guess the suit: Red or Black?\n")

def ask_card_number():
  return input(f"Guess the number: {', '.join(CARD_NUMBER)}?\n")

def ask_card_suit():
  CARD_SUIT_str = "\n".join([f"{suit}. {CARD_SUIT_SYMBOL[suit]}" for suit in CARD_SUIT])
  return input(f"Guess the suit?\n{CARD_SUIT_str}\n")

def play_game_one():
  player_answer = ask_color()
  acceptable_answers = ["Red", "Black"]
  while player_answer not in acceptable_answers:
    print("\nSorry, but the acceptable answer is only \"Red\" or \"Black\". Please, try again.")
    player_answer = input("Guess the suit: Red or Black?\n")
    
  if player_answer == "Red" and random_card_suit in ["H", "D"]:
    print("Correct! The card was: " + pretty_card)
  elif player_answer == "Black" and random_card_suit in ["S", "C"]:
    print("Correct! The card was: " + pretty_card)
  else:
    print("Incorrect! The card was: " + pretty_card)

def play_game_two():
  player_answer_one = ask_card_number()
  while player_answer_one not in CARD_NUMBER:
    print(f"\nSorry, but the acceptable answer shoud be one of: {CARD_NUMBER}. Please, try again.")
    player_answer_one = ask_card_number()

  player_answer_two = ask_card_suit()
  while player_answer_two not in CARD_SUIT:
    print(f"\nSorry, but the acceptable answer shoud be one of: {CARD_SUIT}. Please, try again.")
    player_answer_two = ask_card_suit()
  
  if player_answer_one == random_card_number and player_answer_two == random_card_suit:
    print("Correct! The card was: " + pretty_card)
  else:
    print("Incorrect! The card was: " + pretty_card)

if game_mode == "1":
  play_game_one()
else:
  play_game_two()