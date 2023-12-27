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
I will generate a random card, but I won't tell you which one.
You should guess the card or its attribute.
What do you want to try to guess?
1. Color (red or black)
2. Suit (hearts, diamonds, clubs or spades)
3. Card value (e.g. "2", "3", "J", "Q", "K", "A", etc.)
4. Card itself (e.g. 2H (two hearts) or KD (king diamonds))
""")

def ask_game_mode():
  return input("Enter 1, 2, 3 or 4\n")
  
game_mode = int(ask_game_mode())
while game_mode not in [1, 2, 3, 4]:
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
  return input("Guess the color: Red or Black?\n")

def ask_card_suit():
  CARD_SUIT_str = "\n".join([f"{suit}. {CARD_SUIT_SYMBOL[suit]}" for suit in CARD_SUIT])
  return input(f"Guess the suit?\n{CARD_SUIT_str}\n")

def ask_card_number():
  return input(f"Guess the number: {', '.join(CARD_NUMBER)}?\n")

def ask_card_itself():
  return input("Guess the card itself (like \"2H\" (two hearts) or \"KD\" (king diamonds))?\n")


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
  player_answer = ask_card_suit()
  while player_answer not in CARD_SUIT:
    print(f"\nSorry, but the acceptable answer shoud be one of: {CARD_SUIT}. Please, try again.")
    player_answer = ask_card_suit()
    
  if player_answer == random_card_suit:
    print("Correct! The card was: " + pretty_card)
  else:
    print("Incorrect! The card was: " + pretty_card)


def play_game_three():
  player_answer = ask_card_number()
  while player_answer not in CARD_NUMBER:
    print(f"\nSorry, but the acceptable answer shoud be one of: {CARD_NUMBER}. Please, try again.")
    player_answer = ask_card_number()
  
  if player_answer == random_card_number:
    print("Correct! The card was: " + pretty_card)
  else:
    print("Incorrect! The card was: " + pretty_card)

def play_game_four():
  tint = "Sorry, but the acceptable answer should consist of the value and the suit, no spaces, 2 or 3 letters. For example, \"5C\" or \"10S\""
  player_answer = ask_card_itself()
  # print(player_answer[2])
  
  if len(player_answer) == 3 and player_answer[:2] != "10":
    print(tint)
    play_game_four()
    return
  elif len(player_answer) != 2:
    print(tint)
    play_game_four()
    return

  if len(player_answer) == 3:
    value = player_answer[:2]
  else:
    value = player_answer[0]
  if value not in CARD_NUMBER:
    print(f"Sorry, but the the value of the card should be one of: {CARD_NUMBER}")
    play_game_four()
    return

  if len(player_answer) == 3:
    suit = player_answer[2]
  else:
    suit = player_answer[1]
  # print(value)
  # print(suit)
  # return
  
  if suit not in CARD_SUIT:
    print(f"\nSorry, but the suit should be the one of: {CARD_SUIT}. Please, try again.")
    play_game_four()
    return

  if value == random_card_number and suit == random_card_suit:
    print("Correct! The card was: " + pretty_card)
  else:
    print("Incorrect! The card was: " + pretty_card)

if game_mode == 1:
  play_game_one()
elif game_mode == 2:
  play_game_two()
elif game_mode == 3:
  play_game_three()
else:
  play_game_four()