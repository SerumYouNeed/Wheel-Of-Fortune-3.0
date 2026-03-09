from app.domain.puzzle import Puzzle
from app.services.puzzle_service import PuzzleService
from app.services.game_service import GameService
from app.domain.game_state import GameState


def main():

    puzzle = Puzzle("ALA MA KOTA")
    puzzle_service = PuzzleService(puzzle)
    game_state = GameState.RUNNING
    service = GameService(puzzle, puzzle_service, game_state)
    service.start_game()


if __name__ == "__main__":
    main()
