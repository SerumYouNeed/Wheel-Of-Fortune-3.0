from app.repository.db import execute_query


class PlayerRepository:

    def create_players_table(self):
        execute_query("""
                CREATE TABLE IF NOT EXISTS players (
                    id TEXT PRIMARY KEY,
                    name TEXT NOT NULL,
                    score INTEGER NOT NULL,
                    password TEXT NOT NULL
                )
                """)

    def save_player(self, player):
        execute_query("""
                INSERT INTO players (id, name, score, password)
                      VALUES (:id, :name, :score, :password)
                """, {"id": player.id, "name": player.name, "score": player.score, "password": player.hashed_password})

    def check_identity(self, name: str, password: str) -> bool:
        execute_query("""
                SELECT id FROM players WHERE name = :name AND password = :password
                """, {"name": name, "password": password})
    
