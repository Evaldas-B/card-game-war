from classes.game import Game


def main() -> None:
    game = Game()

    while True:
        print(game.p1_deck)
        print(game.p2_deck)

        print(game.p1_playing_pile)
        print(game.p2_playing_pile)

        if not game.simulate_round():
            break


if __name__ == "__main__":
    main()
