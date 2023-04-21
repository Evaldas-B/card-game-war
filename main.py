from classes.game import Game


def main() -> None:
    game = Game()

    while True:
        if not game.simulate_round():
            break

        print(game.round_summary())

    print(game.round_summary())


if __name__ == "__main__":
    main()
