from enum import Enum
import puzzle

def main():

    class GameState(Enum):
        TERMINATED = 0
        RUNNING = 1

    game_state = GameState.RUNNING

    puzzle = puzzle.Puzzle('ALA MA KOTA')

    while(game_state):
        letter = input('Podaj literę: ').upper()
        while (not letter.isalpha()):
            letter = input('Podałeś złą wartość. Powtórz: ').upper()
        


if __name__ == "__main__":
    main()