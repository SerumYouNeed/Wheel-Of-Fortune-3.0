from enum import Enum
from domain.puzzle import Puzzle

def main():

    class GameState(Enum):
        RUNNING = "running"
        WON = "won"
        LOST = "lost"

    game_state = GameState.RUNNING

    puzzle = Puzzle('ALA MA KOTA')

    while(game_state == GameState.RUNNING):
        print(puzzle.masked_puzzle)
        letter = input('Podaj literę: ').upper()
        while (not letter.isalpha()):
            letter = input('Podałeś złą wartość. Powtórz: ').upper()
        if (puzzle.is_letter_in_puzzle(letter)):
            puzzle.reveal(letter)

if __name__ == "__main__":
    main()