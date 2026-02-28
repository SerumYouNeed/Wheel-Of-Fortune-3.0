class Puzzle():

    def __init__(self, puzzle: str):
        self._puzzle = puzzle
        self._masked_puzzle = self.mask_puzzle()
        self._puzzle_after_letter_guess =  None

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
        return '_' if letter.isalpha() else letter

    def is_letter_in_puzzle(self, letter: str):
        return letter in self._puzzle

    def mask_puzzle(self):
        return ''.join(self.mask_letter(letter) for letter in self._puzzle)


    def reveal(self, letter: str) -> bool:
        if letter not in self._puzzle:
            return False

        new_mask = []

        for i, char in enumerate(self._puzzle):
            if char == letter:
                new_mask.append(letter)
            else:
                new_mask.append(self._masked_puzzle[i])

        self._masked_puzzle = ''.join(new_mask)
        return True