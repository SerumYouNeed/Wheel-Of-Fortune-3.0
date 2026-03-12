from app.repository.db import execute_query


class PlayerRepository:

    def create_players_table(self):
        execute_query("""
                CREATE TABLE IF NOT EXISTS players (
                    id TEXT PRIMARY KEY,
                    name TEXT NOT NULL,
                    score INTEGER NOT NULL
                )
                """)
