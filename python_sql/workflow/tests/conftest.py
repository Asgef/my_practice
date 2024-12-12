import pytest
import psycopg2
import psycopg2.extras
import dotenv
import os

dotenv.load_dotenv()
DB_PASS = os.getenv("DB_PASS")


@pytest.fixture(scope="session")
def db_connection():
    conn = psycopg2.connect(f"postgresql://asgef:{DB_PASS}@localhost:5432/asgef_db")
    conn.set_isolation_level(psycopg2.extensions.ISOLATION_LEVEL_READ_COMMITTED)
    yield conn
    conn.close()


@pytest.fixture(autouse=True)
def reset_table(db_connection):
    with db_connection.cursor() as cur:
        cur.execute("TRUNCATE TABLE movies RESTART IDENTITY")
    db_connection.commit()


@pytest.fixture(scope="function")
def db_transaction(db_connection):
    with db_connection:
        with db_connection.cursor() as cur:
            cur.execute("BEGIN")
            yield db_connection
            cur.execute("ROLLBACK")
