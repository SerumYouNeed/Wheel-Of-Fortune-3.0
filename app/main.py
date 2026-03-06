from enum import Enum
from app.domain.puzzle import Puzzle
from app.services.puzzle_service import PuzzleService

def main():

    class GameState(Enum):
        RUNNING = "running"
        WON = "won"
        LOST = "lost"

    game_state = GameState.RUNNING

    puzzle = Puzzle('ALA MA KOTA')
    puzzle_service = PuzzleService(puzzle)

    while(game_state == GameState.RUNNING):
        print(puzzle.masked_puzzle)
        letter = input('Podaj literę: ').upper()
        while (not letter.isalpha() or letter in puzzle_service.check_letter_in_guessed(letter)):
            letter = input('Podałeś złą wartość. Powtórz: ').upper()
        if (puzzle.is_letter_in_puzzle(letter)):
            puzzle.reveal(letter)
            guessed_in_turn = puzzle_service.count_guessed_letter(letter)
            print(f'Well done. You found {guessed_in_turn} letter(s) in the puzzle.')

if __name__ == "__main__":
    main()