# Python Old Maid

## Introduction

Old Maid card game implemented in python using GPT4 in less than 30 minutes.  Proof of concept for code generation, not fully tested.

## Usage

```bash
python app.py --computer-players <1-3>
```

## Example
```
$ python app.py --computer-players 2
Your hand: ['2 of Spades', '6 of Spades', '8 of Clubs', '9 of Spades', 'Ace of Diamonds', 'Jack of Spades', 'Queen of Clubs']
Choose a card from the next player's hand (1-5): 1
Player 2 chose a card from Player 3's hand.
Player 3 chose a card from Player 1's hand.
Your hand: ['2 of Spades', '6 of Spades', '8 of Clubs', '9 of Spades', 'Ace of Diamonds', 'Jack of Spades', 'Queen of Clubs']
Choose a card from the next player's hand (1-5): 1
Player 2 chose a card from Player 3's hand.
Player 3 chose a card from Player 1's hand.
Your hand: ['6 of Spades', '9 of Spades', 'Ace of Diamonds', 'Jack of Spades', 'Queen of Clubs']
Choose a card from the next player's hand (1-5): 1
Player 2 chose a card from Player 3's hand.
Player 3 chose a card from Player 1's hand.
Your hand: ['9 of Spades', 'Jack of Spades', 'Queen of Clubs']
Choose a card from the next player's hand (1-3): 1
Player 2 chose a card from Player 3's hand.
Player 3 chose a card from Player 1's hand.
Your hand: ['7 of Diamonds', 'Jack of Spades', 'Queen of Clubs']
Choose a card from the next player's hand (1-3): 1
Player 2 chose a card from Player 3's hand.
Your hand: ['Jack of Spades', 'Queen of Clubs']
Choose a card from the next player's hand (1-1): 1
Game over. You are the Old Maid!
```
