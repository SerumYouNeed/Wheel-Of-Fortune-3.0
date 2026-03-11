class GameSession:

    def __init__(self, session_id: str, player_id: str):
        self.session_id = session_id
        self.player_id = player_id
        self._letters_guessed = set()

    def add_letter_to_guessed(self, letter: str):
        self._letters_guessed.add(letter)

    def check_letter_in_guessed(self, letter: str) -> bool:
        return True if letter in self._letters_guessed else False

