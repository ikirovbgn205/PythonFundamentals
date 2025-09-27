deck_of_cards = input().split()
shuffles = int(input())

left_part = []
right_part = []

for current_shuffle in range(shuffles):
    middle_of_the_deck = len(deck_of_cards) // 2
    left_part = deck_of_cards[:middle_of_the_deck]
    right_part = deck_of_cards[middle_of_the_deck:]
    shuffled_cards = []
    for card_index in range(len(left_part)):
        shuffled_cards.append(left_part[card_index])
        shuffled_cards.append(right_part[card_index])
    deck_of_cards = shuffled_cards.copy()

print(deck_of_cards)
