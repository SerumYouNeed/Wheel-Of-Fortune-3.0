class Puzzle:
    """Represents the puzzle word and tracks guessed letters."""

    def __init__(self, solution: str):
        self.solution = solution.upper()
        self.guessed_letters = set()

    def guess_letter(self, letter: str):
        self.guessed_letters.add(letter.upper())

    def has_letter(self, letter: str) -> bool:
        return letter.upper() in self.solution

    def count_letter(self, letter: str) -> int:
        """Counts the occurrences of a letter in the solution."""
        return self.solution.count(letter.upper())

    def masked(self) -> str:
        """Return puzzle with unguessed letters replaced by '_'."""
        return " ".join(
            letter if letter in self.guessed_letters else "_"
            for letter in self.solution
        )

    def is_solved(self) -> bool:
        """Return True when all letters have been guessed."""
        return all(letter in self.guessed_letters for letter in self.solution)
