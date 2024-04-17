import random
import argparse

def create_deck():
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
    deck = [{'suit': suit, 'rank': rank} for suit in suits for rank in ranks]
    deck.remove({'suit': random.choice(suits), 'rank': 'Queen'})  # Remove one Queen to make Old Maid
    return deck

def deal_cards(deck, num_players):
    random.shuffle(deck)
    return [deck[i::num_players] for i in range(num_players)]

def find_pairs(player_hand):
    pairs_removed = 0
    player_hand.sort(key=lambda card: card['rank'])
    i = 0
    while i < len(player_hand) - 1:
        if player_hand[i]['rank'] == player_hand[i+1]['rank']:
            player_hand.pop(i)
            player_hand.pop(i)
            pairs_removed += 1
        else:
            i += 1
    return pairs_removed

def choose_card_from(player_hand):
    if len(player_hand) == 0:
        return None  # Return None if the player hand is empty
    return random.randint(0, len(player_hand) - 1)

def get_card_index_from_user(next_player_hand_size):
    while True:
        try:
            card_index = int(input(f"Choose a card from the next player's hand (1-{next_player_hand_size}): ")) - 1
            if card_index < 0 or card_index >= next_player_hand_size:
                raise ValueError("Card index out of range. Please try again.")
            return card_index
        except ValueError as e:
            print(f"Invalid input: {e}")

def play_round(players, current_player_index):
    next_player_index = (current_player_index + 1) % len(players)
    if len(players[current_player_index]) == 0 or len(players[next_player_index]) == 0:
        return  # Skip if current or next player has no cards
    if current_player_index == 0:  # Human player
        print("Your hand:", ['{} of {}'.format(card['rank'], card['suit']) for card in players[current_player_index]])
        card_index = get_card_index_from_user(len(players[next_player_index]))
    else:  # Computer player
        card_index = choose_card_from(players[next_player_index])
        if card_index is None:  # Skip if no card to choose
            return
        print(f"Player {current_player_index + 1} chose a card from Player {next_player_index + 1}'s hand.")
    chosen_card = players[next_player_index].pop(card_index)
    players[current_player_index].append(chosen_card)
    find_pairs(players[current_player_index])

def game_loop(players):
    current_player_index = 0
    while not all(len(player_hand) <= 1 for player_hand in players):
        play_round(players, current_player_index)
        current_player_index = (current_player_index + 1) % len(players)

def find_old_maid(players):
    for i, player_hand in enumerate(players):
        if len(player_hand) == 1:
            return i
    return -1

def main(computer_players):
    if computer_players is None:
        print("Error: Number of computer players not provided.")
        parser.print_help()
        return
    deck = create_deck()
    players = deal_cards(deck, computer_players + 1)
    for player_hand in players:
        find_pairs(player_hand)
    game_loop(players)
    old_maid_index = find_old_maid(players)
    if old_maid_index == 0:
        print("Game over. You are the Old Maid!")
    else:
        print(f"Game over. Player {old_maid_index + 1} is the Old Maid!")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Play Old Maid.")
    parser.add_argument('--computer-players', type=int, required=True, choices=range(1, 4), help="Number of computer players (1-3).")
    args = parser.parse_args()
    main(args.computer_players)
