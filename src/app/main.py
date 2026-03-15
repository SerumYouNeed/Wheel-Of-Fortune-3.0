from app.domain.puzzle import Puzzle
from app.services.puzzle_service import PuzzleService
from app.domain.game_state import GameState
from app.repository.player_repository import PlayerRepository


def main():

    puzzle = Puzzle("ALA MA KOTA")
    player_repository = PlayerRepository()
    player_repository.create_players_table()


if __name__ == "__main__":
    main()
