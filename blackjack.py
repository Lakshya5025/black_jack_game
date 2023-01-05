import random
def deck():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def calculate_total(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


def compare(user_score, computer_score):
    if user_score > 21 and computer_score > 21:
        return "You went over. You lose 😤"
    if user_score == computer_score:
        return "Draw 🙃"
    elif computer_score == 0:
        return "Lose, opponent has Blackjack 😱"
    elif user_score == 0:
        return "Win with a Blackjack 😎"
    elif user_score > 21:
        return "You went over. You lose 😭"
    elif computer_score > 21:
        return "Opponent went over. You win 😁"
    elif user_score > computer_score:
        return "You win 😃"
    else:
        return "You lose 😤"


user_cards = []
computer_cards = []
game_over = False
for _ in range(2):
    user_cards.append(deck())
    computer_cards.append(deck())
while game_over == False:
    user_total = calculate_total(user_cards)
    computer_total = calculate_total(computer_cards)
    print(f"Your cards: {user_cards}, current score: {user_total}")
    print(f"Computer's first card: {computer_cards[0]}")
    if computer_total == 0 or user_total == 0 or user_total > 21:
        game_over = True
    else:
        choice = input('Type y for another card and n for pass ')
        if choice == "y":
            user_cards.append(deck())
        else:
            game_over = True
while computer_total != 0 and computer_total < 17:
    computer_cards.append(deck())
    computer_total = calculate_total(computer_cards)
print(f"   Your final hand: {user_cards}, final score: {user_total}")
print(f"   Computer's final hand: {computer_cards}, final score: {computer_total}")
print(compare(user_total, computer_total))

