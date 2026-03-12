class Puzzle:

    def __init__(self, solution: str):
        self.solution = solution.upper()
        self.guessed_letters = set()

    def guess_letter(self, letter: str):
        self.guessed_letters.add(letter.upper())

    def has_letter(self, letter: str) -> bool:
        return letter.upper() in self.solution

    def count_letter(self, letter: str) -> int:
        return self.solution.count(letter.upper())

    def masked(self) -> str:
        return " ".join(
            letter if letter in self.guessed_letters else "_"
            for letter in self.solution
        )

    def is_solved(self) -> bool:
        return all(letter in self.guessed_letters for letter in self.solution)
