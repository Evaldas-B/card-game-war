import random
from classes.card import Card
from typing import List, Literal, TypedDict, Optional
from classes.deck import Deck


class RoundHistory(TypedDict, total=False):
    P1: Card
    P2: Card
    Winner: Optional[Literal["P1", "P2", "Draw"]]


class Game:
    def __init__(self) -> None:
        """
        Initializes the game by creating a shuffled 52 card deck and splitting it to both players
        evenly.
        """
        shuffled_deck = Deck(Deck.generate_shuffled_52_cards_deck())
        self.p1_deck, self.p2_deck = shuffled_deck.split()

        self.p1_playing_pile = Deck([])
        self.p2_playing_pile = Deck([])

        self.p1_discard_pile = Deck([])
        self.p2_discard_pile = Deck([])

        self.rounds = 0
        self.history: List[RoundHistory] = []

    def is_war(self):
        """
        Checks if the game is at the sate of war

        Returns: True if game is at state of war, otherwise False
        """
        try:
            return self.p1_playing_pile.cards[-1] == self.p2_playing_pile.cards[-1]
        except:
            return False

    def simulate_round(self) -> bool:
        """
        Has 4 steps:
        1. Tries to repopulate both player decks
        2. Both players places cards on table
        3. Rewards the round winner
        4. Checks if the game is concluded

        While the round is running records moves history

        Returns: True if next round is possible, otherwise False
        """
        self.repopulate_decks()

        # If there is a war each player places 3 cards
        if self.is_war():
            self.p1_playing_pile.append(self.p1_deck.pop(3))
            self.p2_playing_pile.append(self.p2_deck.pop(3))

        # Each player places 1 card
        p1_card = self.p1_deck.pop(1)
        p2_card = self.p2_deck.pop(1)
        round_history: RoundHistory = {
            "P1": p1_card[0],
            "P2": p2_card[0],
        }

        self.p1_playing_pile.append(p1_card)
        self.p2_playing_pile.append(p2_card)

        # Reward round winner with cards if such exists
        if self.p1_playing_pile.cards[-1] > self.p2_playing_pile.cards[-1]:
            table_cards = self.p1_playing_pile.remove_all_cards()
            table_cards += self.p2_playing_pile.remove_all_cards()
            self.p1_discard_pile.cards += table_cards
            round_history["Winner"] = "P1"

        elif self.p2_playing_pile.cards[-1] > self.p1_playing_pile.cards[-1]:
            table_cards = self.p1_playing_pile.remove_all_cards()
            table_cards += self.p2_playing_pile.remove_all_cards()
            self.p2_discard_pile.cards += table_cards
            round_history["Winner"] = "P2"

        else:
            round_history["Winner"] = "Draw"

        self.history.append(round_history)
        self.rounds += 1
        return self.round_possible()

    def repopulate_decks(self) -> None:
        """
        Repopulate the players deck if necessary and possible

        If the game is at state of war repopulate player deck if he less than 4 cards
        If the game is NOT at a state of war repopulate player deck if he has no cards left
        """
        repopulate_p1 = False
        repopulate_p2 = False

        if self.is_war():
            if len(self.p1_deck) < 4 and len(self.p1_discard_pile) > 0:
                repopulate_p1 = True

            if len(self.p2_deck) < 4 and len(self.p2_discard_pile) > 0:
                repopulate_p2 = True

        else:
            if len(self.p1_deck) < 1 and len(self.p1_discard_pile) > 0:
                repopulate_p1 = True

            if len(self.p2_deck) < 1 and len(self.p2_discard_pile) > 0:
                repopulate_p2 = True

        if repopulate_p1:
            self.p1_deck.append(self.p1_discard_pile.remove_all_cards())
            self.p1_deck.shuffle_cards()

        if repopulate_p2:
            self.p2_deck.append(self.p2_discard_pile.remove_all_cards())
            self.p2_deck.shuffle_cards()

    def round_possible(self) -> bool:
        """
        Check if both players have enough remaining cards to participate in next round

        Returns: True if players have enough cards, otherwise False
        """
        p1_remaining_cards = len(self.p1_deck) + len(self.p1_discard_pile)
        p2_remaining_cards = len(self.p2_deck) + len(self.p2_discard_pile)

        if self.is_war():
            if p1_remaining_cards < 4:
                return False
            if p2_remaining_cards < 4:
                return False

        else:
            if p1_remaining_cards < 1:
                return False
            if p2_remaining_cards < 1:
                return False

        return True

    def round_summary(self) -> str:
        """
        Returns round summary in this format:
        ******* Round n *******
        P1: A♦
        P2: K♦
        Winner: P1

        P1 remaining cards: 27
        P2 remaining cards: 25
        """

        return "TODO: should return round summary in specified format"
