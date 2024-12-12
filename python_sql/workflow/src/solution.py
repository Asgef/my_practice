import psycopg2
import dotenv
import os

dotenv.load_dotenv()
DB_PASS = os.getenv("DB_PASS")


conn = psycopg2.connect(f'postgresql://asgef:{DB_PASS}@localhost:5432/asgef_db')


# BEGIN (write your solution here)
def add_movies(connector):
    movies = """
    INSERT INTO movies (title, release_year, duration) 
    VALUES
        ('Godfather', 1972, 175),
        ('The Green Mile', 1999, 189)
    """
    cursor = connector.cursor()
    cursor .execute(movies)
    connector.commit()


def get_all_movies(connector):
    all_movies = "SELECT * FROM movies"
    cursor = connector.cursor()
    cursor.execute(all_movies)
    connector.commit()
    return list(cursor)
# END
