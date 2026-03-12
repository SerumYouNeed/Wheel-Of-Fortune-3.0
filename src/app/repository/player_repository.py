from app.repository.db import get_connection


class PlayerRepository:

    def save(self, player):

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "INSERT INTO players (id, name, score) VALUES (?, ?, ?)",
            (player.id, player.name, player.score)
        )

        conn.commit()
        conn.close()