import uuid


class Player:

    def __init__(self, name: str):
        self.id: str = str(uuid.uuid4())
        self.name = name.upper()
        self.score = 0
