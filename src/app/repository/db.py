from sqlalchemy import create_engine, text

engine = create_engine("sqlite+pysqlite:///data/game.db", echo=True, future=True)


def get_connection():
    return engine.connect()


def execute_query(query: str, params: dict = None):
    """Helper to execute a query with optional parameters and commit changes."""
    with get_connection() as conn:
        conn.execute(text(query), params or {})
        conn.commit()
