import pytest
from classes.card import Card
from classes.deck import Deck


def test_if_deck_contains_52_unique_cards():
    deck = Deck(Deck.generate_shuffled_52_cards_deck())

    assert len(deck.cards) == 52

    cards = [str(card) for card in deck.cards]

    # Check if all the values are unique
    assert len(cards) == len(set(cards))


def test_popping_last_card():
    deck = Deck(Deck.generate_shuffled_52_cards_deck())

    assert deck.cards[-1] == deck.pop()[0]


def test_pop_raises_exception_with_invalid_argument():
    deck = Deck(Deck.generate_shuffled_52_cards_deck())

    with pytest.raises(ValueError):
        deck.pop(0)

    with pytest.raises(ValueError):
        deck.pop(-1)


def test_pop_raises_exception_when_removing_more_cards_than_available():
    deck = Deck(Deck.generate_shuffled_52_cards_deck())

    with pytest.raises(ValueError):
        deck.pop(53)


def test_popping_multiple_cards():
    deck = Deck(Deck.generate_shuffled_52_cards_deck())

    last_4_cards = deck.cards[-4:]
    popped_cards = deck.pop(4)

    assert len(last_4_cards) == len(popped_cards)

    for deck_card, popped_card in zip(last_4_cards, popped_cards):
        assert deck_card == popped_card


def test_splitting():
    deck = Deck(Deck.generate_shuffled_52_cards_deck())

    deck1, deck2 = deck.split()

    assert len(deck1.cards) == 26
    assert len(deck2.cards) == 26


def test_splitting_deck_with_1_card():
    deck = Deck([Card("A♠")])

    deck1, deck2 = deck.split()

    assert len(deck1.cards) == 0
    assert len(deck2.cards) == 0


def tests_prepending():
    deck = Deck(["5♠", "6♠"])
    deck.perpend([Card("3♠"), Card("4♠")])

    assert str(deck) == "3♠, 4♠, 5♠, 6♠"
