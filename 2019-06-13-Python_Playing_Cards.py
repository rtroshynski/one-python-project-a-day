
# https://stackoverflow.com/questions/50769728/how-to-randomly-shuffle-a-deck-of-cards-among-players
import random


class Card:
    def __init__(self, kind, rank, deck):
        self._kind = kind
        self._rank = rank
        self.deck = deck
        self.where = None

    def __repr__(self):
        return 'Card(kind={}, rank={}'.format(self.kind, self.rank)

    @property
    def kind(self):
        return self._kind

    @property
    def rank(self):
        return self._rank


class Deck:
    def __init__(self):
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        kinds = ['H', 'C', 'D', 'S']
        self.cards = [Card(kind, rank, self) for kind in kinds for rank in ranks]

    def deal(self, players, n=None):
        if any(p.deck is not self for p in players):
            raise RuntimeError('Player {} is not playing the deck'.format(p.id))

        n = n if n is not None else len(self.cards)
        random.shuffle(self.cards)

        for i, card in enumerate(self.cards[:n * len(players)]):
            card.where = players[i % len(players)]


class Player:
    def __init__(self, id, deck):
        self.id = id
        self.deck = deck

    @property
    def hand(self):
        return [card for card in deck.cards if card.where is self]
        
deck = Deck()
players = [Player(id, deck) for id in range(3)]

deck.deal(players, n=4)

for p in players:
    print(p.hand)
