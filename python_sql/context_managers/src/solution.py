import psycopg2
import dotenv
import os

dotenv.load_dotenv()
DB_PASS = os.getenv("DB_PASS")


conn = psycopg2.connect(f'postgresql://asgef:{DB_PASS}@localhost:5432/asgef_db')


def get_all_cars(conn):
    sql = """
    SELECT id, brand, model
    FROM cars
    ORDER BY brand ASC;
    """

    with conn.cursor() as curs:
        curs.execute(sql)
        result = curs.fetchall()
    return result
