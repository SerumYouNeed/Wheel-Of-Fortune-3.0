from app.domain.puzzle import Puzzle


class PuzzleService:

    def __init__(self, puzzle: Puzzle):
        self._puzzle = puzzle

    def count_guessed_letter(self, letter: str) -> int:
        counter = 0
        for char in self._puzzle._puzzle:
            if char == letter:
                counter += 1
        return counter

    def is_letter_in_puzzle(self, letter: str):
        return letter in self._puzzle._puzzle

    def reveal(self, letter: str) -> bool:
        if letter not in self._puzzle._puzzle:
            return False

        new_mask = []

        for i, char in enumerate(self._puzzle._puzzle):
            if char == letter:
                new_mask.append(letter)
            else:
                new_mask.append(self._puzzle._masked_puzzle[i])

        self._puzzle._masked_puzzle = "".join(new_mask)
        return True
