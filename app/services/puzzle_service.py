from app.domain.puzzle import Puzzle

class PuzzleService():

    def __init__(self, puzzle: Puzzle):
        self._puzzle = puzzle 


    def count_guessed_letter(self, letter: str) -> int:
        counter = 0
        for char in self._puzzle._puzzle:
            if char == letter:
                counter += 1
        return counter

    def add_letter_to_guessed(self, letter: str):
        self._puzzle._letters_guessed_before.add(letter)

    def check_letter_in_guessed(self, letter: str) -> bool:
        return True if letter in self._puzzle._letters_guessed_before else False


