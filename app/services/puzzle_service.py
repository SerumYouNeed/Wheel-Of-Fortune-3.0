class PuzzleService():

    def __init__(self, puzzle: Puzzle):
        self._puzzle = puzzle 


    def count_guessed_letter(self, letter: str) -> int:
    counter = 0
    for char in self._puzzle:
        if char == letter:
            counter += 1
    return counter

    def add_letter_to_guessed(sefl, letter: str):
        self._puzzle._letters_before.add(letter)


