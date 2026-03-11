class Puzzle:

    def __init__(self, puzzle: str):
        self._puzzle = puzzle
        self._masked_puzzle = self.mask_puzzle()
        self._puzzle_after_letter_guess = None
 
    @property
    def puzzle(self):
        return self._puzzle

    @property
    def masked_puzzle(self):
        return self._masked_puzzle

    @property
    def puzzle_after_letter_guess(self):
        return self._puzzle_after_letter_guess

    def mask_letter(self, letter):
        return "_" if letter.isalpha() else letter

    def mask_puzzle(self):
        return "".join(self.mask_letter(letter) for letter in self._puzzle)

    def check_answer(self, answer: str) -> bool:
        return self._puzzle == answer.upper()
