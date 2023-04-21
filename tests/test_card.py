import pytest
from classes.card import Card


def test_correct_initialization():
    ace_of_clubs = Card("A♧")
    assert str(ace_of_clubs) == "A♧"

    king_of_spades = Card("K♤")
    assert str(king_of_spades) == "K♤"

    ten_of_hearths = Card("10♡")
    assert str(ten_of_hearths) == "10♡"

    two_of_diamonds = Card("2♢")
    assert str(two_of_diamonds) == "2♢"


def test_incorrect_initialization():
    with pytest.raises(ValueError):
        Card("♧A")

    with pytest.raises(ValueError):
        Card("L♧")

    with pytest.raises(ValueError):
        Card("1♧")

    with pytest.raises(ValueError):
        Card("1♧")

    with pytest.raises(ValueError):
        Card("22")

    with pytest.raises(ValueError):
        Card("♧♧")


def test_comparison():
    ace_of_clubs = Card("A♧")
    king_of_hearts = Card("K♡")
    ace_of_diamonds = Card("A♢")

    assert ace_of_clubs > king_of_hearts
    assert king_of_hearts < ace_of_clubs
    assert ace_of_clubs == ace_of_diamonds
