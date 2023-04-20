from classes.game import Game
from classes.deck import Deck
from classes.card import Card


def test_p1_winning_cards_in_single_round():
    game = Game()

    game.p1_deck = Deck([Card("2♠"), Card("A♠")])
    game.p2_deck = Deck([Card("2♠"), Card("K♠")])

    game.simulate_round()

    assert str(game.p1_deck) == "2♠"
    assert str(game.p2_deck) == "2♠"

    assert len(game.p1_discard_pile) == 2
    assert str(game.p1_discard_pile) == "A♠, K♠"

    assert len(game.p2_discard_pile) == 0
    assert str(game.p2_discard_pile) == ""


def test_war_round():
    game = Game()
    game.p1_deck = Deck([Card("5♠"), Card("3♠"), Card("3♠"), Card("3♠"), Card("A♠")])
    game.p2_deck = Deck([Card("4♠"), Card("3♠"), Card("3♠"), Card("3♠"), Card("A♠")])

    game.simulate_round()

    assert len(game.p1_playing_pile) == 1
    assert str(game.p1_playing_pile) == "A♠"

    assert len(game.p2_playing_pile) == 1
    assert str(game.p2_playing_pile) == "A♠"

    # Now the game is at state of war
    game.simulate_round()

    assert len(game.p1_discard_pile) == 10
    assert str(game.p1_discard_pile) == "A♠, 3♠, 3♠, 3♠, 5♠, A♠, 3♠, 3♠, 3♠, 4♠"


def test_repopulating_deck():
    game = Game()

    game.p1_deck = Deck([])
    game.p1_discard_pile = Deck([Card("2♠"), Card("A♠")])
    game.repopulate_decks()

    assert len(game.p1_deck) == 2
    assert len(game.p1_discard_pile) == 0


def test_not_repopulating_deck_unnecessarily():
    game = Game()

    game.p1_deck = Deck([Card("2♠"), Card("3♠")])
    game.p1_discard_pile = Deck([Card("4♠"), Card("5♠")])
    game.repopulate_decks()

    assert len(game.p1_deck) == 2
    assert len(game.p1_discard_pile) == 2


def test_finds_draw_on_war():
    game = Game()

    game.p1_deck = Deck([])
    game.p1_discard_pile = Deck([Card("A♠"), Card("A♠"), Card("A♠"), Card("A♠")])
    game.p1_playing_pile = Deck([Card("A♠")])

    game.p2_deck = Deck([])
    game.p2_discard_pile = Deck([Card("A♠"), Card("A♠"), Card("A♠"), Card("A♠")])
    game.p2_playing_pile = Deck([Card("A♠")])

    assert game.simulate_round() == False


def test_finds_draw():
    game = Game()

    game.p1_deck = Deck([])
    game.p1_discard_pile = Deck([Card("A♠")])

    game.p2_deck = Deck([])
    game.p2_discard_pile = Deck([Card("A♠")])

    assert game.simulate_round() == False
