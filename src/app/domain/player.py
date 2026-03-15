import uuid


class Player:

    def __init__(self, name: str, guest=False):
        self.id: str = str(uuid.uuid4())
        self.name = name.upper()
        self.score = 0
        self.guest = guest
        self.password_hash = None
