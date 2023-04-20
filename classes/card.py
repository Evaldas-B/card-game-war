import re


class Card:
    def __init__(self, card_expression: str) -> None:
        card_elements = re.match(r"^([AKQJ]|10|[2-9])([♠♥♣♦])$", card_expression)

        if not card_elements:
            raise ValueError("Expecting card_expression to be in this format: A♥")

        self.value = card_elements.group(1)
        self.suit = card_elements.group(2)

    def __str__(self) -> str:
        """
        Returns card in this format: A♥
        """
        return f"{self.value}{self.suit}"

    def __repr__(self) -> str:
        """
        Returns card in this format: A♥
        """
        return f"{self.value}{self.suit}"

    def get_numeric_value(self) -> int:
        """
        Returns the numeric value of the card, where A is 14, K is 13, Q is 12, J is 11, and all other cards
        have their face value as their numeric value (e.g. 10 is 10, 9 is 9, etc.).
        """

        card_values = {
            "A": 14,
            "K": 13,
            "Q": 12,
            "J": 11,
        }

        if self.value in card_values:
            return card_values[self.value]

        return int(self.value)

    def __lt__(self, other) -> bool:
        """
        Compares the numeric value of the current card with another card.

        Args:
            other: Another card to compare with.

        Returns:
            True if the numeric value of the current card is less than the numeric value of the other object.
            False otherwise.
        """
        if not isinstance(other, Card):
            raise NotImplemented

        return self.get_numeric_value() < other.get_numeric_value()

    def __eq__(self, other) -> bool:
        """
        Checks if numeric values of both cards are equal

        Args:
            other: Another card to compare with.

        Returns:
            True if the numeric values of both cards are equal.
            False otherwise.
        """

        if not isinstance(other, Card):
            raise NotImplemented

        return self.get_numeric_value() == other.get_numeric_value()
