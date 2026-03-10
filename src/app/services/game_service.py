from app.domain.puzzle import Puzzle
from app.services.puzzle_service import PuzzleService
from app.domain.game_state import GameState


class GameService:

    def __init__(self, puzzle: Puzzle, service: PuzzleService, game_state: GameState):
        self._puzzle = puzzle
        self._puzzle_service = service
        self._game_state = game_state

    def choose_move(self):
        choice = input("What do you want to do? 1: pick letter, 2: solve the puzzle.")
        match choice:
            case "1":
                return "pick_letter"    
            case "2":   
                return "solve_puzzle"
            case _:
                print("Wrong choice. Try again.")
                return self.choose_move()

    def start_game(self):
        while self._game_state == GameState.RUNNING:
            print(self._puzzle.masked_puzzle)
            letter = input("Podaj literę: ").upper()
            while not letter.isalpha() or self._puzzle_service.check_letter_in_guessed(
                letter
            ):
                letter = input("Podałeś złą wartość. Powtórz: ").upper()
            if self._puzzle_service.is_letter_in_puzzle(letter):
                self._puzzle_service.reveal(letter)
                guessed_in_turn = self._puzzle_service.count_guessed_letter(letter)
                print(
                    f"Well done. You found {guessed_in_turn} letter(s) in the puzzle."
                )
