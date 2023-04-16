from classes.card import Card
from typing import Tuple, List
import random


card_values = ["A", "K", "Q", "J", "10", "9", "8", "7", "6", "5", "4", "3", "2"]
card_suits = "♠♥♣♦"


class Deck:
    def __init__(self, cards: List[Card] = []) -> None:
        self.cards = cards

    def __str__(self) -> str:
        """
        Returns all cards joined by a comma
        """
        return ", ".join(str(card) for card in self.cards)

    def split(self) -> Tuple["Deck", "Deck"]:
        """
        Splits the deck evenly into two decks.

        If the original deck contains only 1 card, two empty decks are returned.

        If the deck has an odd number of cards, the last card will be dropped before splitting.

        Returns:
            A tuple containing two new decks, created by splitting the original deck.
        """
        if len(self.cards) % 2 != 0:
            self.cards.pop()

        middle = len(self.cards) // 2

        deck1 = Deck(self.cards[:middle])
        deck2 = Deck(self.cards[middle:])

        return (deck1, deck2)

    def pop(self, number_of_cards: int = 1) -> List[Card]:
        """
        Removes and returns a specified number of cards from the top of the deck.

        Args:
            number_of_cards: The number of cards to remove from the top of the deck. Must be a positive integer.

        Returns:
            A list of the removed cards, in the order they were removed.

        Raises:
            ValueError: If `number_of_cards` is not a positive integer, or if it is greater than the number of cards in the deck.
        """
        if number_of_cards < 1:
            raise ValueError("Minimum value of cards to be removed is 1")
        if len(self.cards) < number_of_cards:
            raise ValueError(
                f"Deck contains {len(self.cards)} cards you are trying to remove {number_of_cards}"
            )

        removed_cards: List[Card] = []

        for _ in range(number_of_cards):
            removed_card = self.cards.pop()
            removed_cards.insert(0, removed_card)

        return removed_cards

    def perpend(self, cards: List[Card]) -> None:
        """
        Adds provided list of cards to the beginning of the current list of cards
        """
        self.cards = cards + self.cards

    @staticmethod
    def generate_shuffled_52_cards_deck() -> List[Card]:
        """
        Generates a standard 52-card deck, shuffles it, and returns the shuffled deck.

        Returns:
            A list of 52 cards, representing a standard deck of playing cards.
        """

        cards: List[Card] = []

        for suit in card_suits:
            for value in card_values:
                cards.append(Card(f"{value}{suit}"))

        random.shuffle(cards)
        return cards
